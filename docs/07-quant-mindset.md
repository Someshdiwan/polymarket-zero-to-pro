# The Quant Trader Mindset

> Professional prediction market traders do not guess. They identify mispriced probabilities, quantify their edge, and execute with discipline. This document is the difference between gambling and trading.

---

## The Fundamental Principle

```
Every market price is the crowd's best estimate
of probability.

Your job is not to predict the future.
Your job is to find where the crowd is wrong.

Wrong by enough to profit from.
```

---

## Part 1 Edge: The Only Thing That Matters

### What is Edge?
```
Edge = Your estimated probability − Market price

Positive edge = YOU think event is more likely than market
Negative edge = Market knows something you don't
Zero edge     = Coin flip, do not bet
```

### Edge Examples

**Positive Edge → Bet ✅**
```
Market: "Will Fed cut rates in March?"
Market price: YES at 20¢ (20% chance)
Your research: Strong inflation data, 40% chance

Edge = 40% − 20% = +20% edge
This is a bet worth taking
```

**Zero Edge → Skip ❌**
```
Market: "Will BTC be up in 5 minutes?"
Market price: UP at 50¢ (50% chance)
Your view: Also 50%

Edge = 50% − 50% = 0%
No edge = no bet
This is a casino game
```

**Negative Edge → Never Bet ❌**
```
Market: "Will US strike Iran?"
Market price: YES at 97¢
Breaking news: Strike confirmed

Edge = 0% (market already knows)
You have no information advantage
Betting YES here = buying at peak
```

---

## Part 2 : Information Hierarchy

### Where Edge Comes From

```
Level 1 — Public news (everyone has this)
          Edge: Near zero
          Example: CNN reports on Iran

Level 2 — Deep domain knowledge
          Edge: Moderate
          Example: You study geopolitics daily,
                   understand nuance others miss

Level 3 — Speed advantage
          Edge: Time-sensitive
          Example: Breaking news drops,
                   you bet before market updates

Level 4 — Synthesis advantage
          Edge: Strong
          Example: You combine 5 sources,
                   form view market hasn't priced yet

Level 5 — Structural knowledge
          Edge: Strongest
          Example: You understand resolution criteria
                   better than other traders
```

### Your Best Markets = Your Deepest Knowledge
```
Follow cricket daily?        → Bet cricket markets
Follow geopolitics daily?    → Bet Iran/Russia/China markets
Follow crypto deeply?        → Bet BTC/ETH markets
Follow Indian politics?      → Bet Indian election markets
Follow economics?            → Bet Fed/RBI/inflation markets

Never bet markets where you
have no informational advantage
```

---

## Part 3 : Expected Value Thinking

### The Core Formula
```
EV = (Win Probability × Profit) − (Lose Probability × Loss)

Positive EV = bet is profitable over time
Negative EV = bet loses money over time
Zero EV     = break even (fees make it negative)
```

### Calculating EV Step by Step

**Setup:**
```
Market: Iran strike on March 3
Market price: YES at 95¢, NO at 5¢
You think: Only 80% chance (market overpricing)
Bet: $5 on NO

Your NO probability = 20% (100% − 80%)
Market NO probability = 5%
Your edge = 20% − 5% = +15%
```

**EV Calculation:**
```
If NO wins (20% chance):
Profit = ($5 ÷ 0.05) − $5 = $95

If YES wins (80% chance):
Loss = $5

EV = (0.20 × $95) − (0.80 × $5)
EV = $19.00 − $4.00
EV = +$15.00 per $5 bet ✅

Strong positive EV = take this bet
```

### EV Red Flags
```
EV is negative when:
→ You have no edge (just following crowd)
→ Market already priced the news
→ Your probability estimate = market price
→ Betting 99¢ markets (near zero reward)
→ BTC 5 min (random noise)
```

---

## Part 4 : Probability Calibration

### What is Calibration?
```
A well-calibrated trader is right
exactly as often as they predict.

If you say 70% chance → you should win 70% of those bets
If you say 30% chance → you should win 30% of those bets

Miscalibrated traders consistently over or underestimate
```

### How to Improve Calibration

**Track your predictions:**
```
Before each bet record:
→ Your estimated probability
→ Market price
→ Outcome

After 50 bets analyse:
→ When you said 70%, did you win 70% of time?
→ When you said 30%, did you win 30% of time?

Gaps = your calibration error = where you lose money
```

**Common calibration biases:**
```
Overconfidence bias
→ You think 90% chance, actually 60%
→ You overbuy expensive positions

Recency bias
→ Last event happened → you think next will too
→ You chase recent trends

Narrative bias
→ Good story = high probability in your mind
→ Good stories do not always win markets
```

---

## Part 5 : The Kelly Criterion

### Optimal Position Sizing
```
Never bet too much → ruin risk
Never bet too little → underperform
Kelly finds the mathematically optimal size
```

### Formula
```
f = (bp − q) ÷ b

f = fraction of bankroll to bet
b = net odds received (payout ÷ stake − 1)
p = your estimated probability of winning
q = probability of losing (1 − p)
```

### Example
```
Market: NO at 5¢
Your estimated probability of NO winning: 20%
Bankroll: $14

b = ($100 − $5) ÷ $5 = 19
p = 0.20
q = 0.80

f = (19 × 0.20 − 0.80) ÷ 19
f = (3.80 − 0.80) ÷ 19
f = 3.00 ÷ 19
f = 0.158 = 15.8% of bankroll

Optimal bet = $14 × 0.158 = $2.21
```

