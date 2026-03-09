1. profit_calculator.py

```
python profit_calculator.py --amount     10 --price 25 --current 60
python profit_calculator.py --batch      # analyse multiple trades
python profit_calculator.py --table      # scenario table across all exit prices
```

Shows shares, payout, P&L, India 30% tax, Kelly sizing, sell signal at 100%+.

1. market_scanner.py

```
python market_scanner.py                                     # top markets by volume
python market_scanner.py --category crypto
python market_scanner.py --closing-soon                      # closes within 24h
python market_scanner.py --min-price 20 --max-price 80
python market_scanner.py --stats                             # category breakdown
```

Hits Polymarket public API — no key needed

1. portfolio_tracker.py

```
python portfolio_tracker.py              # dashboard
python portfolio_tracker.py --add        # log a trade
python portfolio_tracker.py --resolve    # mark WIN/LOSS
python portfolio_tracker.py --stats      # win rate, ROI, by category
python portfolio_tracker.py --export     # save to CSV
```

Stores data in ~/.polymarket_portfolio.json — persists across sessions

1. ev_calculator.py

```
python ev_calculator.py --prob 40 --price 20 --stake 2    --bankroll 14
python ev_calculator.py --table --price 20                # EV at every probability
python ev_calculator.py --compare                         # compare multiple bets
python ev_calculator.py --simulate 1000                   # Monte Carlo 1000 runs
```
