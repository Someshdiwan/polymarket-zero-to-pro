"""
AI Strategy Bot — Polymarket

Scans Polymarket for edge opportunities using Claude AI.

Pipeline:
1. Fetch active markets above volume threshold
2. Filter to relevant categories
3. Fetch recent news for each market
4. Ask Claude to estimate probability
5. Calculate edge vs market price
6. Display signals or auto-execute trades

Usage:
    python main.py --scan                    # Scan all markets
    python main.py --scan --category crypto  # Scan specific category
    python main.py --scan --execute          # Scan and auto-execute signals
    python main.py --scan --dry-run          # Scan without real trades
    python main.py --schedule                # Run every 30 minutes

Author: polymarket-zero-to-pro
"""

import os
import sys
import time
import argparse
import logging
import schedule
from datetime import datetime
from dotenv import load_dotenv
from colorama import Fore, Style, init

# Add parent directory to path for shared utilities
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from market_analyzer import scan_markets, display_signals
from news_fetcher import fetch_news

load_dotenv()
init(autoreset=True)


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
}

# Daily loss tracker
daily_loss = 0.0

# Logging

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/ai_bot.log"),
        logging.StreamHandler(sys.stdout),
    ],
)

logger = logging.getLogger(__name__)


# Client Setup
def get_client():
    """Initialise Polymarket CLOB client."""
    try:
        from py_clob_client.client import ClobClient
        from py_clob_client.clob_types import ApiCreds

        creds = ApiCreds(
            api_key=CONFIG["api_key"],
            api_secret=CONFIG["api_secret"],
            api_passphrase=CONFIG["api_passphrase"],
        )

        return ClobClient(
            "https://clob.polymarket.com",
            key=CONFIG["private_key"],
            chain_id=137,
            creds=creds,
        )

    except Exception as e:
        logger.error(f"Failed to initialise client: {e}")
        sys.exit(1)


# Market Fetcher

def fetch_markets(client, category=None, limit=50):
    """Fetch and filter markets from Polymarket."""
    try:
        logger.info("Fetching markets from Polymarket...")
        all_markets = client.get_markets()

        # Filter by volume
        filtered = [
            m for m in all_markets
            if float(m.get("volume", 0)) >= CONFIG["min_volume"]
        ]

        # Filter by category
        if category:
            filtered = [
                m for m in filtered
                if category.lower() in m.get("category", "").lower()
            ]

        # Skip near-resolved markets
        filtered = [
            m for m in filtered
            if 5 <= float(m.get("outcomePrices", [0.5])[0]) * 100 <= 95
        ]

        # Sort by volume
        filtered.sort(key=lambda x: float(x.get("volume", 0)), reverse=True)

        logger.info(f"Found {len(filtered)} qualifying markets")
        return filtered[:limit]

    except Exception as e:
        logger.error(f"Error fetching markets: {e}")
        return []


# Trade Executor

def execute_signal(client, signal):
    """
    Execute a trade based on an AI signal.

    Args:
        client: ClobClient instance
        signal: Signal dict from market_analyzer

    Returns:
        True if successful, False otherwise
    """
    global daily_loss

    # Daily loss limit check
    if daily_loss >= CONFIG["daily_loss_limit"]:
        logger.warning(f"Daily loss limit ${CONFIG['daily_loss_limit']} reached. No more trades today.")
        return False

    market_id = signal["market_id"]
    direction = signal["direction"]
    amount    = CONFIG["max_bet_size"]

    # Dry run mode
    if CONFIG["dry_run"]:
        print(Fore.YELLOW + f"\n[DRY RUN] Signal: {signal['recommendation']}")
        print(f"  Market: {signal['question'][:55]}...")
        print(f"  Amount: ${amount:.2f}")
        print(f"  Edge:   {signal['edge']:.1%}")
        print(f"  EV:     ${signal['ev_on_2usd']:+.2f}" + Style.RESET_ALL)
        return True

    # Live execution
    try:
        from py_clob_client.clob_types import MarketOrderArgs, OrderType

        logger.info(f"Executing: {direction} ${amount:.2f} on {market_id}")

        order_args     = MarketOrderArgs(token_id=market_id, amount=amount)
        signed_order   = client.create_market_order(order_args)
        response       = client.post_order(signed_order, OrderType.FOK)

        logger.info(f"Order response: {response}")

        # Log trade
        _log_signal_trade(signal, amount, response)

        print(Fore.GREEN + f"✅ Executed: {direction} ${amount:.2f}" + Style.RESET_ALL)
        return True

    except Exception as e:
        logger.error(f"Execution failed: {e}")
        daily_loss += amount
        return False


