#!/usr/bin/env python3
"""
ev_calculator.py

Expected Value calculator for Polymarket trades.
Calculates EV, Kelly sizing, edge, and multi-scenario analysis.

Usage:
    python ev_calculator.py                              # Interactive
    python ev_calculator.py --prob 35 --price 20        # Quick EV
    python ev_calculator.py --compare                   # Compare multiple bets
    python ev_calculator.py --simulate 1000             # Monte Carlo simulation
"""

import argparse
import random
from colorama import Fore, Style, init
from tabulate import tabulate

init(autoreset=True)

DIVIDER = "─" * 55


# Core EV Formulas

def calc_ev(your_prob, price_cents, stake=1.0):
    """
    Expected Value of a bet.

    EV = (P_win × Profit) − (P_lose × Loss)

    Args:
        your_prob:   Your estimated win probability (0.0 - 1.0)
        price_cents: Market price in cents (0 - 100)
        stake:       Amount to bet in USD

    Returns:
        EV in USD
    """
    price         = price_cents / 100
    shares        = stake / price
    profit_if_win = shares - stake
    loss_if_lose  = stake

    return (your_prob * profit_if_win) - ((1 - your_prob) * loss_if_lose)


def calc_edge(your_prob, price_cents):
    """Edge = your probability minus market implied probability."""
    return your_prob - (price_cents / 100)


def calc_kelly(your_prob, price_cents, bankroll=100.0, fraction=0.5):
    """
    Kelly Criterion optimal bet size.

    Full Kelly: f = (bp - q) / b
    Half Kelly: f × 0.5 (recommended, lower variance)

    Args:
        your_prob:   Win probability (0.0 - 1.0)
        price_cents: Market price in cents
        bankroll:    Total balance in USD
        fraction:    Kelly fraction (0.5 = half Kelly)

    Returns:
        Recommended bet size in USD
    """
    p = your_prob
    q = 1 - p
    b = (100 / price_cents) - 1   # Net odds

    if b <= 0 or p <= 0:
        return 0.0

    kelly  = (b * p - q) / b
    kelly  = max(0.0, kelly)
    sized  = kelly * fraction * bankroll

    # Hard cap at 20% of bankroll
    return min(sized, bankroll * 0.20)


def calc_breakeven_prob(price_cents):
    """Minimum probability needed for positive EV."""
    return price_cents / 100


def calc_implied_odds(price_cents):
    """Convert price to decimal odds and return on $1."""
    price = price_cents / 100
    if price <= 0:
        return 0
    return 1 / price


def roi_at_resolution(price_cents):
    """Return on investment if market resolves YES."""
    price = price_cents / 100
    if price <= 0:
        return 0
    return ((1.0 - price) / price) * 100


# Monte Carlo Simulation

