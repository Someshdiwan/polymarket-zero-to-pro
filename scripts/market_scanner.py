#!/usr/bin/env python3
"""
market_scanner.py

Scan Polymarket for active markets filtered by volume, category,
price range, and closing time. No API key required for read-only access.

Usage:
    python market_scanner.py                         # Show top markets
    python market_scanner.py --category crypto       # Filter by category
    python market_scanner.py --min-price 20 --max-price 80
    python market_scanner.py --min-volume 100000
    python market_scanner.py --closing-soon          # Closing within 24h
    python market_scanner.py --watchlist             # Save/view watchlist
"""

import json
import os
import sys
import argparse
import requests
from datetime import datetime, timezone
from colorama import Fore, Style, init
from tabulate import tabulate

init(autoreset=True)

# Polymarket public API (no key required)
GAMMA_API   = "https://gamma-api.polymarket.com"
MARKETS_URL = f"{GAMMA_API}/markets"
WATCHLIST_FILE = os.path.expanduser("~/.polymarket_watchlist.json")

DIVIDER = "─" * 70

# API Fetcher

def fetch_markets(limit=100, offset=0):
    """
    Fetch active markets from Polymarket Gamma API.
    No authentication required.
    """
    try:
        params = {
            "active":   "true",
            "closed":   "false",
            "limit":    limit,
            "offset":   offset,
            "order":    "volume",
            "ascending":"false",
        }

        response = requests.get(MARKETS_URL, params=params, timeout=15)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.ConnectionError:
        print(Fore.RED + "❌ Connection failed. Check your internet connection." + Style.RESET_ALL)
        sys.exit(1)
    except requests.exceptions.Timeout:
        print(Fore.RED + "❌ Request timed out." + Style.RESET_ALL)
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        print(Fore.RED + f"❌ API error: {e}" + Style.RESET_ALL)
        sys.exit(1)
    except Exception as e:
        print(Fore.RED + f"❌ Unexpected error: {e}" + Style.RESET_ALL)
        sys.exit(1)


# Filters

def apply_filters(markets, args):
    """Apply all filters and return matching markets."""
    filtered = []
    now = datetime.now(timezone.utc)

    for m in markets:
        volume    = float(m.get("volume", 0) or 0)
        yes_price = _get_yes_price(m)
        category  = (m.get("category") or "").lower()
        end_date  = m.get("endDate") or m.get("endDateIso")

        # Volume filter
        if volume < args.min_volume:
            continue

        # Category filter
        if args.category and args.category.lower() not in category:
            continue

        # Price range filter
        if yes_price is not None:
            if args.min_price and yes_price < args.min_price:
                continue
            if args.max_price and yes_price > args.max_price:
                continue

        # Closing soon filter (within 24 hours)
        if args.closing_soon and end_date:
            try:
                close_dt = datetime.fromisoformat(end_date.replace("Z", "+00:00"))
                hours_left = (close_dt - now).total_seconds() / 3600
                if hours_left > 24 or hours_left < 0:
                    continue
            except Exception:
                continue

        # Skip near-resolved (outside 5-95 range) unless overridden
        if not args.all_prices and yes_price is not None:
            if yes_price > 95 or yes_price < 5:
                continue

        filtered.append(m)

    return filtered


def _get_yes_price(market):
    """Extract YES price as float 0-100."""
    try:
        prices = market.get("outcomePrices") or []
        if isinstance(prices, str):
            prices = json.loads(prices)
        if prices:
            return float(prices[0]) * 100
    except Exception:
        pass
    return None


def _get_hours_left(market):
    """Return hours until market closes."""
    end_date = market.get("endDate") or market.get("endDateIso")
    if not end_date:
        return None
    try:
        close_dt   = datetime.fromisoformat(end_date.replace("Z", "+00:00"))
        now        = datetime.now(timezone.utc)
        hours_left = (close_dt - now).total_seconds() / 3600
        return max(0, hours_left)
    except Exception:
        return None


