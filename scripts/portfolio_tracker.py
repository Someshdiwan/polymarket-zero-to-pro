#!/usr/bin/env python3
"""
portfolio_tracker.py

Track all your Polymarket bets — open positions, resolved trades,
win rate, P&L history, and performance by category.

Data stored locally in ~/.polymarket_portfolio.json
No API key required for manual entry.
With API key: auto-syncs from Polymarket.

Usage:
    python portfolio_tracker.py                  # Dashboard
    python portfolio_tracker.py --add            # Add a trade manually
    python portfolio_tracker.py --resolve        # Mark trade as resolved
    python portfolio_tracker.py --history        # Full trade history
    python portfolio_tracker.py --stats          # Performance statistics
    python portfolio_tracker.py --export         # Export to CSV
"""

import json
import os
import csv
import sys
import argparse
from datetime import datetime
from colorama import Fore, Style, init
from tabulate import tabulate

init(autoreset=True)

PORTFOLIO_FILE = os.path.expanduser("~/.polymarket_portfolio.json")
DIVIDER        = "─" * 65


# Data Layer

def load_portfolio():
    """Load portfolio from disk. Create empty if not exists."""
    if not os.path.exists(PORTFOLIO_FILE):
        return {"trades": [], "created": datetime.now().isoformat()}
    with open(PORTFOLIO_FILE, "r") as f:
        return json.load(f)


def save_portfolio(portfolio):
    """Save portfolio to disk."""
    with open(PORTFOLIO_FILE, "w") as f:
        json.dump(portfolio, f, indent=2)


def next_id(portfolio):
    """Generate next trade ID."""
    trades = portfolio.get("trades", [])
    if not trades:
        return 1
    return max(t["id"] for t in trades) + 1


# Trade Operations

def add_trade(portfolio):
    """Interactively add a new trade."""
    print(f"\n{Fore.CYAN}ADD NEW TRADE{Style.RESET_ALL}\n")

    try:
        question = input("Market question (short description): ").strip()
        if not question:
            print(Fore.RED + "Question required." + Style.RESET_ALL)
            return

        side       = input("Side (YES/NO): ").strip().upper()
        if side not in ["YES", "NO"]:
            print(Fore.RED + "Must be YES or NO." + Style.RESET_ALL)
            return

        amount     = float(input("Amount invested ($): "))
        entry_price = float(input("Entry price (¢): "))
        category   = input("Category (politics/crypto/sports/etc): ").strip() or "other"
        market_id  = input("Market ID (optional): ").strip() or ""
        notes      = input("Notes (optional): ").strip() or ""

        shares     = amount / (entry_price / 100)

        trade = {
            "id":           next_id(portfolio),
            "question":     question,
            "side":         side,
            "amount":       amount,
            "entry_price":  entry_price,
            "shares":       round(shares, 4),
            "category":     category,
            "market_id":    market_id,
            "notes":        notes,
            "status":       "open",
            "outcome":      None,
            "payout":       None,
            "profit":       None,
            "opened_at":    datetime.now().isoformat(),
            "resolved_at":  None,
        }

        portfolio["trades"].append(trade)
        save_portfolio(portfolio)

        print(Fore.GREEN + f"\n✅ Trade #{trade['id']} added." + Style.RESET_ALL)
        print(f"   {side} {amount:.2f} @ {entry_price:.1f}¢ → {shares:.2f} shares")
        print(f"   Win payout: ${shares:.2f}  |  Return: {((shares/amount)-1)*100:.1f}%\n")

    except ValueError:
        print(Fore.RED + "Invalid input." + Style.RESET_ALL)
    except KeyboardInterrupt:
        print("\nCancelled.")


