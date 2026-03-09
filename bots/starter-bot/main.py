"""
Polymarket Starter Bot
======================
A simple CLI bot to interact with Polymarket markets.
Supports: fetching markets, viewing positions, placing trades.

Usage:
    python main.py --markets          # List active markets
    python main.py --positions        # View your positions
    python main.py --trade            # Interactive trade mode
    python main.py --dry-run --trade  # Test without real money

Author: polymarket-zero-to-pro
"""

import os
import sys
import json
import argparse
import logging
from datetime import datetime
from dotenv import load_dotenv
from tabulate import tabulate
from colorama import Fore, Style, init

# Initialise colorama for colored terminal output
init(autoreset=True)

# Load environment variables
load_dotenv()


# Configuration
CONFIG = {
    "api_key":          os.getenv("POLY_API_KEY"),
    "api_secret":       os.getenv("POLY_API_SECRET"),
    "api_passphrase":   os.getenv("POLY_API_PASSPHRASE"),
    "private_key":      os.getenv("PRIVATE_KEY"),
    "dry_run":          os.getenv("DRY_RUN", "true").lower() == "true",
    "max_bet_size":     float(os.getenv("MAX_BET_SIZE", "2.00")),
    "daily_loss_limit": float(os.getenv("DAILY_LOSS_LIMIT", "10.00")),
    "min_volume":       float(os.getenv("MIN_MARKET_VOLUME", "50000")),
    "min_edge":         float(os.getenv("MIN_EDGE_THRESHOLD", "0.10")),
    "log_file":         os.getenv("LOG_FILE", "logs/trades.log"),
}

# Logging Setup

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(CONFIG["log_file"]),
        logging.StreamHandler(sys.stdout),
    ],
)

logger = logging.getLogger(__name__)


# Polymarket Client
def get_client():
    """Initialise and return Polymarket CLOB client."""
    try:
        from py_clob_client.client import ClobClient
        from py_clob_client.clob_types import ApiCreds

        host = "https://clob.polymarket.com"
        chain_id = 137  # Polygon mainnet

        creds = ApiCreds(
            api_key=CONFIG["api_key"],
            api_secret=CONFIG["api_secret"],
            api_passphrase=CONFIG["api_passphrase"],
        )

        client = ClobClient(
            host,
            key=CONFIG["private_key"],
            chain_id=chain_id,
            creds=creds,
        )

        return client

    except ImportError:
        logger.error("py-clob-client not installed. Run: pip install py-clob-client")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Failed to initialise client: {e}")
        sys.exit(1)


# Market Functions
def fetch_markets(client, limit=20, category=None):
    """
    Fetch active markets from Polymarket.

    Args:
        client: ClobClient instance
        limit: Number of markets to fetch
        category: Filter by category (politics, crypto, sports etc)

    Returns:
        List of market dictionaries
    """
    try:
        logger.info("Fetching active markets...")
        markets = client.get_markets()

        # Filter by minimum volume
        filtered = [
            m for m in markets
            if float(m.get("volume", 0)) >= CONFIG["min_volume"]
        ]

        # Filter by category if specified
        if category:
            filtered = [
                m for m in filtered
                if category.lower() in m.get("category", "").lower()
            ]

        # Sort by volume descending
        filtered.sort(key=lambda x: float(x.get("volume", 0)), reverse=True)

        return filtered[:limit]

    except Exception as e:
        logger.error(f"Error fetching markets: {e}")
        return []


def display_markets(markets):
    """Display markets in formatted table."""
    if not markets:
        print(Fore.YELLOW + "No markets found matching criteria.")
        return

    table_data = []
    for i, market in enumerate(markets, 1):
        yes_price = market.get("outcomePrices", ["N/A"])[0]
        no_price  = market.get("outcomePrices", ["N/A", "N/A"])[1]
        volume    = float(market.get("volume", 0))

        # Colour code by probability
        yes_float = float(yes_price) if yes_price != "N/A" else 0
        if yes_float > 0.7:
            price_str = Fore.GREEN + f"{yes_float:.0%}" + Style.RESET_ALL
        elif yes_float < 0.3:
            price_str = Fore.RED + f"{yes_float:.0%}" + Style.RESET_ALL
        else:
            price_str = Fore.YELLOW + f"{yes_float:.0%}" + Style.RESET_ALL

        table_data.append([
            i,
            market.get("question", "N/A")[:60] + "...",
            f"YES {yes_price}¢ | NO {no_price}¢",
            f"${volume:,.0f}",
            market.get("endDateIso", "N/A")[:10],
        ])

    headers = ["#", "Market", "Prices", "Volume", "Closes"]
    print(Fore.CYAN + "\n=== ACTIVE MARKETS ===" + Style.RESET_ALL)
    print(tabulate(table_data, headers=headers, tablefmt="rounded_outline"))


