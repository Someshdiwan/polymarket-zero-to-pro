# 🧮 Profit & Loss Calculations

> Understanding the mathematics behind prediction markets is fundamental to becoming a profitable trader. Master these formulas before placing a single dollar.

---

## The 4 Core Formulas

```
1. Shares     = Amount Invested ÷ Share Price
2. Payout     = Shares × $1
3. Profit     = Payout - Amount Invested
4. Return %   = (Profit ÷ Amount Invested) × 100
```

---

## Part 1 : Shares Formula

### Formula
```
Shares = Amount Invested ÷ Share Price
```

### Examples

**Example A : Buying NO at 2¢**
```
Amount    = $10
Price     = 2¢ = $0.02

Shares    = $10 ÷ $0.02
Shares    = 500 ✅
```

**Example B : Buying YES at 50¢**
```
Amount    = $10
Price     = 50¢ = $0.50

Shares    = $10 ÷ $0.50
Shares    = 20 ✅
```

**Example C : Buying NO at 8.9¢**
```
Amount    = $1
Price     = 8.9¢ = $0.089

Shares    = $1 ÷ $0.089
Shares    = 11.2 ✅
```

> 💡 Lower price = more shares = bigger potential payout

---

## Part 2 : Payout Formula

### Formula
```
Payout = Shares × $1
```

> Every winning share is worth exactly $1 at resolution

### Examples

```
500 shares → 500 × $1 = $500 payout
20 shares  → 20  × $1 = $20 payout
11.2 shares → 11.2 × $1 = $11.20 payout
```

---

## Part 3 : Profit Formula

### Formula
```
Profit = Payout - Amount Invested
```

### Examples

**Example A**
```
Payout   = $500
Invested = $10

Profit   = $500 - $10 = $490 ✅
```

**Example B**
```
Payout   = $20
Invested = $10

Profit   = $20 - $10 = $10 ✅
```

**Example C : Loss**
```
Payout   = $0 (you lost)
Invested = $10

Profit   = $0 - $10 = -$10 ❌
```

---

## Part 4 : Return % Formula

### Formula
```
Return % = (Profit ÷ Amount Invested) × 100
```

### Examples

```
Profit $490, Invested $10
Return = ($490 ÷ $10) × 100 = 4900% 🚀

Profit $10, Invested $10
Return = ($10 ÷ $10) × 100 = 100% ✅

Loss -$7, Invested $10
Return = (-$7 ÷ $10) × 100 = -70% ❌
```

---

## Part 5 : Sell Early Formula

### When you sell before resolution
```
Sell Value = Shares × Current Price
Profit     = Sell Value - Amount Invested
Return %   = (Profit ÷ Amount Invested) × 100
```

### Real Example
```
You bought NO at 2¢ with $10
Shares = 500

1 hour later NO price = 10¢

Sell Value = 500 × $0.10 = $50
Profit     = $50 - $10   = $40
Return     = ($40 ÷ $10) × 100 = 400% ✅
```

---

## Part 6 : Complete Scenarios Table

### Setup: $10 invested, bought NO at 2¢ = 500 shares

#### If you SELL EARLY at different prices

| NO Price | Sell Value | Profit/Loss | Return % |
|---|---|---|---|
| 0.5¢ | $2.50 | -$7.50 | -75% ❌ |
| 1¢ | $5.00 | -$5.00 | -50% ❌ |
| 2¢ | $10.00 | $0.00 | 0% |
| 5¢ | $25.00 | +$15.00 | +150% ✅ |
| 10¢ | $50.00 | +$40.00 | +400% ✅ |
| 20¢ | $100.00 | +$90.00 | +900% ✅ |
| 50¢ | $250.00 | +$240.00 | +2400% ✅ |
| 100¢ | $500.00 | +$490.00 | +4900% ✅ |

#### If you HOLD to resolution

| Outcome | Payout | Profit | Return % |
|---|---|---|---|
| NO wins ✅ | $500 | +$490 | +4900% |
| YES wins ❌ | $0 | -$10 | -100% |

---

## Part 7 : Multiple Bets Calculation

### Total Portfolio Profit
```
Total Profit = Sum of all individual profits

Bet 1: Invested $2  → Won $10  → Profit = +$8
Bet 2: Invested $2  → Lost     → Profit = -$2
Bet 3: Invested $1  → Won $5   → Profit = +$4
Bet 4: Invested $5  → Lost     → Profit = -$5
─────────────────────────────────────────────
Total Invested = $10
Total Returned = $15
Net Profit     = +$5
Overall Return = ($5 ÷ $10) × 100 = +50% ✅
```

---

## Part 8 : Expected Value (EV)

### What is EV?
```
EV tells you if a bet is worth taking
Positive EV = good bet over time
Negative EV = bad bet over time
```