def _format_hours(hours):
    """Format hours remaining into readable string."""
    if hours is None:
        return "—"
    if hours < 1:
        return Fore.RED + f"{hours*60:.0f}m" + Style.RESET_ALL
    if hours < 24:
        return Fore.YELLOW + f"{hours:.1f}h" + Style.RESET_ALL
    days = hours / 24
    return f"{days:.1f}d"


def _format_volume(volume):
    """Format volume with K/M suffix."""
    if volume >= 1_000_000:
        return f"${volume/1_000_000:.1f}M"
    if volume >= 1_000:
        return f"${volume/1_000:.0f}K"
    return f"${volume:.0f}"


def _price_color(price):
    """Colour code YES price by probability."""
    if price is None:
        return "N/A"
    if price >= 70:
        return Fore.GREEN + f"{price:.0f}¢" + Style.RESET_ALL
    if price <= 30:
        return Fore.RED + f"{price:.0f}¢" + Style.RESET_ALL
    return Fore.YELLOW + f"{price:.0f}¢" + Style.RESET_ALL

# Display

def display_markets(markets, title="ACTIVE MARKETS"):
    """Display markets in a formatted table."""
    if not markets:
        print(Fore.YELLOW + "\nNo markets found matching your filters." + Style.RESET_ALL)
        return

    print(f"\n{Fore.CYAN}{'═'*70}")
    print(f"  {title} — {len(markets)} results")
    print(f"{'═'*70}{Style.RESET_ALL}\n")

    table_data = []
    for i, m in enumerate(markets, 1):
        yes_price  = _get_yes_price(m)
        no_price   = round(100 - yes_price, 1) if yes_price is not None else None
        volume     = float(m.get("volume", 0) or 0)
        hours_left = _get_hours_left(m)
        question   = m.get("question", "N/A")
        category   = m.get("category") or "—"

        table_data.append([
            i,
            question[:55] + ("..." if len(question) > 55 else ""),
            _price_color(yes_price),
            _price_color(no_price),
            _format_volume(volume),
            _format_hours(hours_left),
            category[:12],
        ])

    headers = ["#", "Market", "YES", "NO", "Volume", "Closes", "Category"]
    print(tabulate(table_data, headers=headers, tablefmt="rounded_outline"))
    print(f"\nShowing {len(markets)} markets  |  Tip: use --category, --min-price, --max-price to filter\n")


def display_market_detail(market):
    """Show full detail for a single market."""
    yes_price  = _get_yes_price(market)
    no_price   = round(100 - yes_price, 1) if yes_price is not None else None
    volume     = float(market.get("volume", 0) or 0)
    hours_left = _get_hours_left(market)

    print(f"\n{Fore.CYAN}{DIVIDER}{Style.RESET_ALL}")
    print(f"  {market.get('question', 'N/A')}")
    print(f"{Fore.CYAN}{DIVIDER}{Style.RESET_ALL}")
    print(f"  Category     : {market.get('category', '—')}")
    print(f"  YES Price    : {_price_color(yes_price)}")
    print(f"  NO Price     : {_price_color(no_price)}")
    print(f"  Volume       : {_format_volume(volume)}")
    print(f"  Closes in    : {_format_hours(hours_left)}")
    print(f"  Market ID    : {market.get('conditionId') or market.get('id', '—')}")
    print(f"  Description  : {(market.get('description') or '—')[:200]}")
    print(f"{Fore.CYAN}{DIVIDER}{Style.RESET_ALL}\n")


# Watchlist
def load_watchlist():
    """Load saved watchlist from disk."""
    if not os.path.exists(WATCHLIST_FILE):
        return []
    with open(WATCHLIST_FILE, "r") as f:
        return json.load(f)


def save_watchlist(watchlist):
    """Save watchlist to disk."""
    with open(WATCHLIST_FILE, "w") as f:
        json.dump(watchlist, f, indent=2)


