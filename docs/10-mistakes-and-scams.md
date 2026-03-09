# Mistakes & Scams  What Destroys Traders

> The fastest way to become profitable is to stop losing money unnecessarily. Most beginner losses on Polymarket are not from bad luck they are from predictable, avoidable mistakes and deliberate scams. This document covers both.

---

## Two Categories of Loss

```
Category 1 — Trading Mistakes
             Errors in judgment, strategy, and psychology
             Fixable with knowledge and discipline

Category 2 — Scams
             Deliberate fraud by external actors
             Preventable with awareness
```

---

## Part 1 : Critical Trading Mistakes

---

### Mistake 1 — Not Selling at 100%+ Profit

```
What happens:
Position shows 200%, 300%, 462% profit
Trader holds for more
Market resolves wrong
Profit = $0

Why it happens:
Greed overrides logic
"It might go higher" thinking
No pre-defined exit rule

The fix:
100%+ profit = sell immediately, no exceptions
Set the rule before you enter the trade
Remove emotion from the decision entirely
```

**Real example from this repo:**
```
Bought UP at 4¢ with $1
Position showed +462% ($5.62)
Did not sell
Market resolved against position
Result: -$1 instead of +$4.62

Cost of not selling: $5.62
```

---

### Mistake 2 — Trading BTC 5 Minute Markets

```
What happens:
Trader bets BTC up/down every 5 minutes
Loses consistently over time

Why it happens:
Looks like easy money
Action feels productive
Short feedback loop is addictive

The math:
5 min BTC = pure random noise
Expected value = 0% (negative after fees)
No strategy works consistently
House always wins over enough bets

The fix:
Never open a 5 minute market
15 minute minimum with candle strategy
See: 06-candlestick-strategy.md
```

---

### Mistake 3 — Wrong Network Selection

```
What happens:
Trader sends ETH via Ethereum mainnet
Pays $10-20 in gas fees
On a $20 deposit = 50-100% immediately lost to fees

Why it happens:
Ethereum is the default on most interfaces
Looks the same as Polygon/Base
Easy to miss the network selector

The fix:
Always verify network BEFORE confirming
Correct networks: Polygon or Base
Ethereum mainnet: Never for small amounts
Gas cost comparison:
  Ethereum = $5-20 per transaction
  Polygon  = $0.001 per transaction
  Base     = $0.001 per transaction
```

---

### Mistake 4 — Betting Without Edge

```
What happens:
Trader bets because market looks interesting
No research, no probability estimate
No comparison to market price
Pure gut feeling

Why it happens:
Feels like informed decision
Market topic is familiar
Overconfidence in general knowledge

The fix:
Before every bet ask:
→ What is MY probability estimate?
→ What is the market price?
→ Is my edge greater than 10%?
→ What is my information source?

If you cannot answer all four = do not bet
```

---

### Mistake 5 — Chasing Losses

```
What happens:
Lose $2 bet
Immediately bet $5 to recover
Lose $5 bet
Bet $10 to recover
Account destroyed in hours

Why it happens:
Loss aversion is hardwired into humans
Brain treats unrealised loss as emergency
Feels urgent to "fix" the loss immediately

The math:
$2 loss → $5 bet → $10 bet → $20 bet
One losing streak = account blown

The fix:
Each bet is completely independent
Previous losses do not change future probability
Daily loss limit = 30% of balance
Hit limit = stop trading for the day, no exceptions
```

---

### Mistake 6 — Ignoring Market Volume

```
What happens:
Trader buys into low volume market ($2K total)
Position shows profit
Tries to sell
No buyers available
Forced to hold to resolution
Resolution goes wrong

Why it happens:
Low volume markets have high potential payouts
Attractive odds mask the liquidity risk

The fix:
Minimum volume rules:
  Short-term trade  = $100K minimum
  Medium-term trade = $50K minimum
  Long-term hold    = $20K minimum
  Under $5K         = never trade
```

---

### Mistake 7 — Betting 99¢ Markets

```
What happens:
Market shows YES at 99¢
Trader thinks "easy win, almost certain"
Bets $10 to win $0.10
Takes same risk as any other bet
For negligible reward

The math:
$10 bet at 99¢ = win $0.10 or lose $10
Risk/reward = 100:1 against you
Even at 99% accuracy = negative EV long term

The fix:
Target markets in 5¢ - 70¢ range
Maximum meaningful entry at 80¢
Above 80¢ = reward does not justify risk
```

---

