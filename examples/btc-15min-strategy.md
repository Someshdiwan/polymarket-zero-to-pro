# Case Study : BTC 15-Minute Strategy

> A real walkthrough of applying the candlestick strategy to Polymarket's BTC Up/Down 15-minute markets. Includes two trade setups one executed correctly, one where discipline was broken and what each taught.

---

## Setup

```
Platform:    Polymarket BTC Up/Down
Timeframe:   15-minute markets only
Chart tool:  TradingView — BTCUSDT Binance, 1-min candles
Indicators:  EMA 9, EMA 21, Volume bars
Bet size:    $2 maximum per trade
```

---

## Part 1 : The 462% Trade That Slipped Away

### Market Context

```
Date:         Early March 2026
BTC price:    $82,340
Price to Beat: $82,800
Gap:          BTC is $460 BELOW target
Time left:    14 minutes
Market odds:  UP 4¢  |  DOWN 96¢
```

### Chart Reading

```
TradingView 1-min candles:

Candle -5:  ████ Red, medium body
Candle -4:  ██   Red, small body (momentum slowing)
Candle -3:  ██   Red, small body (same)
Candle -2:  ░    Doji — indecision
Candle -1:  ████████ Large green — reversal signal

EMA 9:  crossing UP through EMA 21
Volume: spike on last green candle ✅
```

### Decision Process

```
Pattern:     Reversal — green engulfing after 3 reds
Distance:    $460 below target (UP needs big move)
Time:        14 minutes remaining
Odds:        UP at 4¢

Conflict:    Pattern says UP possible
             Distance says UP very unlikely
             Odds say market agrees (4¢)

Decision:    Bet UP — pattern + volume spike
             Market at 4¢ = huge reward if right
             $1 bet → $25 payout if UP wins
```

### Trade Execution

```
Bet:     $1 on UP at 4¢
Shares:  $1 ÷ $0.04 = 25 shares
Payout:  25 × $1 = $25.00
```

### What Happened Next

```
Minute 1:  BTC jumps $180 → UP at 12¢ (+200%)
Minute 3:  BTC jumps $290 → UP at 28¢ (+600%)
Minute 5:  BTC jumps $380 → UP at 42¢ (+950%)
           Position value = $10.50 on $1 bet

At this point: +$9.50 profit showing (+950%)

Minute 8:  BTC stalls — UP at 35¢
Minute 10: BTC drops $150 — UP at 18¢
Minute 12: BTC drops further — UP at 8¢
Minute 14: BTC at $82,290 — still $510 below target
Minute 15: Market resolves — UP loses

Final result: -$1.00
Missed profit: $9.50 at peak
```

### The Mistake

```
At Minute 5:
  Position showing +950%
  BTC had moved $380 — massive move for 5 minutes
  Momentum clearly slowing (candles getting smaller)
  
  Correct action: SELL at 42¢ → pocket $10.50
  Actual action:  Held, watched it reverse

Why held?
  "It might reach the target"
  "I want the full $25"
  Greed overrode the exit rule

Cost of not selling: $9.50
```

### Rule Established

```
100%+ profit showing = sell immediately
No exceptions
No "it might go higher"
Lock in the win

At 950% profit: sell
At 200% profit: sell
At 100% profit: sell

The market will always have another setup tomorrow.
The profit you don't take is not real.
```

---

## Part 2 : A Clean Setup Executed Correctly

### Market Context

```
Date:         March 4, 2026
BTC price:    $83,150
Price to Beat: $82,900
Gap:          BTC is $250 ABOVE target
Time left:    12 minutes
Market odds:  UP 68¢  |  DOWN 32¢
```

### Chart Reading

```
TradingView 1-min candles:

Candle -6:  ████████ Large green
Candle -5:  ██████   Medium green
Candle -4:  █████    Medium green
Candle -3:  ██████   Medium green (consistent momentum)
Candle -2:  ████     Small green (slight slowdown)
Candle -1:  ██████   Medium green (resumed)

EMA 9:  clearly above EMA 21 ✅
Volume: consistent, no spike or drop
BTC:    $250 above target with 12 min left ✅
```

### Decision Process

```
Checklist:
✅ 15-minute market (not 5-min)
✅ 12 minutes remaining (8+ required)
✅ Odds at 68¢ (between 20¢-80¢)
✅ Pattern clear — 5 consecutive green candles
✅ Distance confirms — $250 ABOVE target
✅ EMA 9 above EMA 21 (uptrend)
✅ No major news against position
✅ Calm, logical state

All 8 = bet confirmed
Direction: UP
```

