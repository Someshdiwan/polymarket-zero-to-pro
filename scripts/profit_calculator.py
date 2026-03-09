#!/usr/bin/env python3
"""
profit_calculator.py

Calculate profits, payouts, returns, and break-even prices
for Polymarket trades.

Usage:
    python profit_calculator.py                  # Interactive mode
    python profit_calculator.py --amount 10 --price 25 --current 60
    python profit_calculator.py --batch          # Analyse multiple trades
"""

import argparse
from colorama import Fore, Style, init

init(autoreset=True)

DIVIDER = "─" * 50


# Core Calculations
def calc_shares(amount, price_cents):
    """Shares purchased = amount invested / price per share."""
    return amount / (price_cents / 100)


def calc_payout_if_win(shares):
    """Each winning share pays $1.00 at resolution."""
    return shares * 1.00


def calc_profit_if_win(payout, amount):
    """Net profit = payout minus original investment."""
    return payout - amount


def calc_return_pct(profit, amount):
    """Return percentage on investment."""
    return (profit / amount) * 100


def calc_sell_value(shares, current_price_cents):
    """Current market value if you sell now."""
    return shares * (current_price_cents / 100)


def calc_unrealised_pnl(sell_value, amount):
    """Unrealised profit or loss vs entry cost."""
    return sell_value - amount


def calc_breakeven_price(entry_price_cents):
    """
    Price must reach $1.00 at resolution to break even.
    Entry price IS the break-even — you need the market to resolve YES.
    But for selling early, break-even sell price = entry price.
    """
    return entry_price_cents


def calc_kelly(your_probability, price_cents, bankroll):
    """Half-Kelly optimal bet size."""
    p = your_probability
    q = 1 - p
    b = (100 / price_cents) - 1      # Net odds
    if b <= 0:
        return 0
    kelly     = (b * p - q) / b
    kelly     = max(0, kelly)
    half_kelly = kelly * 0.5
    return min(bankroll * half_kelly, bankroll * 0.20)  # Cap at 20%


def india_tax(profit):
    """India flat 30% crypto tax on profit."""
    return profit * 0.30


# Display
def print_analysis(amount, entry_price, current_price=None, your_prob=None, bankroll=None):
    """Full trade analysis printout."""

    shares       = calc_shares(amount, entry_price)
    payout       = calc_payout_if_win(shares)
    profit       = calc_profit_if_win(payout, amount)
    ret_pct      = calc_return_pct(profit, amount)

    print(f"\n{Fore.CYAN}{'═'*50}")
    print(f"  POLYMARKET PROFIT CALCULATOR")
    print(f"{'═'*50}{Style.RESET_ALL}")

    # Entry summary
    print(f"\n{Fore.WHITE}ENTRY{Style.RESET_ALL}")
    print(f"  Amount invested : ${amount:.2f}")
    print(f"  Entry price     : {entry_price:.1f}¢  ({entry_price:.1f}% implied prob)")
    print(f"  Shares bought   : {shares:.4f}")

    # Resolution outcome
    print(f"\n{Fore.WHITE}IF MARKET RESOLVES IN YOUR FAVOUR{Style.RESET_ALL}")
    print(f"  Payout          : ${payout:.2f}")
    win_color = Fore.GREEN if profit > 0 else Fore.RED
    print(win_color + f"  Profit          : ${profit:.2f}")
    print(win_color + f"  Return          : {ret_pct:.1f}%{Style.RESET_ALL}")

    # India tax
    tax = india_tax(profit)
    after_tax = profit - tax
    print(f"\n{Fore.WHITE}INDIA TAX (30% flat){Style.RESET_ALL}")
    print(f"  Tax owed        : ${tax:.2f}")
    print(f"  Profit after tax: ${after_tax:.2f}")

    # Current market value (if current price provided)
    if current_price is not None:
        sell_val = calc_sell_value(shares, current_price)
        unreal   = calc_unrealised_pnl(sell_val, amount)
        unreal_pct = calc_return_pct(unreal, amount)

        print(f"\n{Fore.WHITE}SELL NOW (at {current_price:.1f}¢){Style.RESET_ALL}")
        print(f"  Sell value      : ${sell_val:.2f}")
        pnl_color = Fore.GREEN if unreal >= 0 else Fore.RED
        print(pnl_color + f"  Unrealised P&L  : ${unreal:+.2f}  ({unreal_pct:+.1f}%){Style.RESET_ALL}")

        # 100% profit trigger
        if unreal_pct >= 100:
            print(Fore.GREEN + f"\n  ✅ SELL SIGNAL: {unreal_pct:.0f}% profit — take it now" + Style.RESET_ALL)
        elif unreal_pct >= 50:
            print(Fore.YELLOW + f"\n  ⚠  Approaching 100% — monitor closely" + Style.RESET_ALL)
        elif unreal < 0:
            loss_pct = abs(unreal_pct)
            print(Fore.RED + f"\n  ⚠  Position down {loss_pct:.0f}% — review your thesis" + Style.RESET_ALL)

    # Kelly sizing (if probability and bankroll provided)
    if your_prob is not None and bankroll is not None:
        kelly_bet = calc_kelly(your_prob / 100, entry_price, bankroll)
        edge      = (your_prob / 100) - (entry_price / 100)

        print(f"\n{Fore.WHITE}SIZING (Kelly){Style.RESET_ALL}")
        print(f"  Your probability: {your_prob:.1f}%")
        print(f"  Market price    : {entry_price:.1f}%")
        edge_color = Fore.GREEN if edge > 0.10 else (Fore.YELLOW if edge > 0 else Fore.RED)
        print(edge_color + f"  Edge            : {edge*100:+.1f}%{Style.RESET_ALL}")
        print(f"  Bankroll        : ${bankroll:.2f}")
        print(f"  Half-Kelly bet  : ${kelly_bet:.2f}")

    print(f"\n{Fore.CYAN}{DIVIDER}{Style.RESET_ALL}\n")