def add_to_watchlist(market):
    """Add a market to watchlist."""
    watchlist  = load_watchlist()
    market_id  = market.get("conditionId") or market.get("id")

    if any(w["id"] == market_id for w in watchlist):
        print(Fore.YELLOW + "Already in watchlist." + Style.RESET_ALL)
        return

    watchlist.append({
        "id":       market_id,
        "question": market.get("question", ""),
        "added":    datetime.now().isoformat(),
    })
    save_watchlist(watchlist)
    print(Fore.GREEN + f"✅ Added to watchlist: {market.get('question', '')[:50]}" + Style.RESET_ALL)


def show_watchlist():
    """Display saved watchlist with live prices."""
    watchlist = load_watchlist()

    if not watchlist:
        print(Fore.YELLOW + "Watchlist is empty. Use --add-watch after scanning." + Style.RESET_ALL)
        return

    print(f"\n{Fore.CYAN}WATCHLIST — {len(watchlist)} markets{Style.RESET_ALL}\n")

    for i, item in enumerate(watchlist, 1):
        print(f"  {i}. {item['question'][:65]}")
        print(f"     ID: {item['id']}  |  Added: {item['added'][:10]}\n")


# Category Stats

def show_category_stats(markets):
    """Show breakdown of markets by category."""
    from collections import Counter

    categories = Counter()
    volumes    = {}

    for m in markets:
        cat    = m.get("category") or "Unknown"
        vol    = float(m.get("volume", 0) or 0)
        categories[cat] += 1
        volumes[cat]     = volumes.get(cat, 0) + vol

    print(f"\n{Fore.CYAN}CATEGORY BREAKDOWN{Style.RESET_ALL}\n")
    print(f"{'Category':<25} {'Markets':>8} {'Total Volume':>15}")
    print(DIVIDER[:50])

    for cat, count in categories.most_common():
        vol = volumes.get(cat, 0)
        print(f"{cat:<25} {count:>8} {_format_volume(vol):>15}")
    print()


# CLI

def main():
    parser = argparse.ArgumentParser(
        description="Polymarket Market Scanner",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument("--category",    type=str,            help="Filter by category (crypto, politics, sports...)")
    parser.add_argument("--min-volume",  type=float, default=10000, help="Minimum market volume in USD (default: 10000)")
    parser.add_argument("--max-volume",  type=float,          help="Maximum market volume in USD")
    parser.add_argument("--min-price",   type=float,          help="Minimum YES price in cents (e.g. 20)")
    parser.add_argument("--max-price",   type=float,          help="Maximum YES price in cents (e.g. 80)")
    parser.add_argument("--closing-soon",action="store_true", help="Only markets closing within 24 hours")
    parser.add_argument("--all-prices",  action="store_true", help="Include near-resolved markets (>95¢ or <5¢)")
    parser.add_argument("--limit",       type=int, default=50,help="Number of markets to fetch (default: 50)")
    parser.add_argument("--stats",       action="store_true", help="Show category breakdown stats")
    parser.add_argument("--watchlist",   action="store_true", help="Show your saved watchlist")
    parser.add_argument("--detail",      type=int,            help="Show full detail for market number N")

    args = parser.parse_args()

    # Watchlist mode
    if args.watchlist:
        show_watchlist()
        return

    print(Fore.CYAN + "\nFetching markets from Polymarket..." + Style.RESET_ALL)
    raw_markets = fetch_markets(limit=args.limit)
    filtered    = apply_filters(raw_markets, args)

    if args.stats:
        show_category_stats(filtered)
        return

    if args.detail and 1 <= args.detail <= len(filtered):
        display_market_detail(filtered[args.detail - 1])
        return

    # Build title
    title_parts = ["ACTIVE MARKETS"]
    if args.category:
        title_parts.append(args.category.upper())
    if args.closing_soon:
        title_parts.append("CLOSING SOON")

    display_markets(filtered, title=" | ".join(title_parts))


if __name__ == "__main__":
    main()