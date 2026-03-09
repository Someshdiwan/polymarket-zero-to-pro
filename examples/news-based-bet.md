# Case Study : News Based Bet

> How to identify, analyse, and time a trade based on breaking news before the market fully reprices. This is the highest-accessibility edge for retail traders speed of information processing, not inside information.

---

## The Core Principle

```
News breaks
     ↓
Market takes 5-30 minutes to reprice
     ↓
Your window of opportunity exists here
     ↓
After 30-60 minutes — edge is gone
```

---

## Part 1 : Finding the Opportunity

### The Setup

```
Date:    March 4, 2026, 7:42 AM IST
Source:  Reuters breaking news alert

Headline:
"Federal Reserve Chair signals rate cut
 likely at May meeting, citing cooling inflation"

Polymarket market:
"Will Fed cut rates at May 2026 FOMC meeting?"
```

### Market Prices at 7:42 AM

```
YES = 38¢  (38% implied probability)
NO  = 62¢

Volume: $2.1M (high liquidity ✅)
```

### The Analysis Window

```
7:42 AM — Headline drops
7:43 AM — You read the headline
7:44 AM — You open the full Reuters article
7:46 AM — You check Fed Chair's exact wording
7:48 AM — You form your probability estimate
7:50 AM — You check market price again
           YES now at 44¢ (already moved +6¢)
7:52 AM — You place bet
```

---

## Part 2 : Probability Estimation

### Step 1 : Read the Primary Source

```
Not Reuters summary — the actual Fed Chair statement:

"Given the continued moderation in core PCE
 and labour market softening, the Committee
 will give serious consideration to adjustment
 at the May meeting."

Key phrase: "serious consideration"
Not: "we will cut"
Not: "a cut is appropriate"
```

### Step 2 : Historical Base Rate

```
When Fed Chair uses "serious consideration" language:
→ Historically cuts ~65% of time at that meeting
→ Remaining 35%: data worsens before meeting date

Source: Fed meeting transcripts 2015-2025
```

### Step 3 : Current Context Adjustment

```
Factors supporting cut (push probability UP):
→ Core PCE trending down 3 months straight
→ Unemployment ticked up 0.2% last month
→ Chair's language more direct than usual

Factors against cut (push probability DOWN):
→ Oil prices up 8% this month (inflation risk)
→ Strong retail sales data last week
→ One dissenting Fed governor already vocal

Net assessment: 60% probability of May cut
```

### Step 4 : Compare to Market

```
Your estimate:    60%
Market price:     44¢ (44% implied)
Edge:             60% − 44% = +16% ✅

EV on $5 bet:
  Shares = $5 ÷ $0.44 = 11.36
  Win payout = $11.36

  EV = (0.60 × $6.36) − (0.40 × $5)
     = $3.82 − $2.00
     = +$1.82 ✅ Strong positive EV
```

---

## Part 3 : Trade Execution

### Kelly Sizing

```
Bankroll:    $20
p:           0.60
price:       44¢
b:           (100/44) - 1 = 1.27

Kelly = (1.27 × 0.60 - 0.40) / 1.27
      = (0.762 - 0.40) / 1.27
      = 0.285 = 28.5% of bankroll

Half Kelly = 14.25%
Bet size   = $20 × 0.1425 = $2.85

Cap at 20%: $20 × 0.20 = $4.00
Recommended: $2.85
```

### Order Placed

```
Time:     7:52 AM
Side:     YES
Price:    44¢
Amount:   $2.85
Shares:   $2.85 ÷ $0.44 = 6.48 shares
Payout:   $6.48 if YES wins
Profit:   +$3.63 if YES wins
Return:   +127% if YES wins
Loss:     -$2.85 if NO wins
```

---

## Part 4 : Monitoring the Position

### Price Movement After Trade

```
7:52 AM  (entry)  YES = 44¢
8:15 AM            YES = 52¢  (+18%)  — more analysts weigh in
9:00 AM            YES = 58¢  (+32%)  — Bloomberg confirms story
11:00 AM           YES = 61¢  (+39%)  — market consensus building
Next day           YES = 64¢  (+45%)

Current sell value at 64¢:
  6.48 shares × $0.64 = $4.15
  Profit if sell now  = +$1.30 (+46%)
```

### Hold or Sell Decision