# Multi-scenario table

def print_scenario_table(amount, entry_price):
    """Show profit/loss across different exit prices."""
    shares = calc_shares(amount, entry_price)

    print(f"\n{Fore.CYAN}SCENARIO TABLE — ${amount} at {entry_price}¢{Style.RESET_ALL}")
    print(f"{'Exit Price':>12} {'Sell Value':>12} {'P&L':>10} {'Return':>10}")
    print(DIVIDER)

    prices = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 99]
    # Add resolution payout row
    for p in prices:
        sell_val  = calc_sell_value(shares, p)
        pnl       = sell_val - amount
        ret       = calc_return_pct(pnl, amount)
        color     = Fore.GREEN if pnl >= 0 else Fore.RED
        marker    = " ← entry" if p == entry_price else ""
        print(color + f"{p:>11}¢ ${sell_val:>10.2f} ${pnl:>+9.2f} {ret:>+9.1f}%{marker}" + Style.RESET_ALL)

    # Resolution row
    payout = calc_payout_if_win(shares)
    profit = payout - amount
    ret    = calc_return_pct(profit, amount)
    print(Fore.GREEN + f"{'RESOLVE YES':>12} ${payout:>10.2f} ${profit:>+9.2f} {ret:>+9.1f}%" + Style.RESET_ALL)
    print(Fore.RED   + f"{'RESOLVE NO':>12} ${'0.00':>10} ${-amount:>+9.2f} {-100:>+9.1f}%" + Style.RESET_ALL)
    print()


# Batch mode