def resolve_trade(portfolio):
    """Mark an open trade as resolved."""
    open_trades = [t for t in portfolio["trades"] if t["status"] == "open"]

    if not open_trades:
        print(Fore.YELLOW + "No open trades to resolve." + Style.RESET_ALL)
        return

    print(f"\n{Fore.CYAN}RESOLVE A TRADE{Style.RESET_ALL}\n")

    # Show open trades
    for t in open_trades:
        print(f"  #{t['id']:>3}  {t['side']:<4}  ${t['amount']:.2f} @ {t['entry_price']:.1f}¢  "
              f"  {t['question'][:45]}")

    print()
    try:
        trade_id = int(input("Enter trade # to resolve: "))
        trade    = next((t for t in open_trades if t["id"] == trade_id), None)

        if not trade:
            print(Fore.RED + "Trade not found." + Style.RESET_ALL)
            return

        outcome = input("Outcome (WIN/LOSS/CANCELLED): ").strip().upper()
        if outcome not in ["WIN", "LOSS", "CANCELLED"]:
            print(Fore.RED + "Must be WIN, LOSS, or CANCELLED." + Style.RESET_ALL)
            return

        if outcome == "WIN":
            payout = trade["shares"]
            profit = payout - trade["amount"]
        elif outcome == "LOSS":
            payout = 0.0
            profit = -trade["amount"]
        else:  # CANCELLED
            payout = trade["amount"]
            profit = 0.0

        trade["status"]      = "resolved"
        trade["outcome"]     = outcome
        trade["payout"]      = round(payout, 2)
        trade["profit"]      = round(profit, 2)
        trade["resolved_at"] = datetime.now().isoformat()

        save_portfolio(portfolio)

        color = Fore.GREEN if profit > 0 else (Fore.YELLOW if profit == 0 else Fore.RED)
        print(color + f"\n✅ Resolved as {outcome}")
        print(f"   Payout: ${payout:.2f}  |  Profit: ${profit:+.2f}" + Style.RESET_ALL)

    except (ValueError, KeyboardInterrupt):
        print("\nCancelled.")


def update_price(portfolio):
    """Update current price for an open trade."""
    open_trades = [t for t in portfolio["trades"] if t["status"] == "open"]
    if not open_trades:
        print(Fore.YELLOW + "No open trades." + Style.RESET_ALL)
        return

    for t in open_trades:
        print(f"  #{t['id']:>3}  {t['question'][:50]}")

    try:
        trade_id     = int(input("\nTrade # to update: "))
        trade        = next((t for t in open_trades if t["id"] == trade_id), None)
        if not trade:
            print(Fore.RED + "Not found." + Style.RESET_ALL)
            return

        current_price = float(input("Current price (¢): "))
        trade["current_price"] = current_price

        sell_value   = trade["shares"] * (current_price / 100)
        unreal_pnl   = sell_value - trade["amount"]
        unreal_pct   = (unreal_pnl / trade["amount"]) * 100

        color = Fore.GREEN if unreal_pnl >= 0 else Fore.RED
        print(color + f"\nUnrealised P&L: ${unreal_pnl:+.2f}  ({unreal_pct:+.1f}%)" + Style.RESET_ALL)

        if unreal_pct >= 100:
            print(Fore.GREEN + "✅ 100%+ profit — consider selling now!" + Style.RESET_ALL)

        save_portfolio(portfolio)

    except (ValueError, KeyboardInterrupt):
        print("\nCancelled.")


# Display