### Formula
```
EV = (Win Probability × Profit) - (Lose Probability × Loss)
```

### Example A : Good Bet ✅
```
Market price = 10¢ (market says 10% chance)
You think    = 30% chance (you have edge)

Win prob  = 0.30
Lose prob = 0.70
Profit if win  = $9 (on $1 bet)
Loss if lose   = $1

EV = (0.30 × $9) - (0.70 × $1)
EV = $2.70 - $0.70
EV = +$2.00 ✅ (positive = good bet)
```

### Example B : Bad Bet ❌
```
Market price = 10¢ (market says 10% chance)
You think    = 10% chance (no edge)

EV = (0.10 × $9) - (0.90 × $1)
EV = $0.90 - $0.90
EV = $0.00 ❌ (zero = coin flip, not worth it)
```

### Example C : Terrible Bet ❌
```
BTC 5 min market
Price = 50¢ (50/50 coin flip)
You have no edge

EV = (0.50 × $1) - (0.50 × $1)
EV = $0.50 - $0.50
EV = $0.00

Plus platform fees = slightly negative EV
= Guaranteed loss over many bets ❌
```

---

## Part 9 : Bankroll Management Math

### The 20% Rule
```
Never risk more than 20% per trade

Balance = $14
Max bet = $14 × 0.20 = $2.80 per trade
```

### Kelly Criterion (Advanced)
```
Optimal bet size formula:

f = (bp - q) ÷ b

Where:
f = fraction of balance to bet
b = net odds (payout ÷ bet - 1)
p = your estimated win probability
q = lose probability (1 - p)

Example:
Price = 10¢, you think 30% chance
b = ($10 - $1) ÷ $1 = 9
p = 0.30
q = 0.70

f = (9 × 0.30 - 0.70) ÷ 9
f = (2.70 - 0.70) ÷ 9
f = 2.00 ÷ 9
f = 0.22 = 22% of balance ✅
```

> 💡 Kelly says bet 22% here  close to our 20% rule

---

## Part 10 Real Day 1 Numbers

### Somesh's First Day on Polymarket

```
Starting balance  = $19.25
─────────────────────────────────
Bet 1: BTC 5min UP  $1.00 → Lost    = -$1.00
Bet 2: BTC 5min UP  $1.00 → Lost    = -$1.00
Bet 3: BTC 5min DOWN $2.00 → Lost   = -$2.00
Bet 4: BTC UP $1.00 → Won +462%!    = +$4.62
       (but didn't sell in time)    = -$1.00
Bet 5: Iran NO $0.50 → Lost         = -$0.50
─────────────────────────────────
Total lost        = ~$5.50
Ending balance    = $13.75
Return            = -28.5%

Lessons learned   = Priceless 😄
```

### What Should Have Happened
```
If sold Bet 4 at 462% profit:
Profit = +$4.62
Net loss = -$0.88 instead of -$5.50

One good sell = 6x better outcome
```

---

## Part 11 : Quick Calculator

### Use This to Calculate Any Bet

```
Step 1: Find share count
        Shares = Amount ÷ (Price ÷ 100)

Step 2: Find max payout
        Payout = Shares × 1

Step 3: Find profit if win
        Profit = Payout - Amount

Step 4: Find current sell value
        Sell = Shares × (Current Price ÷ 100)

Step 5: Find current profit
        Current Profit = Sell - Amount

Step 6: Find return %
        Return = (Current Profit ÷ Amount) × 100
```

### Quick Reference Card

```
╔════════════════════════════════════════════╗
║  Amount $1 invested at different prices    ║
╠══════════╦══════════╦══════════╦═══════════╣
║  Price   ║  Shares  ║ Max Win  ║  Profit   ║
╠══════════╬══════════╬══════════╬═══════════╣
║   1¢     ║   100    ║  $100    ║   $99     ║
║   2¢     ║    50    ║   $50    ║   $49     ║
║   5¢     ║    20    ║   $20    ║   $19     ║
║  10¢     ║    10    ║   $10    ║    $9     ║
║  20¢     ║     5    ║    $5    ║    $4     ║
║  50¢     ║     2    ║    $2    ║    $1     ║
║  99¢     ║   1.01   ║  $1.01   ║  $0.01    ║
╚══════════╩══════════╩══════════╩═══════════╝
```

---

## Next Steps

| I want to... | Go to... |
|---|---|
| Understand auto resolve | [05-auto-resolve.md](05-auto-resolve.md) |
| Learn trading strategy | [07-quant-mindset.md](07-quant-mindset.md) |
| Use profit calculator script | [scripts/profit_calculator.py](../scripts/profit_calculator.py) |
| Avoid mistakes | [10-mistakes-and-scams.md](10-mistakes-and-scams.md) |

---

*The math never lies but emotions make you ignore it 😄*