### Mistake 8 — Emotional Position Sizing

```
What happens:
Strong feeling about outcome
Bet entire balance on single market
Market resolves wrong
Account back to zero

Why it happens:
Conviction feels like certainty
"I know this will happen" thinking
No separation between confidence and probability

The fix:
Maximum per trade = 20% of balance
Strong conviction = still 20% maximum
Kelly Criterion for precise sizing
See: 07-quant-mindset.md Part 5
```

---

### Mistake 9 — Not Reading Resolution Criteria

```
What happens:
Trader bets on market
Event happens in ambiguous way
Market resolves differently than expected
Loss despite "being right"

Example:
Market: "Will US strike Iran on March 2?"
Trader thinks: airstrikes = YES
Resolution criteria: requires confirmed
ground troops (hypothetical example)
Airstrikes happen but market resolves NO

The fix:
Read the Rules section of every market
Understand exactly what qualifies as YES
Understand exactly what qualifies as NO
Ambiguous criteria = reduce position size
```

---

### Mistake 10 — Trading While Emotional

```
What happens:
After a loss, trader feels tilted
Makes impulsive bets to recover
Ignores research process
Loses more

Signs you are trading emotionally:
→ Increasing bet sizes after losses
→ Betting unfamiliar market categories
→ Skipping your research process
→ Feeling the market "owes" you a win
→ Checking positions every 5 minutes

The fix:
Define tilt triggers in advance
When triggered = mandatory stop for the day
No exceptions regardless of market conditions
```

---

## Part 2 : Scams to Avoid

---

### Scam 1 — P2P Personal UPI Request 🚨 MOST COMMON

```
How it works:
You initiate P2P trade on Binance
Seller contacts you in chat
Seller says: "Pay on my personal UPI: 9XXXXX@paytm"
Claims Binance app UPI is not working
You pay personal UPI
Seller cancels Binance order
You lose money, receive no crypto

Why it works:
Feels like helpful workaround
Seller sounds legitimate
Urgency pressure ("order will expire")

The rule:
ONLY pay UPI/bank details shown INSIDE Binance app
NEVER pay any number or ID shared in chat
If seller asks for personal payment = cancel + report immediately

How to report:
Binance → order → Appeal → select fraud reason
```

---

### Scam 2 — Fake Polymarket Websites

```
How it works:
Scammer creates near-identical website
polymarket.io
poly-market.com
polymarkets.com
polymarket.trade
You connect wallet to fake site
Site drains your wallet

How to identify:
Real URL = https://polymarket.com (only)
Check URL character by character
Bookmark the real site, always use bookmark

Signs of fake site:
→ URL slightly different
→ Asks for seed phrase
→ Unusual wallet permissions requested
→ Comes from social media ad or DM link
```

---

### Scam 3 — Fake Support Impersonation

```
How it works:
You post about an issue on Twitter/Discord/Telegram
Someone DMs you claiming to be Polymarket support
Asks you to "verify your wallet"
Asks for seed phrase or private key
Wallet drained immediately

The rule:
Polymarket support never DMs you first
No legitimate service ever asks for seed phrase
Seed phrase = complete wallet access = give to nobody
Ever. Under any circumstances. For any reason.

If someone asks for your seed phrase:
They are a scammer. Full stop.
```

---

### Scam 4 — Pump and Dump Low Volume Markets

```
How it works:
Scammer identifies low volume market ($3K total)
Buys heavily to move price
Creates appearance of momentum
Others follow the movement
Scammer sells at top
Price collapses
Followers left with worthless position

How to identify:
Sudden large price movement in low volume market
Someone tips you about a "sure thing" market
Social media hype around obscure market
Volume spikes without news catalyst

The fix:
Only trade markets with $50K+ volume
Ignore tips from strangers about specific markets
Price movements in low volume = manipulation risk
```

---

### Scam 5 — Fake Alpha Groups

```
How it works:
Telegram/Discord group claims to have
"insider information" on Polymarket outcomes
Charges ₹500-5000/month for "signals"
Signals are random or deliberately wrong
(Sometimes deliberately wrong to fade their own calls)

Why it works:
Prediction markets feel like they need insider info
Past "wins" shared as proof (losses hidden)
Social proof from fake members

The reality:
No legitimate information advantage is sold in groups
Real edge comes from your own research
Anyone selling "guaranteed" prediction market signals
is extracting money from you, not sharing edge

The fix:
Build your own research process
See: 07-quant-mindset.md Part 7
No shortcut replaces genuine domain knowledge
```