def _log_signal_trade(signal, amount, response):
    """Log AI-executed trade to CSV."""
    import csv

    log_path = "logs/ai_trades.csv"
    fieldnames = [
        "timestamp", "question", "direction", "amount",
        "edge", "ev", "ai_probability", "market_prob", "response"
    ]

    write_header = not os.path.exists(log_path)

    with open(log_path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
        writer.writerow({
            "timestamp":    datetime.now().isoformat(),
            "question":     signal["question"][:80],
            "direction":    signal["direction"],
            "amount":       amount,
            "edge":         f"{signal['edge']:.3f}",
            "ev":           f"{signal['ev_on_2usd']:.3f}",
            "ai_probability": f"{signal['ai_probability']:.3f}",
            "market_prob":  f"{signal['market_prob']:.3f}",
            "response":     str(response)[:100],
        })


# Main Scan Loop

def run_scan(client, category=None, execute=False):
    """
    Run a full market scan cycle.

    Args:
        client: ClobClient instance
        category: Optional category filter
        execute: Whether to auto-execute signals
    """
    print(f"\n{'='*60}")
    print(f"SCAN STARTED: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Mode: {'DRY RUN' if CONFIG['dry_run'] else 'LIVE'}")
    print(f"{'='*60}")

    # Fetch markets
    markets = fetch_markets(client, category=category)

    if not markets:
        print(Fore.YELLOW + "No qualifying markets found." + Style.RESET_ALL)
        return

    # Scan for signals
    signals = scan_markets(markets)

    # Display results
    display_signals(signals)

    # Execute if requested
    if execute and signals:
        print(f"\n{Fore.CYAN}Executing {len(signals)} signal(s)...{Style.RESET_ALL}")
        for signal in signals:
            success = execute_signal(client, signal)
            if success:
                time.sleep(2)  # Rate limiting between orders

    print(f"\nScan complete. Found {len(signals)} signal(s).")
    print(f"Daily loss so far: ${daily_loss:.2f} / ${CONFIG['daily_loss_limit']:.2f}")


# Scheduler

def start_scheduler(client, category=None, execute=False, interval_minutes=30):
    """Run scan on a schedule."""
    print(f"Starting scheduler: every {interval_minutes} minutes")
    print("Press Ctrl+C to stop\n")

    # Run immediately on start
    run_scan(client, category=category, execute=execute)

    # Schedule recurring runs
    schedule.every(interval_minutes).minutes.do(
        run_scan,
        client=client,
        category=category,
        execute=execute,
    )

    while True:
        try:
            schedule.run_pending()
            time.sleep(60)
        except KeyboardInterrupt:
            print("\nScheduler stopped.")
            break


# Performance Report

def show_performance():
    """Display performance stats from trade log."""
    import csv

    log_path = "logs/ai_trades.csv"

    if not os.path.exists(log_path):
        print("No trade history found.")
        return

    trades = []
    with open(log_path, "r") as f:
        reader = csv.DictReader(f)
        trades = list(reader)

    if not trades:
        print("No trades logged yet.")
        return

    total        = len(trades)
    total_bet    = sum(float(t["amount"]) for t in trades)
    avg_edge     = sum(float(t["edge"]) for t in trades) / total
    avg_ev       = sum(float(t["ev"]) for t in trades) / total

    print(f"\n{'='*50}")
    print("AI BOT PERFORMANCE SUMMARY")
    print(f"{'='*50}")
    print(f"Total trades:    {total}")
    print(f"Total wagered:   ${total_bet:.2f}")
    print(f"Average edge:    {avg_edge:.1%}")
    print(f"Average EV:      ${avg_ev:.2f}")
    print(f"{'='*50}\n")


# CLI

def main():
    parser = argparse.ArgumentParser(
        description="Polymarket AI Strategy Bot",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument("--scan",       action="store_true", help="Scan markets for edge")
    parser.add_argument("--execute",    action="store_true", help="Auto-execute signals found")
    parser.add_argument("--schedule",   action="store_true", help="Run on recurring schedule")
    parser.add_argument("--dry-run",    action="store_true", help="Simulate without real trades")
    parser.add_argument("--performance",action="store_true", help="Show trade performance stats")
    parser.add_argument("--category",   type=str,            help="Market category filter")
    parser.add_argument("--interval",   type=int, default=30,help="Schedule interval in minutes")

    args = parser.parse_args()

    if args.dry_run:
        CONFIG["dry_run"] = True

    # Validate credentials
    if not CONFIG["api_key"] or CONFIG["api_key"] == "your_api_key_here":
        print(Fore.RED + "❌ API credentials not configured.")
        print("Copy bots/starter-bot/.env.example to bots/ai-strategy-bot/.env" + Style.RESET_ALL)
        sys.exit(1)

    print(Fore.CYAN + "\nPolymarket AI Strategy Bot" + Style.RESET_ALL)
    print(f"Mode:      {'DRY RUN' if CONFIG['dry_run'] else '⚡ LIVE TRADING'}")
    print(f"Max bet:   ${CONFIG['max_bet_size']}")
    print(f"Min edge:  {CONFIG['min_edge']:.0%}")
    print(f"Min vol:   ${CONFIG['min_volume']:,.0f}")

    if args.performance:
        show_performance()
        return

    client = get_client()

    if args.schedule:
        start_scheduler(
            client,
            category=args.category,
            execute=args.execute,
            interval_minutes=args.interval,
        )
    elif args.scan:
        run_scan(client, category=args.category, execute=args.execute)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
    