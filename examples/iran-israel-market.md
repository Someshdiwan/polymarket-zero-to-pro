# Case Study Iran / Israel Strike Markets

> A real trade scenario from March 2026. This case study walks through the full decision process market identification, probability estimation, position sizing, and outcome analysis on one of the highest volatility geopolitical markets of the year.

---

## Background

On February 28, 2026, the US and Israel launched "Operation Epic Fury" a coordinated strike campaign across 24 Iranian provinces. Iranian Supreme Leader Khamenei was killed. Iran retaliated with successive missile waves targeting Israel.

Polymarket had active markets on each specific date asking whether strikes would occur.

---

## The Markets

```
"Will US/Israel strike Iran on March 2?"
"Will US/Israel strike Iran on March 3?"
"Will US/Israel strike Iran on March 4?"
"Will US/Israel strike Iran on March 5?"

Each date = separate contract
Each resolves independently at end of that date
```

---

## Part 1 : Market Prices as Events Unfolded

### February 28 (Strike Begins)

```
Before news broke:
  YES = 15¢   (market thought 15% chance)
  NO  = 85¢

After first strike confirmed:
  YES = 92¢   (+513% move in hours)
  NO  = 8¢

Lesson: Early YES buyers made 6x
        Late YES buyers (at 92¢) had terrible risk/reward
```

### March 2 (Active Strike Day)

```
Morning:
  YES = 97¢   (near certain, ongoing strikes)
  NO  = 3¢

End of day:
  Strikes confirmed on March 2
  YES resolves → $1.00
  NO  resolves → $0.00

YES buyers at 15¢ → 567% return ✅
NO  buyers at 85¢ → -100%       ❌
```

### March 5 (Later Date)

```
March 2:  YES = 85¢  (high, ongoing campaign)
March 4:  YES = 85¢  (still high)
March 5:  YES = 85¢  (slightly lower, uncertainty)

By March 5: Campaign paused
  YES = drops to 40¢ intraday
  Final: strikes did not occur on March 5
  NO resolves → $1.00

NO buyers at 15¢ on March 5 → 567% return ✅
```

---

## Part 2 : The Decision Framework Applied

### Should You Have Bought YES at 15¢ (Feb 28 morning)?

```
Market price:     YES at 15¢ (15% implied probability)
Situation:        US/Israel military buildup confirmed
                  Multiple credible sources reporting
                  Historical escalation patterns

Your estimate:    40% chance (based on news reading)
Edge:             40% − 15% = +25% ✅

EV on $5 bet:
  Shares = $5 ÷ $0.15 = 33.3 shares
  Win payout = 33.3 × $1 = $33.30

  EV = (0.40 × $28.30) − (0.60 × $5)
     = $11.32 − $3.00
     = +$8.32 ✅ Strong positive EV
```

**Decision: YES was a strong bet at 15¢**

---

### Should You Have Bought NO at 3¢ (March 2 morning)?

```
Market price:     NO at 3¢  (3% implied probability)
Situation:        Strikes actively ongoing that morning
                  Multiple live reports of aircraft

Your estimate:    2% chance strikes stop before EOD
Edge:             2% − 3% = −1% ❌

EV on $5 bet:
  Shares = $5 ÷ $0.03 = 166.7 shares
  Win payout = $166.70

  EV = (0.02 × $161.70) − (0.98 × $5)
     = $3.23 − $4.90
     = −$1.67 ❌ Negative EV
```

**Decision: NO at 3¢ with active strikes = negative EV. Skip.**

The potential 50x return does not justify the near-zero probability.

---

### Should You Have Bought NO on March 5 at 15¢?

```
Market price:     NO at 15¢  (15% implied)
Situation:        March 2-4 strikes confirmed
                  March 5 = new date, escalation ongoing
                  BUT: campaigns have natural pauses
                  Iran had launched 10th missile wave (retaliation)

Your estimate:    35% chance NO wins
                  (campaign could pause for diplomacy/assessment)
Edge:             35% − 15% = +20% ✅

EV on $5 bet:
  Shares = $5 ÷ $0.15 = 33.3
  Win payout = $33.30

  EV = (0.35 × $28.30) − (0.65 × $5)
     = $9.91 − $3.25
     = +$6.66 ✅
```

