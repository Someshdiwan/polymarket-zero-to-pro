# Candlestick Strategy for BTC Prediction Markets

> Candlestick analysis applied to Polymarket's BTC Up/Down markets provides a probabilistic edge not a guarantee. Used correctly alongside trend confirmation and market context, it shifts win rate from 50% to a consistent 55-65%.

---

## Prerequisites

```
Before applying this strategy:
→ Understand how BTC Up/Down markets work
→ Have TradingView open alongside Polymarket
→ Only bet 15 min markets (never 5 min)
→ Max $2 per trade
→ Never trade last 3 minutes of any market
```

---

## Part 1 : Understanding BTC Up/Down Markets

### How the Market Works
```
Polymarket sets a "Price to Beat" at market open
You bet whether BTC will be ABOVE or BELOW
that price at market close

Price to Beat = $66,607.60
Current BTC   = $66,154.67 (below by $453)
Time left     = 5 minutes

Market pricing:
UP   = 0.2¢  (0.2% chance BTC recovers $453 in 5 min)
DOWN = 99.9¢ (99.9% chance BTC stays below)
```

### Why 15 Min Over 5 Min
```
5 min markets
→ Insufficient time for patterns to develop
→ Pure noise, no signal
→ Even correct analysis can be wrong
→ Avoid entirely

15 min markets
→ Enough time for momentum to continue
→ Patterns have higher completion rate
→ News can be factored in
→ This is where strategy applies
```

---

## Part 2 : Candlestick Basics

### Anatomy of a Candle
```
       │          ← Upper wick (high)
    ┌──┴──┐
    │     │       ← Body (open to close)
    │     │
    └──┬──┘
       │          ← Lower wick (low)

Green candle = closed HIGHER than it opened (bullish)
Red candle   = closed LOWER than it opened (bearish)

Large body   = strong conviction
Small body   = indecision
Long wick    = rejection of price level
```

---

## Part 3 : Key Patterns for BTC Markets

### Pattern 1 : Strong Momentum (Most Reliable)

**Bullish Momentum → Bet UP**
```
3 consecutive green candles
Each candle body larger than last
Little to no upper wicks
BTC price well above "Price to Beat"

Signal strength: ████████░░ 80%
```

**Bearish Momentum → Bet DOWN**
```
3 consecutive red candles
Each candle body larger than last
Little to no lower wicks
BTC price well below "Price to Beat"

Signal strength: ████████░░ 80%
```

---

### Pattern 2 : Engulfing Candle

**Bullish Engulfing → Bet UP**
```
Large red candle followed by
Even larger green candle that fully covers it

    ┌───┐
    │ R │
    │   │    ┌─────┐
    │   │    │     │
    └───┘    │  G  │
             │     │
             └─────┘

Signal strength: ███████░░░ 70%
```

**Bearish Engulfing → Bet DOWN**
```
Large green candle followed by
Even larger red candle that fully covers it

Signal strength: ███████░░░ 70%
```

---

### Pattern 3 : Price Far From Target

```
This is not a candle pattern
It is a distance filter

BTC is $400+ away from Price to Beat
with 10+ minutes remaining

Direction = whichever side BTC is currently on

If BTC = $200 BELOW target → Bet DOWN
If BTC = $300 ABOVE target → Bet UP

Logic: BTC needs massive move to cross target
Market already pricing this in
Signal strength: █████████░ 90%
```

---

### Pattern 4 : Doji (Avoid Signal)

```
Very small body, long wicks on both sides

    │
  ┌─┴─┐
  └─┬─┘
    │

Meaning: Market is indecisive
Action:  SKIP this market entirely
Do not bet when doji appears near target price
```

---

### Pattern 5 : Hammer / Rejection

**Hammer → Reversal signal**
```
Long lower wick, small body at top

  ┌───┐
  └───┘
    │
    │
    │   ← Long lower wick = buyers rejected the low

Meaning: Selling rejected, possible reversal UP
Action:  Consider UP bet if trend was down
Signal strength: ██████░░░░ 60%
```

---

## Part 4 : The Complete Strategy Framework

### Step 1 : Check Market Conditions
```
Open 15 min BTC market
Check:
→ Price to Beat vs Current Price
→ Time remaining (must be 8+ minutes)
→ Market odds (avoid if 99¢ either side)
→ Volume (higher is better)
```

### Step 2 : Open TradingView
```
Go to tradingview.com
Search: BTCUSDT
Set timeframe: 1 min or 3 min candles
Look at last 5-10 candles
```

### Step 3 : Identify Pattern
```
Strong trend?     → Follow the trend
Engulfing candle? → Follow the engulf direction
Price far away?   → Bet in current direction
Doji / choppy?    → SKIP, do not bet
```

### Step 4 : Confirm with Distance
```
Pattern says UP
BTC currently $300 above target
= Double confirmation → Bet UP ✅

Pattern says UP
BTC currently $50 below target
= Contradiction → SKIP ❌
```