---

### Scam 6 — Fake Airdrop / Bonus Offers

```
How it works:
"Polymarket is giving 500 USDC to new users"
"Connect wallet to claim your trading bonus"
You connect wallet to malicious site
Site requests token approval
Wallet drained

How to identify:
Polymarket does not run unsolicited airdrops
Offers arriving via DM, ad, or random post = fake
Always verify on official polymarket.com directly

The fix:
Never click links in DMs related to crypto bonuses
Check official Polymarket Twitter for any real offers
When in doubt = do not connect wallet
```

---

### Scam 7 — AlchemyPay / Payment Page Fraud

```
How it works:
Scammer creates fake AlchemyPay payment page
Sends you link instead of going through Bitget
You pay to fake UPI
No crypto received

How to identify:
Real AlchemyPay flow = comes from INSIDE Bitget app
URL = cash.inrapidlink.com (official)
Has countdown timer
Has UTR input field
Has PhonePe/Paytm buttons

Fake page signs:
→ Link sent via chat or message
→ No timer
→ Asks for unusual information
→ URL does not match official domain

The fix:
Always initiate payment from INSIDE Bitget app
Never follow external links for payment
```

---

## Part 3 : Security Checklist

### Wallet Security
```
✅ Never share seed phrase with anyone
✅ Store seed phrase offline (paper, metal)
✅ Never type seed phrase into any website
✅ Use hardware wallet for large amounts
✅ Separate wallet for Polymarket trading
✅ Never connect wallet to unknown sites
```

### Trading Security
```
✅ Bookmark polymarket.com, always use bookmark
✅ Verify URL before every wallet connection
✅ Only pay P2P via details inside exchange app
✅ Never follow crypto links from DMs or ads
✅ Verify any "support" contact via official channels
✅ Check market volume before entering position
```

### Account Security
```
✅ Enable 2FA on all exchange accounts
✅ Use unique strong password per platform
✅ Never access accounts on public WiFi
✅ Use VPN on untrusted networks
✅ Regularly check active sessions on exchanges
```

---

## Part 4 : If You Get Scammed

### Immediate Steps
```
Step 1 → Stop all transactions immediately
Step 2 → Move remaining funds to new wallet
Step 3 → Revoke token approvals on revoke.cash
Step 4 → Document everything (screenshots, tx hashes)
Step 5 → Report to platform (Binance, Polymarket)
Step 6 → Report to cybercrime.gov.in (India)
```

### Reality Check
```
Crypto transactions are irreversible
Recovery of scammed funds = extremely rare
Prevention is the only reliable protection
If it sounds too good to be true = it is
```

---

## Quick Reference

```
╔══════════════════════════════════════════════════╗
║           NEVER DO THESE THINGS                  ║
╠══════════════════════════════════════════════════╣
║ Share your seed phrase with anyone               ║
║ Pay P2P via chat-shared UPI details              ║
║ Bet BTC 5 minute markets                         ║
║ Chase losses by increasing bet size              ║
║ Bet more than 20% of balance per trade           ║
║ Buy markets priced at 99¢                        ║
║ Trade low volume markets under $20K              ║
║ Connect wallet to links from DMs or ads          ║
║ Buy "prediction market signals" from anyone      ║
║ Hold through 100%+ profit out of greed           ║
╚══════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════╗
║           ALWAYS DO THESE THINGS                 ║
╠══════════════════════════════════════════════════╣
║ Use BASE or Polygon network (never ETH mainnet)  ║
║ Verify URL before wallet connection              ║
║ Pay only via details shown inside exchange app   ║
║ Sell immediately at 100%+ profit                 ║
║ Read resolution criteria before every bet        ║
║ Stop trading after hitting daily loss limit      ║
║ Keep seed phrase offline and private             ║
║ Check market volume before entering              ║
║ Calculate edge before every bet                  ║
║ Log every trade for review                       ║
╚══════════════════════════════════════════════════╝
```

---

## Next Steps

| I want to... | Go to... |
|---|---|
| Build a trading bot | [bots/README.md](../bots/README.md) |
| Learn quant mindset | [07-quant-mindset.md](07-quant-mindset.md) |
| Understand profit math | [04-profit-loss-calc.md](04-profit-loss-calc.md) |
| India-specific safety | [india-specific/p2p-safety.md](../india-specific/p2p-safety.md) |

---

*Every scam works once. Every mistake teaches once. Neither needs to happen to you.*