def get_market_by_id(client, market_id):
    """Fetch single market by ID."""
    try:
        return client.get_market(market_id)
    except Exception as e:
        logger.error(f"Error fetching market {market_id}: {e}")
        return None


# Position Functions
def fetch_positions(client):
    """Fetch current open positions."""
    try:
        logger.info("Fetching positions...")
        positions = client.get_positions()
        return positions
    except Exception as e:
        logger.error(f"Error fetching positions: {e}")
        return []


def display_positions(positions):
    """Display positions in formatted table."""
    if not positions:
        print(Fore.YELLOW + "No open positions found.")
        return

    table_data = []
    total_value = 0
    total_invested = 0

    for pos in positions:
        current_value = float(pos.get("currentValue", 0))
        size          = float(pos.get("size", 0))
        avg_price     = float(pos.get("avgPrice", 0))
        invested      = size * avg_price

        pnl        = current_value - invested
        pnl_pct    = (pnl / invested * 100) if invested > 0 else 0
        pnl_color  = Fore.GREEN if pnl >= 0 else Fore.RED

        total_value    += current_value
        total_invested += invested

        table_data.append([
            pos.get("market", "N/A")[:40] + "...",
            pos.get("outcome", "N/A"),
            f"{size:.1f}",
            f"{avg_price:.3f}¢",
            f"${current_value:.2f}",
            pnl_color + f"${pnl:+.2f} ({pnl_pct:+.1f}%)" + Style.RESET_ALL,
        ])

    headers = ["Market", "Side", "Shares", "Avg Price", "Value", "P&L"]
    print(Fore.CYAN + "\n=== OPEN POSITIONS ===" + Style.RESET_ALL)
    print(tabulate(table_data, headers=headers, tablefmt="rounded_outline"))

    total_pnl = total_value - total_invested
    print(f"\nTotal Value: ${total_value:.2f}")
    print(f"Total Invested: ${total_invested:.2f}")
    color = Fore.GREEN if total_pnl >= 0 else Fore.RED
    print(color + f"Total P&L: ${total_pnl:+.2f}" + Style.RESET_ALL)



# Edge Calculator
def calculate_edge(your_probability, market_price):
    """
    Calculate edge between your estimate and market price.

    Args:
        your_probability: Your estimated probability (0.0 - 1.0)
        market_price: Current market price in cents (0 - 100)

    Returns:
        edge as float, positive = good bet
    """
    market_prob = market_price / 100
    edge = your_probability - market_prob
    return edge


def calculate_ev(your_probability, market_price_cents, stake):
    """
    Calculate expected value of a bet.

    Args:
        your_probability: Your win probability (0.0 - 1.0)
        market_price_cents: Current price in cents
        stake: Amount to bet in USD

    Returns:
        Expected value in USD
    """
    price        = market_price_cents / 100
    shares       = stake / price
    profit_if_win = shares - stake
    loss_if_lose  = stake

    ev = (your_probability * profit_if_win) - ((1 - your_probability) * loss_if_lose)
    return ev


def calculate_kelly(your_probability, market_price_cents, bankroll):
    """
    Calculate Kelly Criterion optimal bet size.

    Args:
        your_probability: Your win probability
        market_price_cents: Market price in cents
        bankroll: Total available balance

    Returns:
        Recommended bet size in USD
    """
    price  = market_price_cents / 100
    b      = (1 / price) - 1   # Net odds
    p      = your_probability
    q      = 1 - p

    kelly_fraction = (b * p - q) / b
    kelly_fraction = max(0, kelly_fraction)  # No negative bets

    # Half Kelly for safety
    half_kelly     = kelly_fraction * 0.5
    optimal_bet    = bankroll * half_kelly

    # Cap at max bet size
    optimal_bet    = min(optimal_bet, CONFIG["max_bet_size"])

    return optimal_bet


