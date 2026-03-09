# 📊 How Markets Work on Polymarket

> Understanding YES/NO markets, share mechanics, prices, and payouts explained simply with real examples.

---

## The Core Idea

```
Polymarket asks a YES or NO question
You buy shares betting on the answer
Each share = $1 if you are correct
Each share = $0 if you are wrong
```

---

## Part 1 : YES and NO Shares

### What is a YES Share?
```
You believe the event WILL happen
You buy YES shares
If event happens → each share = $1 ✅
If event doesn't → each share = $0 ❌
```

### What is a NO Share?
```
You believe the event WILL NOT happen
You buy NO shares
If event doesn't happen → each share = $1 ✅
If event happens       → each share = $0 ❌
```

### Real Example
```
Market: "Will US strike Iran on March 3?"

Buy YES = betting strike HAPPENS
Buy NO  = betting strike DOES NOT happen

Strike happens   → YES wins, NO loses
No strike        → NO wins, YES loses
```

---

## Part 2 : How Share Price Works

### Price = Probability
```
Share price is always between 0¢ and 100¢

1¢   = 1% chance   (very unlikely)
10¢  = 10% chance  (unlikely)
50¢  = 50% chance  (coin flip)
90¢  = 90% chance  (very likely)
99¢  = 99% chance  (almost certain)
```

### YES + NO always = 100¢
```
YES = 97¢  →  NO = 3¢   (total = 100¢)
YES = 50¢  →  NO = 50¢  (total = 100¢)
YES = 20¢  →  NO = 80¢  (total = 100¢)
```

### Who Sets the Price?
```
NOT Polymarket
NOT a bookmaker

YOU and other traders set the price!

More people buy YES → YES price rises
More people buy NO  → NO price rises
Supply and demand = price discovery
```

---

## Part 3 : Share Calculation

### Formula
```
Shares = Amount Invested ÷ Share Price
Payout = Shares × $1 (if you win)
Profit = Payout - Amount Invested
```

### Examples

**Buying YES at 50¢**
```
Invest $10 at 50¢
Shares = $10 ÷ $0.50 = 20 shares
If YES wins → 20 × $1 = $20
Profit = $20 - $10 = $10 (+100%)
```

**Buying NO at 2.8¢**
```
Invest $10 at 2.8¢
Shares = $10 ÷ $0.028 = 357 shares
If NO wins → 357 × $1 = $357
Profit = $357 - $10 = $347 (+3470%!)
```

**Buying YES at 99¢**
```
Invest $10 at 99¢
Shares = $10 ÷ $0.99 = 10.1 shares
If YES wins → 10.1 × $1 = $10.10
Profit = $10.10 - $10 = $0.10 (+1%)
```
> ⚠️ High price = low reward, not worth it

---

## Part 4 : The Payout Table

### If you invest $10 at different prices

| Buy Price | Shares | If You WIN | Profit | Return |
|---|---|---|---|---|
| 1¢ | 1000 | $1000 | $990 | 9900% |
| 2¢ | 500 | $500 | $490 | 4900% |
| 5¢ | 200 | $200 | $190 | 1900% |
| 10¢ | 100 | $100 | $90 | 900% |
| 25¢ | 40 | $40 | $30 | 300% |
| 50¢ | 20 | $20 | $10 | 100% |
| 75¢ | 13.3 | $13.3 | $3.3 | 33% |
| 99¢ | 10.1 | $10.1 | $0.1 | 1% |

> 💡 Low price = high reward but low probability 💰

> 💡 High price = low reward but high probability 💰

---

## Part 5 : What Happens When Price Changes

### Your shares NEVER change after buying
```
You buy 357 NO shares at 2.8¢
Price moves to 10¢
You still own → 357 shares ✅
Your max payout → still $357 ✅
Only current sell value changes
```

### Current Value vs Final Payout

| NO Price | Your 357 Shares Worth NOW | If NO Wins (Final) |
|---|---|---|
| 1¢ | $3.57 | $357 |
| 2.8¢ (entry) | $10.00 | $357 |
| 5¢ | $17.85 | $357 |
| 10¢ | $35.70 | $357 |
| 50¢ | $178.50 | $357 |
| 100¢ | $357.00 | $357 |

```
Current value = what you get if you SELL NOW
Final payout  = what you get if you HOLD and WIN
```

---

## Part 6 : New Buyers vs Your Position

### Your payout is LOCKED at entry
```
You buy NO at 2.8¢ → To win $357 LOCKED 🔒

1 hour later:
NO price drops to 1¢
New buyers pay 1¢ → they win $1000

YOUR payout = still $357 (locked at your entry)
THEIR payout = $1000 (they got cheaper price)

Their better deal does NOT affect you
```

### Movie Ticket Analogy 🎬
```
You bought ticket at ₹200
Next day price drops to ₹100
You still watch same movie
Others pay less but your seat is yours
```

---

## Part 7 : Multi-Date Markets

Some markets have multiple dates like:

```
US/Israel strikes Iran on...?

March 2  → 97%  YES 97¢  |  NO 3¢
March 3  → 95%  YES 95¢  |  NO 5¢
March 4  → 90%  YES 90¢  |  NO 10¢
March 5  → 85%  YES 85¢  |  NO 15¢
```

### What This Means
```
Each date = separate market
March 2 = "Will it happen specifically on March 2?"
March 3 = "Will it happen specifically on March 3?"

They are INDEPENDENT bets
Winning one doesn't affect others
```

### Why Later Dates Are Cheaper
```
March 2 = 97¢ YES (very likely today)
March 5 = 85¢ YES (less certain for that specific day)

Market gets less certain further in future
= NO shares get more expensive later
= Higher potential payout for NO buyers
```

---

## Part 8 : Order Book

```
Order Book = list of all buy/sell orders

Shows:
→ How many people want to buy YES at X price
→ How many people want to sell YES at Y price
→ Liquidity of the market
```

### High Volume vs Low Volume

| | High Volume ($1M+) | Low Volume ($1K) |
|---|---|---|
| Spreads | Tight | Wide |
| Manipulation | Hard | Easy |
| Sell easily? | Yes ✅ | Hard ❌ |
| Reliable price? | Yes ✅ | Not always ❌ |

> 💡 Always prefer high volume markets for fair pricing

---

## Part 9 : Market Types by Time

### Short Term (Minutes)
```
BTC Up or Down — 5 Minutes
BTC Up or Down — 15 Minutes

→ Pure speculation
→ No real edge possible
→ Avoid unless using candle strategy
```

### Medium Term (Hours/Days)
```
"Will X happen today?"
"Will X happen this week?"

→ News can give you edge
→ React fast to breaking news
→ Best for active traders
```

### Long Term (Weeks/Months)
```
"Who wins 2026 election?"
"Will BTC reach $200K in 2026?"

→ Research gives edge
→ Price moves slowly
→ Best for patient traders
```

---

## Part 10 : How Auto Resolution Works

```
Step 1: Market deadline passes
           ↓
Step 2: Polymarket checks outcome
        (Uses APIs, news, trusted sources)
           ↓
Step 3: Result announced on-chain
           ↓
Step 4: Winning shares = $1 each (automatic)
           ↓
Step 5: Losing shares = $0 (automatic)
           ↓
Step 6: Money in your Cash balance
           ↓
Step 7: You see updated balance ✅

Works even if:
→ App is closed ✅
→ You are sleeping ✅
→ You are offline ✅
```

---

## Part 11 : Sell vs Hold Decision

```
                 You own shares
                      ↓
              Is market resolved?
             /                   \
           YES                    NO
            ↓                     ↓
    Auto paid $1/share      Check current price
    No action needed              ↓
                          Are you in profit?
                         /                  \
                       YES                  NO
                        ↓                   ↓
              Is profit > 100%?      How confident are you?
              /             \         /              \
            YES              NO     High              Low
             ↓                ↓      ↓                 ↓
          SELL NOW          Hold    Hold            Sell now
          immediately      or sell                 cut losses
```

---

## Quick Reference Cheatsheet

```
╔══════════════════════════════════════════╗
║         POLYMARKET QUICK MATH            ║
╠══════════════════════════════════════════╣
║ Shares = Amount ÷ Price                  ║
║ Payout = Shares × $1                     ║
║ Profit = Payout - Amount                 ║
║ Return = (Profit ÷ Amount) × 100         ║
╠══════════════════════════════════════════╣
║ Price 1¢  = 99% chance to lose           ║
║ Price 50¢ = 50/50 coin flip              ║
║ Price 99¢ = 99% chance to win (low pay)  ║
╠══════════════════════════════════════════╣
║ YES + NO price = always 100¢             ║
║ Your shares = locked after buying        ║
║ Your payout = locked after buying        ║
║ Auto resolve = no action needed          ║
╚══════════════════════════════════════════╝
```

---

## Common Questions

**Q: Can I lose more than I invest?**
```
No. Maximum loss = amount you invested
You can never go negative on Polymarket
```

**Q: What if I want to exit early?**
```
Go to Positions tab → Click Sell
Get current market price
Can exit anytime before resolution
```

**Q: What if nobody wants to buy my shares?**
```
Low liquidity markets = hard to sell
Always check volume before buying
High volume ($100K+) = easy to sell anytime
```

**Q: Does price change affect my final payout?**
```
No. Your payout is locked at entry price
Price changes only affect sell value
If you hold to resolution = always get locked payout
```

---

## Next Steps

| I want to... | Go to... |
|---|---|
| Learn buy/sell/hold | [03-buy-sell-hold.md](03-buy-sell-hold.md) |
| Calculate my profits | [04-profit-loss-calc.md](04-profit-loss-calc.md) |
| Learn trading strategy | [07-quant-mindset.md](07-quant-mindset.md) |

---

*Real experience. Real numbers. Real mistakes. 😄*