### Step 5 : Check Odds
```
Market odds must be between 20¢ and 80¢
to have meaningful edge

UP at 0.2¢  = market already knows, skip
DOWN at 99¢ = no reward, skip
UP at 40¢   = opportunity, check pattern
DOWN at 35¢ = opportunity, check pattern
```

### Step 6 : Execute
```
Bet max $2
Use Market Order
Set a mental stop (if wrong immediately = lesson learned)
Never add to a losing position
```

---

## Part 5 : Win Rate Expectations

### Realistic Numbers

| Strategy Used | Win Rate | Notes |
|---|---|---|
| Random betting | 50% | Coin flip |
| Candles only | 52-55% | Marginal edge |
| Candles + distance | 55-60% | Solid edge |
| Candles + distance + news | 60-65% | Strong edge |
| Perfect conditions only | 65-70% | Selective, fewer bets |

### Why 65% is Enough to Profit
```
10 bets at $2 each = $20 risked
Win 65% = 6.5 wins × $2 = $13 profit
Lose 35% = 3.5 losses × $2 = -$7 loss
Net = +$6 on $20 risked = +30% return ✅
```

---

## Part 6 : When NOT to Use This Strategy

### Skip When
```
❌ Major news just dropped (Fed decision, war update)
❌ BTC showing choppy, sideways price action
❌ Less than 3 minutes remaining
❌ Market odds are 95¢+ either side
❌ Price is within $50 of target
❌ You just lost 2 bets in a row (emotional state)
❌ 5 min market (never trade these)
```

### News Overrides Everything
```
Candles say DOWN
Fed just announced rate cut → BTC pumping
News overrides candle pattern

Always check news before betting
Strong macro news = skip technical analysis
```

---

## Part 7 : Trade Log Template

### Track Every Trade

```
Date        | 2026-03-02
Market      | BTC Up/Down 15min 2:00-2:15 AM
Direction   | DOWN
Pattern     | 3 red candles, bearish momentum
Distance    | $453 below target
Odds        | DOWN at 58¢
Amount      | $2
Result      | WIN
Payout      | $3.45
Profit      | +$1.45
Notes       | Clean setup, strong momentum
```

### Why Track Trades?
```
Identify which patterns work best for you
Track win rate over time
Spot emotional mistakes
Build data to refine strategy
```

---

## Part 8 : Tools Setup

### TradingView Setup
```
1. Go to tradingview.com (free account)
2. Search BTCUSDT on Binance
3. Set chart to 1 min or 3 min
4. Add indicators:
   → EMA 9 (fast moving average)
   → EMA 21 (slow moving average)
   → Volume bars

EMA 9 above EMA 21 = uptrend → favor UP bets
EMA 9 below EMA 21 = downtrend → favor DOWN bets
```

### Side by Side Setup
```
Left screen  → TradingView BTC chart
Right screen → Polymarket BTC market

Watch chart
See pattern form
Quickly place bet on Polymarket
```

---

## Part 9 : Common Mistakes

### Mistake 1 : Betting 5 Min Markets
```
❌ BTC Up/Down 5 min
Pure noise, no strategy works
Expected value = negative after fees
```

### Mistake 2 : Ignoring Distance
```
❌ Strong UP pattern but BTC is $400 below target
Pattern means nothing against $400 gap
```

### Mistake 3 : Chasing After Loss
```
❌ Lost $2 → immediately bet $5 to recover
Each bet is independent
Chasing = guaranteed larger loss
```

### Mistake 4 : Trading Last 3 Minutes
```
❌ Placing bet with 2 min remaining
Insufficient time for pattern to matter
Random outcome at that point
```

### Mistake 5 : Betting Every Market
```
❌ Betting every single 15 min window
Wait for A+ setups only
Selective betting = higher win rate
```

---

## Part 10 : Quick Decision Checklist

```
Before every bet ask:

✅ Is this a 15 min market? (not 5 min)
✅ Is time remaining 8+ minutes?
✅ Are odds between 20¢ and 80¢?
✅ Is pattern clear? (not choppy)
✅ Does distance confirm direction?
✅ No major news against position?
✅ Am I betting max $2?
✅ Am I in a calm, logical state?

All 8 = Place bet
Any NO = Skip this market
```

---

## Next Steps

| I want to... | Go to... |
|---|---|
| Think like a quant trader | [07-quant-mindset.md](07-quant-mindset.md) |
| Understand profit math | [04-profit-loss-calc.md](04-profit-loss-calc.md) |
| Learn market types | [08-market-types.md](08-market-types.md) |
| Avoid common mistakes | [10-mistakes-and-scams.md](10-mistakes-and-scams.md) |

---

*An edge of 15% win rate above random is enough to build wealth. Protect it with discipline.*