# Trade Execution
def place_trade(client, market_id, outcome, amount):
    """
    Place a trade on Polymarket.

    Args:
        client: ClobClient instance
        market_id: Market condition ID
        outcome: "YES" or "NO"
        amount: USD amount to bet

    Returns:
        Order response or None if dry run
    """
    # Safety checks
    if amount > CONFIG["max_bet_size"]:
        logger.warning(f"Bet ${amount} exceeds max bet size ${CONFIG['max_bet_size']}. Capping.")
        amount = CONFIG["max_bet_size"]

    if amount <= 0:
        logger.error("Bet amount must be positive.")
        return None

    # Dry run mode
    if CONFIG["dry_run"]:
        logger.info(f"[DRY RUN] Would place: {outcome} ${amount:.2f} on market {market_id}")
        print(Fore.YELLOW + f"\n[DRY RUN] Trade simulated:")
        print(f"  Market:  {market_id}")
        print(f"  Side:    {outcome}")
        print(f"  Amount:  ${amount:.2f}")
        print(Fore.YELLOW + "  Set DRY_RUN=false in .env to execute real trades" + Style.RESET_ALL)
        return {"status": "dry_run", "outcome": outcome, "amount": amount}

    # Live trade execution
    try:
        from py_clob_client.clob_types import MarketOrderArgs, OrderType

        logger.info(f"Placing LIVE trade: {outcome} ${amount:.2f} on {market_id}")

        order_args = MarketOrderArgs(
            token_id=market_id,
            amount=amount,
        )

        signed_order = client.create_market_order(order_args)
        response     = client.post_order(signed_order, OrderType.FOK)

        logger.info(f"Order placed: {response}")
        log_trade(market_id, outcome, amount, response)

        return response

    except Exception as e:
        logger.error(f"Failed to place trade: {e}")
        return None


def log_trade(market_id, outcome, amount, response):
    """Log trade to CSV file for review."""
    os.makedirs("logs", exist_ok=True)
    log_path = "logs/trade_history.csv"

    header = "timestamp,market_id,outcome,amount,response\n"
    if not os.path.exists(log_path):
        with open(log_path, "w") as f:
            f.write(header)

    with open(log_path, "a") as f:
        timestamp = datetime.now().isoformat()
        f.write(f"{timestamp},{market_id},{outcome},{amount},{json.dumps(response)}\n")


# Interactive Trade Mode