def batch_mode():
    """Analyse multiple trades at once."""
    print(f"\n{Fore.CYAN}BATCH TRADE ANALYSER{Style.RESET_ALL}")
    print("Enter trades one by one. Leave amount blank to finish.\n")

    trades = []
    total_invested = 0
    total_payout   = 0

    i = 1
    while True:
        print(f"Trade #{i}")
        try:
            amt = input("  Amount ($): ").strip()
            if not amt:
                break
            amount = float(amt)
            price  = float(input("  Entry price (¢): "))
            label  = input("  Label (optional): ").strip() or f"Trade #{i}"

            shares  = calc_shares(amount, price)
            payout  = calc_payout_if_win(shares)
            profit  = calc_profit_if_win(payout, amount)
            ret_pct = calc_return_pct(profit, amount)

            trades.append({
                "label":   label,
                "amount":  amount,
                "price":   price,
                "shares":  shares,
                "payout":  payout,
                "profit":  profit,
                "ret_pct": ret_pct,
            })

            total_invested += amount
            total_payout   += payout
            i += 1
            print()

        except ValueError:
            print(Fore.RED + "Invalid input. Try again." + Style.RESET_ALL)

    if not trades:
        return

    # Summary table
    print(f"\n{Fore.CYAN}{'═'*65}")
    print(f"  BATCH SUMMARY — {len(trades)} trades")
    print(f"{'═'*65}{Style.RESET_ALL}")
    print(f"{'Label':<20} {'Amount':>8} {'Price':>7} {'Payout':>9} {'Profit':>9} {'Return':>8}")
    print("─" * 65)

    for t in trades:
        color = Fore.GREEN if t["profit"] > 0 else Fore.RED
        print(color + f"{t['label']:<20} ${t['amount']:>7.2f} {t['price']:>6.1f}¢ "
              f"${t['payout']:>8.2f} ${t['profit']:>+8.2f} {t['ret_pct']:>+7.1f}%" + Style.RESET_ALL)

    print("─" * 65)
    total_profit = total_payout - total_invested
    total_ret    = calc_return_pct(total_profit, total_invested)
    total_tax    = india_tax(max(0, total_profit))
    color        = Fore.GREEN if total_profit > 0 else Fore.RED

    print(f"{'TOTAL':<20} ${total_invested:>7.2f} {'':>7} ${total_payout:>8.2f} "
          + color + f"${total_profit:>+8.2f} {total_ret:>+7.1f}%" + Style.RESET_ALL)
    print(f"\n  India tax (30%): ${total_tax:.2f}")
    print(f"  Net after tax  : ${total_profit - total_tax:.2f}\n")



# Interactive mode

def interactive_mode():
    """Guided interactive calculator."""
    print(f"\n{Fore.CYAN}POLYMARKET PROFIT CALCULATOR{Style.RESET_ALL}")
    print("Press Enter to skip optional fields.\n")

    try:
        amount       = float(input("Amount invested ($): "))
        entry_price  = float(input("Entry price (¢): "))

        current_raw  = input("Current price (¢) [optional]: ").strip()
        current_price = float(current_raw) if current_raw else None

        prob_raw     = input("Your probability estimate (%) [optional]: ").strip()
        your_prob    = float(prob_raw) if prob_raw else None

        bankroll_raw = input("Your total balance ($) [optional]: ").strip()
        bankroll     = float(bankroll_raw) if bankroll_raw else None

        print_analysis(amount, entry_price, current_price, your_prob, bankroll)
        print_scenario_table(amount, entry_price)

    except ValueError:
        print(Fore.RED + "Invalid input." + Style.RESET_ALL)
    except KeyboardInterrupt:
        print("\nCancelled.")


# CLI

def main():
    parser = argparse.ArgumentParser(
        description="Polymarket Profit Calculator",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("--amount",   type=float, help="Amount invested in USD")
    parser.add_argument("--price",    type=float, help="Entry price in cents (e.g. 25 for 25¢)")
    parser.add_argument("--current",  type=float, help="Current market price in cents")
    parser.add_argument("--prob",     type=float, help="Your probability estimate (0-100)")
    parser.add_argument("--bankroll", type=float, help="Your total balance in USD")
    parser.add_argument("--batch",    action="store_true", help="Analyse multiple trades")
    parser.add_argument("--table",    action="store_true", help="Show scenario table only")

    args = parser.parse_args()

    if args.batch:
        batch_mode()
    elif args.amount and args.price:
        print_analysis(args.amount, args.price, args.current, args.prob, args.bankroll)
        if args.table:
            print_scenario_table(args.amount, args.price)
    else:
        interactive_mode()


if __name__ == "__main__":
    main()