```
Original thesis: 60% probability
Market now says: 64% probability

Has anything changed?
→ No new data released
→ Market has caught up to your estimate
→ Edge has largely disappeared

Edge at entry:  +16%
Edge now:       60% − 64% = −4% (market overshot slightly)

Decision: The edge is gone.
          Original thesis was 60%, market now says 64%.
          Sell and lock in the profit.
```

### Exit

```
Time:    Next morning
Price:   64¢
Sell:    6.48 shares × $0.64 = $4.15
Profit:  +$1.30
Return:  +46% overnight ✅
```

---

## Part 5 : What If You Had Waited for Resolution?

### Resolution Scenario Analysis

```
If YES wins (60% chance):
  Hold to resolution → $6.48 payout → +$3.63 profit (+127%)

If NO wins (40% chance):
  Hold to resolution → $0 payout → -$2.85 loss (-100%)

Expected value of holding:
  EV = (0.60 × $3.63) − (0.40 × $2.85)
     = $2.18 − $1.14
     = +$1.04

Actual profit from selling early:
  +$1.30

Selling early was BETTER in this case.
Why? Market overpriced YES at 64¢ vs your 60% estimate.
When market overshoots your estimate = sell.
```

---

## Part 6 : News Speed Framework

### The 4 Windows

**Window 1 — First 5 Minutes (Maximum Edge)**

```
News just broke
Market still at old price
Maximum edge available
Act fast, research in parallel
Risk: incomplete information
```

**Window 2 — 5 to 30 Minutes (Good Edge)**

```
Market starting to move
Full article available to read
More complete picture
Still meaningful edge if your analysis is deeper
```

**Window 3 — 30 to 120 Minutes (Shrinking Edge)**

```
Major outlets have covered it
Most traders have seen it
Market approaching fair value
Only bet if your analysis differs from consensus
```

**Window 4 — After 2 Hours (No Edge)**

```
Market has fully priced the news
Everyone has the same information
Edge = 0%
Skip unless new information emerges
```

---

## Part 7 : News Sources by Market Type

### For Each Category

```
Politics/Economics:
→ Reuters, Bloomberg, WSJ (primary)
→ Fed website (fomc.federalreserve.gov) for Fed news
→ Official government press releases

Geopolitics:
→ Reuters Breaking News (Twitter/X)
→ BBC News live feed
→ Al Jazeera (Middle East coverage)
→ ISW (Institute for the Study of War)

Crypto:
→ CoinDesk, The Block (primary)
→ Official protocol blogs
→ SEC.gov for regulatory news

Indian Markets:
→ Economic Times
→ LiveMint
→ RBI website (rbi.org.in) for RBI decisions
```

### Speed Setup

```
Phone:  Reuters app with breaking news notifications ON
Laptop: TweetDeck with curated news accounts
Polymarket: open in separate tab, refresh ready

When alert fires:
  1. Read headline (10 seconds)
  2. Identify relevant Polymarket market (30 seconds)
  3. Check current price (10 seconds)
  4. Quick probability estimate (60 seconds)
  5. Place bet if edge > 10% (30 seconds)
  Total: under 3 minutes from alert to trade
```

---

## Part 8 : Common News Trading Mistakes

### Mistake 1 — Trading the Headline Not the Resolution Criteria

```
Headline: "Fed signals rate cut possible"
Market:   "Will Fed cut rates AT MAY MEETING?"

"Possible" ≠ "will happen at May specifically"
Always read the resolution criteria
Vague news ≠ certain resolution
```

### Mistake 2 — Entering After Market Has Repriced

```
You see the news 45 minutes late
Market already moved from 38¢ to 72¢
Edge is gone — do not chase

Discipline: if you missed the move, skip the trade
```

### Mistake 3 — Confusing Sentiment with Probability

```
News feels very bullish
You feel 90% confident
Your actual informed estimate: 60%

Separate feeling from analysis
Write down your number before checking market price
```

### Mistake 4 — Ignoring Conflicting Data

```
Bullish Fed news drops
BUT: oil prices just spiked 10% (inflationary)
Conflicting signals = lower confidence = smaller bet
Or skip entirely until picture clears
```

---

## Summary

```
The news-based edge formula:

1. Fast news source (Reuters, Bloomberg alerts)
2. Read primary source — not just headline
3. Form probability estimate BEFORE checking market
4. Compare to market price
5. Edge > 10% = bet within first 30 minutes
6. Sell when market catches up to your estimate
7. Never enter after 2+ hours of coverage
```

---

*Speed is your edge. Analysis is your weapon. The market pays those who are both fast and right.*