def interactive_trade(client):
    """Interactive CLI for placing trades with edge calculation."""
    print(Fore.CYAN + "\n=== INTERACTIVE TRADE MODE ===" + Style.RESET_ALL)

    if CONFIG["dry_run"]:
        print(Fore.YELLOW + "⚠ DRY RUN MODE — No real money will be spent\n" + Style.RESET_ALL)

    # Step 1: Fetch and display markets
    markets = fetch_markets(client, limit=10)
    display_markets(markets)

    if not markets:
        print("No markets available.")
        return

    # Step 2: Select market
    try:
        choice = int(input("\nSelect market number: ")) - 1
        if choice < 0 or choice >= len(markets):
            print(Fore.RED + "Invalid selection." + Style.RESET_ALL)
            return
        market = markets[choice]
    except ValueError:
        print(Fore.RED + "Invalid input." + Style.RESET_ALL)
        return

    print(f"\nSelected: {market.get('question')}")
    yes_price = float(market.get("outcomePrices", [0.5])[0])
    no_price  = round(1 - yes_price, 4)
    print(f"Current:  YES {yes_price*100:.1f}¢  |  NO {no_price*100:.1f}¢")

    # Step 3: Choose side
    side = input("\nBet YES or NO? ").strip().upper()
    if side not in ["YES", "NO"]:
        print(Fore.RED + "Must be YES or NO." + Style.RESET_ALL)
        return

    market_price = yes_price * 100 if side == "YES" else no_price * 100

    # Step 4: Enter your probability estimate
    try:
        your_prob = float(input(f"Your estimated probability for {side} (0-100): ")) / 100
    except ValueError:
        print(Fore.RED + "Invalid probability." + Style.RESET_ALL)
        return

    # Step 5: Calculate edge and EV
    edge = calculate_edge(your_prob, market_price)
    ev   = calculate_ev(your_prob, market_price, CONFIG["max_bet_size"])

    print(f"\n{'─'*40}")
    print(f"Market price:    {market_price:.1f}¢ ({market_price:.1f}% implied)")
    print(f"Your estimate:   {your_prob*100:.1f}%")

    edge_color = Fore.GREEN if edge > 0 else Fore.RED
    print(edge_color + f"Edge:            {edge*100:+.1f}%" + Style.RESET_ALL)

    ev_color = Fore.GREEN if ev > 0 else Fore.RED
    print(ev_color + f"EV on ${CONFIG['max_bet_size']:.0f} bet:  ${ev:+.2f}" + Style.RESET_ALL)
    print(f"{'─'*40}")

    # Step 6: Edge check
    if edge < CONFIG["min_edge"]:
        print(Fore.RED + f"\n⚠ Edge {edge*100:.1f}% is below minimum {CONFIG['min_edge']*100:.0f}%")
        proceed = input("Proceed anyway? (y/N): ").strip().lower()
        if proceed != "y":
            print("Trade cancelled.")
            return

    # Step 7: Kelly sizing
    try:
        balance = float(input("\nYour current balance ($): "))
    except ValueError:
        balance = 20.0

    kelly_bet = calculate_kelly(your_prob, market_price, balance)
    print(f"\nKelly recommended bet: ${kelly_bet:.2f}")

    try:
        amount = float(input(f"Enter bet amount (max ${CONFIG['max_bet_size']}): $"))
    except ValueError:
        print(Fore.RED + "Invalid amount." + Style.RESET_ALL)
        return

    # Step 8: Confirm
    print(f"\n{'─'*40}")
    print(f"CONFIRM TRADE:")
    print(f"  Market: {market.get('question')[:50]}...")
    print(f"  Side:   {side}")
    print(f"  Amount: ${amount:.2f}")
    print(f"  Edge:   {edge*100:+.1f}%")
    print(f"  EV:     ${ev:+.2f}")
    print(f"{'─'*40}")

    confirm = input("Confirm trade? (y/N): ").strip().lower()
    if confirm != "y":
        print("Trade cancelled.")
        return

    # Step 9: Execute
    token_id = market.get("conditionId") or market.get("id")
    response = place_trade(client, token_id, side, amount)

    if response:
        print(Fore.GREEN + "\n✅ Trade executed successfully!" + Style.RESET_ALL)
    else:
        print(Fore.RED + "\n❌ Trade failed. Check logs." + Style.RESET_ALL)



# Main CLI

def main():
    parser = argparse.ArgumentParser(
        description="Polymarket Starter Bot",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "--markets",
        action="store_true",
        help="List active markets",
    )
    parser.add_argument(
        "--positions",
        action="store_true",
        help="View your open positions",
    )
    parser.add_argument(
        "--trade",
        action="store_true",
        help="Interactive trade mode",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate trades without real money",
    )
    parser.add_argument(
        "--category",
        type=str,
        help="Filter markets by category (politics, crypto, sports)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=20,
        help="Number of markets to display",
    )

    args = parser.parse_args()

    # Override dry run from CLI flag
    if args.dry_run:
        CONFIG["dry_run"] = True

    # Validate API credentials
    if not CONFIG["api_key"] or CONFIG["api_key"] == "your_api_key_here":
        print(Fore.RED + "❌ API credentials not set.")
        print("Copy .env.example to .env and fill in your credentials." + Style.RESET_ALL)
        sys.exit(1)

    print(Fore.CYAN + "Polymarket Starter Bot" + Style.RESET_ALL)
    print(f"Mode: {'DRY RUN' if CONFIG['dry_run'] else 'LIVE TRADING'}")
    print(f"Max bet: ${CONFIG['max_bet_size']}")
    print(f"Min edge: {CONFIG['min_edge']*100:.0f}%\n")

    client = get_client()

    if args.markets:
        markets = fetch_markets(client, limit=args.limit, category=args.category)
        display_markets(markets)

    elif args.positions:
        positions = fetch_positions(client)
        display_positions(positions)

    elif args.trade:
        interactive_trade(client)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