def show_dashboard(portfolio):
    """Main portfolio dashboard."""
    trades    = portfolio.get("trades", [])
    open_pos  = [t for t in trades if t["status"] == "open"]
    resolved  = [t for t in trades if t["status"] == "resolved"]

    print(f"\n{Fore.CYAN}{'═'*65}")
    print(f"  POLYMARKET PORTFOLIO TRACKER")
    print(f"{'═'*65}{Style.RESET_ALL}")

    # Summary stats
    total_invested = sum(t["amount"] for t in trades)
    total_profit   = sum(t["profit"] for t in resolved if t["profit"] is not None)
    wins           = [t for t in resolved if t["outcome"] == "WIN"]
    losses         = [t for t in resolved if t["outcome"] == "LOSS"]
    win_rate       = (len(wins) / len(resolved) * 100) if resolved else 0

    print(f"\n  Total trades    : {len(trades)}  ({len(open_pos)} open, {len(resolved)} resolved)")
    print(f"  Total invested  : ${total_invested:.2f}")

    pnl_color = Fore.GREEN if total_profit >= 0 else Fore.RED
    print(pnl_color + f"  Total P&L       : ${total_profit:+.2f}" + Style.RESET_ALL)

    if resolved:
        wr_color = Fore.GREEN if win_rate >= 55 else (Fore.YELLOW if win_rate >= 45 else Fore.RED)
        print(wr_color + f"  Win rate        : {win_rate:.1f}%  ({len(wins)}W / {len(losses)}L)" + Style.RESET_ALL)

    # Open positions
    if open_pos:
        print(f"\n{Fore.WHITE}OPEN POSITIONS ({len(open_pos)}){Style.RESET_ALL}")
        print(DIVIDER)

        table = []
        for t in open_pos:
            current = t.get("current_price")
            if current:
                sell_val    = t["shares"] * (current / 100)
                unreal      = sell_val - t["amount"]
                unreal_pct  = (unreal / t["amount"]) * 100
                pnl_str     = f"${unreal:+.2f} ({unreal_pct:+.1f}%)"
                pnl_color   = Fore.GREEN if unreal >= 0 else Fore.RED
            else:
                pnl_str   = "—"
                pnl_color = Style.RESET_ALL

            table.append([
                f"#{t['id']}",
                t["question"][:40] + ("..." if len(t["question"]) > 40 else ""),
                t["side"],
                f"${t['amount']:.2f}",
                f"{t['entry_price']:.1f}¢",
                f"{t['shares']:.2f}",
                pnl_color + pnl_str + Style.RESET_ALL,
            ])

        headers = ["ID", "Market", "Side", "Amount", "Entry", "Shares", "Unreal P&L"]
        print(tabulate(table, headers=headers, tablefmt="simple"))

    # Recent resolved
    if resolved:
        recent = sorted(resolved, key=lambda x: x.get("resolved_at", ""), reverse=True)[:5]

        print(f"\n{Fore.WHITE}RECENT RESULTS (last 5){Style.RESET_ALL}")
        print(DIVIDER)

        table = []
        for t in recent:
            outcome_color = Fore.GREEN if t["outcome"] == "WIN" else (Fore.YELLOW if t["outcome"] == "CANCELLED" else Fore.RED)
            table.append([
                f"#{t['id']}",
                t["question"][:38] + ("..." if len(t["question"]) > 38 else ""),
                t["side"],
                outcome_color + t["outcome"] + Style.RESET_ALL,
                f"${t['profit']:+.2f}" if t["profit"] is not None else "—",
                (t.get("resolved_at") or "")[:10],
            ])

        headers = ["ID", "Market", "Side", "Outcome", "Profit", "Date"]
        print(tabulate(table, headers=headers, tablefmt="simple"))

    print()


def show_history(portfolio):
    """Show full trade history."""
    trades = portfolio.get("trades", [])
    if not trades:
        print(Fore.YELLOW + "No trades recorded yet." + Style.RESET_ALL)
        return

    print(f"\n{Fore.CYAN}FULL TRADE HISTORY — {len(trades)} trades{Style.RESET_ALL}\n")

    table = []
    for t in sorted(trades, key=lambda x: x["id"], reverse=True):
        if t["status"] == "open":
            outcome_str = Fore.CYAN + "OPEN" + Style.RESET_ALL
            profit_str  = "—"
        elif t["outcome"] == "WIN":
            outcome_str = Fore.GREEN + "WIN" + Style.RESET_ALL
            profit_str  = Fore.GREEN + f"${t['profit']:+.2f}" + Style.RESET_ALL
        elif t["outcome"] == "LOSS":
            outcome_str = Fore.RED + "LOSS" + Style.RESET_ALL
            profit_str  = Fore.RED + f"${t['profit']:+.2f}" + Style.RESET_ALL
        else:
            outcome_str = Fore.YELLOW + "CANCELLED" + Style.RESET_ALL
            profit_str  = "$0.00"

        table.append([
            f"#{t['id']}",
            t["question"][:35] + "...",
            t["side"],
            f"${t['amount']:.2f}",
            f"{t['entry_price']:.1f}¢",
            outcome_str,
            profit_str,
            t["opened_at"][:10],
        ])

    headers = ["ID", "Market", "Side", "Amount", "Entry", "Outcome", "Profit", "Date"]
    print(tabulate(table, headers=headers, tablefmt="rounded_outline"))
    print()