### Half Kelly Rule
```
Full Kelly  = mathematically optimal
              but high variance, stressful

Half Kelly  = bet half the Kelly amount
            = lower variance
            = more comfortable
            = still highly profitable

Recommended for beginners:
Bet 50% of Kelly output
```

---

## Part 6 : Market Regimes

### Different Markets Require Different Approaches

**Trending Market**
```
Strong consensus building
Price moving consistently one direction
News flow one-sided

Strategy: Follow trend carefully
          Look for value in that direction
          Avoid fighting consensus
```

**Uncertain Market**
```
Price hovering around 40-60¢
Conflicting news sources
No clear direction

Strategy: Wait for clarity
          Do not bet in fog
          Best opportunities come after uncertainty resolves
```

**Overreaction Market**
```
Price spikes to 95¢+ on single news item
Market in panic or euphoria
Other bettors emotional

Strategy: This is where edge lives
          Counter-trade if you have information
          Market often overcorrects
```

**Stale Market**
```
Old news already priced in
No new information flowing
Price static

Strategy: Skip entirely
          No new edge available
          Wait for catalyst
```

---

## Part 7 : The Research Process

### Before Every Significant Bet

**Step 1 — Define the question precisely**
```
Not "will Iran do something?"
But "will US/Israel strike Iran specifically on March 3?"

Resolution criteria matter enormously
Read the market rules carefully
```

**Step 2 — Gather information**
```
Primary sources first:
→ Official government statements
→ Military briefings
→ Verified journalist reports

Secondary sources:
→ Analysis from domain experts
→ Historical base rates
→ Similar past events
```

**Step 3 — Assign probability independently**
```
Start with base rate
"How often does this type of event happen?"

Adjust for current context
"What makes this situation different?"

Arrive at YOUR number
independent of market price
```

**Step 4 — Compare to market**
```
Your number vs market price

Gap > 10% = potential bet
Gap < 10% = insufficient edge, skip
```

**Step 5 — Size the bet**
```
Use Kelly or 20% rule
Never let conviction override risk management
```

---

## Part 8 : Psychological Discipline

### The Trader's Enemies

**Tilt**
```
Definition: Emotional state after loss
            causing irrational bets

Signs:
→ Increasing bet size after loss
→ Betting markets you don't understand
→ Ignoring your own research
→ Feeling you "deserve" to win

Fix:
→ Stop trading for the day
→ Review your trade log
→ Resume only when calm
```

**FOMO**
```
Definition: Chasing a market because
            others are profiting

Signs:
→ Betting after price already moved
→ Buying 90¢+ markets
→ Rushing without research

Fix:
→ There is always another market
→ Late entry = worst risk/reward
→ Missing a trade costs nothing
```

**Overconfidence**
```
Definition: Believing your edge is
            larger than it actually is

Signs:
→ Betting large after win streak
→ Skipping research steps
→ Dismissing contradicting information

Fix:
→ Track calibration rigorously
→ Win streaks are often luck
→ Process matters more than outcomes
```

---

## Part 9 : Building a Trading System

### What a System Looks Like
```
1. Universe of markets
   → Only bet categories you know deeply

2. Signal generation
   → News + probability estimate + EV calculation

3. Position sizing
   → Kelly or fixed 20% rule

4. Entry rules
   → Edge > 10% required
   → Minimum market volume $50K

5. Exit rules
   → Sell at 100%+ profit
   → Cut at 50% loss if thesis broken
   → Hold to resolution if confident

6. Review process
   → Log every trade
   → Weekly review of win rate
   → Monthly calibration check
```

### Why Systems Beat Intuition
```
Intuition = inconsistent, emotional, biased
System    = consistent, unemotional, improvable

A 55% win rate system run consistently
beats a 70% intuition trader
who bets emotionally
```

---

## Part 10 : Weekly Routine

### The Professional Approach
```
Daily (10 minutes):
→ Scan new markets in your categories
→ Check news on open positions
→ Log any resolved bets

Weekly (30 minutes):
→ Review trade log
→ Calculate win rate by category
→ Identify best and worst decisions
→ Adjust strategy if needed

Monthly (1 hour):
→ Full calibration review
→ P&L analysis
→ Refine market selection criteria
```

---

## Quick Reference

```
╔══════════════════════════════════════════════════╗
║              QUANT TRADER RULES                  ║
╠══════════════════════════════════════════════════╣
║ Never bet without edge                           ║
║ Edge = your probability minus market price       ║
║ Minimum edge required = 10%                      ║
║ Size using Kelly or 20% rule                     ║
║ Track every bet, every outcome                   ║
║ Specialise in 2-3 market categories              ║
║ News speed = your most accessible edge           ║
║ Stop trading when emotional                      ║
║ Missing a trade costs nothing                    ║
║ Process matters more than any single outcome     ║
╚══════════════════════════════════════════════════╝
```

---

## Next Steps

| I want to... | Go to... |
|---|---|
| Understand market types | [08-market-types.md](08-market-types.md) |
| Compare platforms | [09-kalshi-vs-polymarket.md](09-kalshi-vs-polymarket.md) |
| Use profit calculator | [scripts/profit_calculator.py](../scripts/profit_calculator.py) |
| Avoid mistakes | [10-mistakes-and-scams.md](10-mistakes-and-scams.md) |

---

*The market is not your opponent. Your own emotions are.*