### Trade Execution

```
Bet:     $2 on UP at 68¢
Shares:  $2 ÷ $0.68 = 2.94 shares
Payout:  2.94 × $1 = $2.94
Profit:  $0.94 if wins
Return:  +47%
```

### What Happened

```
Minute 2:  BTC +$80 → UP at 74¢
Minute 5:  BTC +$140 → UP at 82¢  (+20% on position)
Minute 8:  BTC +$190 → UP at 88¢
Minute 10: BTC holds → UP at 87¢
Minute 12: Market resolves
           Final BTC: $83,360 → $460 above target
           UP wins ✅

Payout:  $2.94
Profit:  +$0.94
Return:  +47%
```

### Why This Trade Worked

```
Strong setup:
→ 5 consecutive green candles = clear momentum
→ Price already above target = market just needed to hold
→ 12 minutes = enough time for thesis to play out
→ EMA confirmation added conviction

No surprises:
→ BTC moved in expected direction from minute 1
→ No news event disrupted momentum
→ Clean resolution
```

### Compared to the First Trade

```
Trade 1 (UP at 4¢):
  Setup quality:  Marginal (fighting $460 gap)
  Result:         Loss (-$1)
  Lesson:         Distance can override pattern

Trade 2 (UP at 68¢):
  Setup quality:  Strong (pattern + distance aligned)
  Result:         Win (+$0.94)
  Lesson:         All 8 checklist points = high quality trade
```

---

## Part 3 : The 5-Minute Trap

### What Was Tried First (Before Learning)

```
Market:  BTC Up/Down — 5 minutes
Bet 1:   UP at 50¢  → Loss  (-$1)
Bet 2:   DOWN at 50¢ → Loss  (-$1)
Bet 3:   UP at 50¢  → Loss  (-$1)
Bet 4:   DOWN at 50¢ → Win   (+$1)
Bet 5:   UP at 50¢  → Loss  (-$1)

Result after 5 bets: -$3 net loss

Pattern recognition attempt: none possible
Candle reading attempt:      irrelevant at 5 min
Chart analysis:              useless — pure noise
```

### Why 5-Minute Markets Are Unbeatable

```
In 5 minutes:
→ Only 5 one-minute candles exist
→ Insufficient data for pattern recognition
→ Single news headline = random spike
→ High-frequency algorithms dominate
→ No retail edge possible

Mathematical reality:
→ 50¢ market = 50% win rate
→ Over 100 bets = break even before fees
→ With spread/fees = negative EV guaranteed

The only correct action: never open a 5-minute market
```

---

## Part 4 : Pattern Quality Grading

### Grade A Setup (Bet Confidently)

```
✅ 4+ consecutive same-direction candles
✅ Price clearly on winning side of target ($200+)
✅ EMA 9 aligned with bet direction
✅ 10+ minutes remaining
✅ Market odds 40¢ - 75¢
✅ No upcoming news event
```

### Grade B Setup (Bet with Caution)

```
✅ 2-3 same-direction candles
✅ Price moderately on winning side ($100-200)
⚠️ EMA borderline
✅ 8-10 minutes remaining
✅ Market odds 25¢ - 80¢
→ Reduce stake to $1
```

### Grade C Setup (Skip)

```
❌ Mixed candles, no clear direction
❌ Price within $100 of target
❌ Doji candle present
❌ Under 8 minutes remaining
❌ Market at 90¢+
→ Do not bet
```

---

## Part 5 : Expected Results Over 20 Trades

### Grade A Trades Only (Selective)

```
Assumption: 10 Grade A setups in 20 sessions
Win rate target: 65%

Wins:   6-7 per 10 bets
Losses: 3-4 per 10 bets

At $2/bet, average odds 60¢:
  Win payout:  $2 ÷ $0.60 = $3.33  →  +$1.33 profit
  Loss:        -$2.00

Expected per 10 bets:
  6.5 wins × $1.33  = +$8.65
  3.5 losses × $2   = -$7.00
  Net               = +$1.65 profit on $20 wagered
  ROI               = +8.3%

Conservative but real edge.
Scale up only after 50+ documented trades.
```

---

## Summary

```
What works:
→ 15-minute markets with clear 4+ candle momentum
→ Price already on winning side by $200+
→ EMA 9/21 alignment confirming direction
→ Sell at 100%+ profit without exception

What does not work:
→ 5-minute markets (ever)
→ Betting when price is within $100 of target
→ Holding through profit for "more"
→ Betting without all 8 checklist items confirmed
```

---

*The setup decides the trade. The checklist removes the emotion.*