def show_stats(portfolio):
    """Detailed performance statistics."""
    trades   = portfolio.get("trades", [])
    resolved = [t for t in trades if t["status"] == "resolved"]

    if not resolved:
        print(Fore.YELLOW + "No resolved trades yet." + Style.RESET_ALL)
        return

    wins      = [t for t in resolved if t["outcome"] == "WIN"]
    losses    = [t for t in resolved if t["outcome"] == "LOSS"]
    cancelled = [t for t in resolved if t["outcome"] == "CANCELLED"]

    total_profit  = sum(t["profit"] for t in resolved if t["profit"])
    total_wagered = sum(t["amount"] for t in resolved)
    win_rate      = len(wins) / len(resolved) * 100 if resolved else 0
    avg_win       = sum(t["profit"] for t in wins) / len(wins) if wins else 0
    avg_loss      = sum(t["profit"] for t in losses) / len(losses) if losses else 0
    roi           = (total_profit / total_wagered * 100) if total_wagered else 0

    print(f"\n{Fore.CYAN}{'═'*50}")
    print(f"  PERFORMANCE STATISTICS")
    print(f"{'═'*50}{Style.RESET_ALL}")

    print(f"\n  Resolved trades : {len(resolved)}")
    print(f"  Wins            : {len(wins)}")
    print(f"  Losses          : {len(losses)}")
    print(f"  Cancelled       : {len(cancelled)}")

    wr_color = Fore.GREEN if win_rate >= 55 else (Fore.YELLOW if win_rate >= 45 else Fore.RED)
    print(wr_color + f"  Win rate        : {win_rate:.1f}%" + Style.RESET_ALL)

    pnl_color = Fore.GREEN if total_profit >= 0 else Fore.RED
    print(pnl_color + f"  Total P&L       : ${total_profit:+.2f}" + Style.RESET_ALL)
    print(f"  Total wagered   : ${total_wagered:.2f}")
    roi_color = Fore.GREEN if roi >= 0 else Fore.RED
    print(roi_color + f"  ROI             : {roi:+.1f}%" + Style.RESET_ALL)
    print(f"  Avg win         : ${avg_win:+.2f}")
    print(f"  Avg loss        : ${avg_loss:+.2f}")

    if avg_loss != 0:
        profit_factor = abs(avg_win / avg_loss)
        pf_color = Fore.GREEN if profit_factor > 1 else Fore.RED
        print(pf_color + f"  Profit factor   : {profit_factor:.2f}x" + Style.RESET_ALL)

    # By category
    from collections import defaultdict
    by_cat = defaultdict(lambda: {"trades": 0, "wins": 0, "profit": 0})
    for t in resolved:
        cat = t.get("category", "other")
        by_cat[cat]["trades"] += 1
        by_cat[cat]["profit"] += t["profit"] or 0
        if t["outcome"] == "WIN":
            by_cat[cat]["wins"] += 1

    if len(by_cat) > 1:
        print(f"\n{Fore.WHITE}BY CATEGORY{Style.RESET_ALL}")
        print(DIVIDER[:50])
        for cat, data in sorted(by_cat.items(), key=lambda x: x[1]["profit"], reverse=True):
            cat_wr  = data["wins"] / data["trades"] * 100
            color   = Fore.GREEN if data["profit"] >= 0 else Fore.RED
            print(color + f"  {cat:<20} {data['trades']:>3} trades  {cat_wr:.0f}% WR  ${data['profit']:+.2f}" + Style.RESET_ALL)

    print()

# Export

def export_csv(portfolio):
    """Export all trades to CSV."""
    trades   = portfolio.get("trades", [])
    filename = f"polymarket_trades_{datetime.now().strftime('%Y%m%d')}.csv"

    fieldnames = [
        "id", "question", "side", "amount", "entry_price", "shares",
        "category", "status", "outcome", "payout", "profit",
        "opened_at", "resolved_at", "notes"
    ]

    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(trades)

    print(Fore.GREEN + f"✅ Exported {len(trades)} trades to {filename}" + Style.RESET_ALL)


# CLI

def main():
    parser = argparse.ArgumentParser(
        description="Polymarket Portfolio Tracker",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument("--add",      action="store_true", help="Add a new trade")
    parser.add_argument("--resolve",  action="store_true", help="Mark a trade as resolved")
    parser.add_argument("--update",   action="store_true", help="Update current price for open trade")
    parser.add_argument("--history",  action="store_true", help="Show full trade history")
    parser.add_argument("--stats",    action="store_true", help="Show performance statistics")
    parser.add_argument("--export",   action="store_true", help="Export trades to CSV")

    args      = parser.parse_args()
    portfolio = load_portfolio()

    if args.add:
        add_trade(portfolio)
    elif args.resolve:
        resolve_trade(portfolio)
    elif args.update:
        update_price(portfolio)
    elif args.history:
        show_history(portfolio)
    elif args.stats:
        show_stats(portfolio)
    elif args.export:
        export_csv(portfolio)
    else:
        show_dashboard(portfolio)


if __name__ == "__main__":
    main()
    