**Decision: NO on March 5 was a strong bet at 15¢**
**Outcome: NO won. 567% return.**

---

## Part 3 : What the Market Got Wrong

### Systematic Mispricing Pattern

```
The market priced each subsequent date
as nearly equal probability to the current date.

March 2: YES 97¢  (correct — strikes ongoing)
March 3: YES 95¢  (roughly correct)
March 4: YES 90¢  (reasonable)
March 5: YES 85¢  (OVERPRICED)
March 6: YES 80¢  (OVERPRICED)

Why overpriced?
→ Retail traders extrapolate current events forward
→ "It's happening now, so it will keep happening"
→ Ignores: ceasefire probability, diplomatic pauses,
           military logistics, political pressure

The edge: Later dates in an active campaign
          are systematically overpriced on YES
```

### The Contrarian Trade

```
When a geopolitical campaign is at peak intensity:
→ Near-term YES = correctly priced
→ Later-date YES = often overpriced
→ Later-date NO = value opportunity

This pattern repeats across conflicts.
Ukraine/Russia, Iran/Israel, Taiwan strait threats.
```

---

## Part 4 : Risk Management on Geopolitical Markets

### Position Sizing for Extreme Volatility

```
Geopolitical markets can move 80% in minutes.
Single tweet from world leader = massive swing.

Rules:
→ Maximum 10% of bankroll per geopolitical bet
   (not the usual 20%)
→ Never bet multiple correlated dates heavily
   (March 2 + March 3 + March 4 = same risk)
→ Set price alerts, do not hold blindly overnight
→ News changes everything — monitor actively
```

### The Correlated Risk Trap

```
Mistake:
  $5 on March 2 YES
  $5 on March 3 YES
  $5 on March 4 YES

Looks like 3 separate bets.
Reality: ALL lose if strikes stop.
Effective single bet = $15 on "strikes continue"

Correct approach:
  $5 on one date maximum
  Or distribute across YES and NO on different dates
```

---

## Part 5 : Full Trade Log (Example)

```
Trade 1:
  Date:     Feb 28 morning
  Market:   "US/Israel strike Iran March 2?"
  Side:     YES
  Price:    15¢
  Amount:   $5.00
  Shares:   33.33
  Outcome:  WIN
  Payout:   $33.33
  Profit:   +$28.33
  Return:   +567%

Trade 2:
  Date:     March 2 morning
  Market:   "US/Israel strike Iran March 5?"
  Side:     NO
  Price:    15¢
  Amount:   $5.00
  Shares:   33.33
  Outcome:  WIN
  Payout:   $33.33
  Profit:   +$28.33
  Return:   +567%

Combined:
  Invested: $10.00
  Returned: $66.66
  Profit:   +$56.66
  ROI:      +567%
```

---

## Part 6 : Key Lessons

```
1. Early positioning before news = maximum edge
   (15¢ before vs 97¢ after = 6x difference in return)

2. Later dates in active campaigns = systematic NO edge
   Market overprices continuation

3. Correlated bets = not diversification
   Multiple dates = same underlying risk

4. 97¢+ markets have near-zero positive EV
   Even when "obvious" — reward doesn't justify stake

5. News speed is your most accessible edge
   First 30 minutes after breaking news = opportunity
   After 2 hours = market has priced it in

6. Each date resolves independently
   One date winning doesn't predict the next
```

---

## Quick Reference

```
╔══════════════════════════════════════════════════╗
║        GEOPOLITICAL MARKET RULES                 ║
╠══════════════════════════════════════════════════╣
║ Enter BEFORE market fully prices in news         ║
║ Later dates = often better NO value              ║
║ Max 10% bankroll on geopolitical bets            ║
║ Never stack correlated date bets                 ║
║ 95¢+ = skip regardless of conviction             ║
║ Monitor actively — single tweet moves 50%        ║
╚══════════════════════════════════════════════════╝
```

---

*The crowd extrapolates. The edge is in knowing when the crowd is wrong about how far.*