def monte_carlo(your_prob, price_cents, stake, n_trials=1000, bankroll=20.0):
    """
    Simulate N independent bets and show outcome distribution.

    Args:
        your_prob:   Win probability per bet
        price_cents: Market price per bet
        stake:       USD per bet
        n_trials:    Number of simulations
        bankroll:    Starting bankroll

    Returns:
        Dict with simulation stats
    """
    results = []

    for _ in range(n_trials):
        balance = bankroll
        for _ in range(50):  # 50 bets per simulation
            if balance < stake:
                break
            win = random.random() < your_prob
            if win:
                shares  = stake / (price_cents / 100)
                balance += shares - stake
            else:
                balance -= stake
        results.append(balance)

    final_balances = results
    profitable     = sum(1 for b in final_balances if b > bankroll)
    busted         = sum(1 for b in final_balances if b < stake)
    avg_balance    = sum(final_balances) / len(final_balances)
    median_balance = sorted(final_balances)[len(final_balances) // 2]
    best           = max(final_balances)
    worst          = min(final_balances)

    return {
        "n_trials":        n_trials,
        "starting":        bankroll,
        "avg_balance":     avg_balance,
        "median_balance":  median_balance,
        "profitable_pct":  profitable / n_trials * 100,
        "busted_pct":      busted / n_trials * 100,
        "best":            best,
        "worst":           worst,
    }

# Display Functions

def print_ev_analysis(your_prob_pct, price_cents, stake, bankroll=None):
    """Full EV analysis display."""
    your_prob  = your_prob_pct / 100
    ev         = calc_ev(your_prob, price_cents, stake)
    edge       = calc_edge(your_prob, price_cents)
    breakeven  = calc_breakeven_prob(price_cents)
    roi        = roi_at_resolution(price_cents)
    imp_odds   = calc_implied_odds(price_cents)

    print(f"\n{Fore.CYAN}{'═'*55}")
    print(f"  EXPECTED VALUE ANALYSIS")
    print(f"{'═'*55}{Style.RESET_ALL}")

    # Input summary
    print(f"\n{Fore.WHITE}INPUTS{Style.RESET_ALL}")
    print(f"  Market price    : {price_cents:.1f}¢  ({price_cents:.1f}% implied)")
    print(f"  Your estimate   : {your_prob_pct:.1f}%")
    print(f"  Stake           : ${stake:.2f}")

    # Edge
    print(f"\n{Fore.WHITE}EDGE{Style.RESET_ALL}")
    edge_color = Fore.GREEN if edge > 0.10 else (Fore.YELLOW if edge > 0 else Fore.RED)
    print(edge_color + f"  Edge            : {edge*100:+.1f}%" + Style.RESET_ALL)

    verdict = "✅ STRONG BET" if edge > 0.15 else \
              "✅ GOOD BET"   if edge > 0.10 else \
              "⚠  MARGINAL"   if edge > 0.05 else \
              "⚠  WEAK"       if edge > 0    else \
              "❌ NO EDGE — SKIP"
    print(f"  Verdict         : {verdict}")
    print(f"  Break-even prob : {breakeven*100:.1f}%")

    # Expected value
    print(f"\n{Fore.WHITE}EXPECTED VALUE{Style.RESET_ALL}")
    ev_color = Fore.GREEN if ev > 0 else Fore.RED
    print(ev_color + f"  EV (${stake:.0f} bet)    : ${ev:+.4f}" + Style.RESET_ALL)

    ev_per_dollar = ev / stake
    print(ev_color + f"  EV per $1       : ${ev_per_dollar:+.4f}" + Style.RESET_ALL)

    # Over 100 bets
    ev_100 = ev * 100
    print(f"  EV over 100 bets: ${ev_100:+.2f}  (at ${stake:.0f}/bet)")

    # Payout mechanics
    print(f"\n{Fore.WHITE}PAYOUT IF WIN{Style.RESET_ALL}")
    shares      = stake / (price_cents / 100)
    profit_win  = shares - stake
    print(f"  Shares bought   : {shares:.4f}")
    print(f"  Win payout      : ${shares:.4f}")
    print(f"  Win profit      : ${profit_win:.4f}")
    print(f"  ROI if win      : {roi:.1f}%")
    print(f"  Decimal odds    : {imp_odds:.2f}x")

    # Kelly sizing
    if bankroll:
        kelly_full = calc_kelly(your_prob, price_cents, bankroll, fraction=1.0)
        kelly_half = calc_kelly(your_prob, price_cents, bankroll, fraction=0.5)

        print(f"\n{Fore.WHITE}KELLY SIZING  (bankroll: ${bankroll:.2f}){Style.RESET_ALL}")
        print(f"  Full Kelly      : ${kelly_full:.2f}")
        print(f"  Half Kelly      : ${kelly_half:.2f}  ← recommended")
        print(f"  20% max cap     : ${bankroll*0.20:.2f}")
        rec = min(kelly_half, bankroll * 0.20)
        print(Fore.CYAN + f"  Recommended bet : ${rec:.2f}" + Style.RESET_ALL)

    print(f"\n{Fore.CYAN}{DIVIDER}{Style.RESET_ALL}\n")


def print_ev_table(price_cents, stake=2.0):
    """Show EV across all probability estimates."""
    print(f"\n{Fore.CYAN}EV TABLE — ${stake:.0f} bet at {price_cents:.0f}¢ market{Style.RESET_ALL}")
    print(f"{'Your Prob':>11} {'Edge':>8} {'EV':>10} {'Verdict':>15}")
    print(DIVIDER)

    probs = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
    for prob_pct in probs:
        prob  = prob_pct / 100
        ev    = calc_ev(prob, price_cents, stake)
        edge  = calc_edge(prob, price_cents)

        if edge > 0.15:
            color   = Fore.GREEN
            verdict = "STRONG BET"
        elif edge > 0.10:
            color   = Fore.GREEN
            verdict = "GOOD BET"
        elif edge > 0.05:
            color   = Fore.YELLOW
            verdict = "MARGINAL"
        elif edge > 0:
            color   = Fore.YELLOW
            verdict = "WEAK"
        else:
            color   = Fore.RED
            verdict = "SKIP"

        marker = " ← market" if prob_pct == price_cents else ""
        print(color + f"{prob_pct:>10}%  {edge*100:>+7.1f}%  ${ev:>+8.4f}  {verdict:>12}{marker}" + Style.RESET_ALL)
    print()


def print_comparison(bets):
    """Compare multiple bets side by side."""
    print(f"\n{Fore.CYAN}BET COMPARISON{Style.RESET_ALL}\n")

    table = []
    for b in bets:
        prob  = b["prob"] / 100
        ev    = calc_ev(prob, b["price"], b["stake"])
        edge  = calc_edge(prob, b["price"])
        roi   = roi_at_resolution(b["price"])
        color = Fore.GREEN if ev > 0 else Fore.RED

        table.append([
            b["label"],
            f"{b['prob']:.0f}%",
            f"{b['price']:.0f}¢",
            f"${b['stake']:.2f}",
            color + f"{edge*100:+.1f}%" + Style.RESET_ALL,
            color + f"${ev:+.4f}" + Style.RESET_ALL,
            f"{roi:.0f}%",
        ])

    headers = ["Label", "Your Prob", "Price", "Stake", "Edge", "EV", "ROI if Win"]
    print(tabulate(table, headers=headers, tablefmt="rounded_outline"))

    # Rank by EV
    ranked = sorted(bets, key=lambda b: calc_ev(b["prob"]/100, b["price"], b["stake"]), reverse=True)
    print(f"\n{Fore.GREEN}Best EV: {ranked[0]['label']}{Style.RESET_ALL}\n")


def print_simulation(results, your_prob, price_cents, stake):
    """Display Monte Carlo simulation results."""
    print(f"\n{Fore.CYAN}MONTE CARLO SIMULATION{Style.RESET_ALL}")
    print(f"  {results['n_trials']:,} simulations × 50 bets each")
    print(f"  ${stake:.2f}/bet at {price_cents:.0f}¢  |  Your prob: {your_prob:.0f}%\n")

    print(f"  Starting balance  : ${results['starting']:.2f}")
    avg_color = Fore.GREEN if results['avg_balance'] > results['starting'] else Fore.RED
    print(avg_color + f"  Avg ending balance: ${results['avg_balance']:.2f}" + Style.RESET_ALL)
    print(f"  Median balance    : ${results['median_balance']:.2f}")
    print(f"  Best outcome      : ${results['best']:.2f}")
    print(f"  Worst outcome     : ${results['worst']:.2f}")

    pct_color = Fore.GREEN if results['profitable_pct'] > 60 else Fore.RED
    print(pct_color + f"  % profitable      : {results['profitable_pct']:.1f}%" + Style.RESET_ALL)
    bust_color = Fore.RED if results['busted_pct'] > 10 else Fore.GREEN
    print(bust_color + f"  % busted          : {results['busted_pct']:.1f}%" + Style.RESET_ALL)
    print()


# Interactive & Compare modes

def interactive_mode():
    """Guided EV calculator."""
    print(f"\n{Fore.CYAN}EV CALCULATOR{Style.RESET_ALL}\n")

    try:
        prob_pct    = float(input("Your estimated probability (%): "))
        price_cents = float(input("Market price (¢): "))
        stake       = float(input("Stake ($) [default 2]: ") or "2")
        bankroll    = input("Your bankroll ($) [optional]: ").strip()
        bankroll    = float(bankroll) if bankroll else None

        print_ev_analysis(prob_pct, price_cents, stake, bankroll)
        print_ev_table(price_cents, stake)

    except (ValueError, KeyboardInterrupt):
        print("\nCancelled.")


def compare_mode():
    """Compare multiple bets."""
    print(f"\n{Fore.CYAN}COMPARE BETS{Style.RESET_ALL}")
    print("Enter bets one by one. Leave label blank to finish.\n")

    bets = []
    i    = 1

    while True:
        try:
            label = input(f"Bet #{i} label (or Enter to finish): ").strip()
            if not label:
                break
            prob  = float(input(f"  Your probability (%): "))
            price = float(input(f"  Market price (¢): "))
            stake = float(input(f"  Stake ($): ") or "2")

            bets.append({"label": label, "prob": prob, "price": price, "stake": stake})
            i += 1
            print()

        except (ValueError, KeyboardInterrupt):
            break

    if bets:
        print_comparison(bets)


# CLI

def main():
    parser = argparse.ArgumentParser(
        description="Polymarket EV Calculator",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument("--prob",      type=float, help="Your estimated probability (0-100)")
    parser.add_argument("--price",     type=float, help="Market price in cents")
    parser.add_argument("--stake",     type=float, default=2.0, help="Stake in USD (default: 2)")
    parser.add_argument("--bankroll",  type=float, help="Your total balance (for Kelly sizing)")
    parser.add_argument("--table",     action="store_true", help="Show EV table across all probabilities")
    parser.add_argument("--compare",   action="store_true", help="Compare multiple bets interactively")
    parser.add_argument("--simulate",  type=int,            help="Run Monte Carlo with N simulations")

    args = parser.parse_args()

    if args.compare:
        compare_mode()

    elif args.prob and args.price:
        print_ev_analysis(args.prob, args.price, args.stake, args.bankroll)
        if args.table:
            print_ev_table(args.price, args.stake)
        if args.simulate:
            results = monte_carlo(args.prob/100, args.price, args.stake, args.simulate)
            print_simulation(results, args.prob, args.price, args.stake)

    elif args.price and args.table:
        print_ev_table(args.price, args.stake)

    else:
        interactive_mode()


if __name__ == "__main__":
    main()
