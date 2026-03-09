# Auto Resolution  How Markets Settle

> Market resolution is the mechanism by which Polymarket determines the winning outcome, distributes payouts, and closes positions. Understanding this process eliminates uncertainty and builds confidence in holding positions to expiry.

---

## Core Concept

```
Every market has a resolution date and criteria
When that date passes → Polymarket verifies outcome
Winning shares = $1.00 each (automatic)
Losing shares  = $0.00 each (automatic)
No manual action required from the trader
```

---

## Part 1 : The Resolution Process

### Step by Step
```
Step 1 → Market deadline passes
              ↓
Step 2 → Polymarket resolution team reviews outcome
         (Using verified news sources, APIs, official data)
              ↓
Step 3 → Outcome confirmed on-chain (blockchain)
              ↓
Step 4 → Smart contract executes automatically
              ↓
Step 5 → Winning shares converted to $1.00 USDC each
              ↓
Step 6 → Losing shares converted to $0.00
              ↓
Step 7 → USDC credited to your Cash balance
              ↓
Step 8 → You see updated portfolio balance ✅
```

### Does it require you to be online?
```
Resolution    → No ✅ (happens automatically)
Payout credit → No ✅ (appears in balance)
Withdrawal    → Yes ✅ (manual action needed)
```

---

## Part 2 : Resolution Sources

### How Polymarket Verifies Outcomes

| Market Type | Verification Source |
|---|---|
| Politics | Official government announcements |
| Sports | Official league/tournament data |
| Crypto prices | Chainlink oracles, exchanges |
| Economic data | Federal Reserve, official reports |
| Geopolitics | Major credible news sources |
| Weather | Official meteorological agencies |

### What is an Oracle?
```
Oracle = trusted data source connected to blockchain

Real world event happens
      ↓
Oracle confirms it on-chain
      ↓
Smart contract reads oracle data
      ↓
Market resolves automatically

No human can manipulate this process
```

---

## Part 3 : Resolution Scenarios

### Scenario A : Clear Outcome ✅
```
Market: "Will US strike Iran on March 2?"
Outcome: Strike confirmed by multiple news sources

Resolution: YES wins
All YES shares → $1.00 each
All NO shares  → $0.00 each
Timeline: Within hours of event
```

### Scenario B : No Event (Expired) ✅
```
Market: "Will US strike Iran on March 2?"
Outcome: March 2 passes, no strike

Resolution: NO wins
All NO shares  → $1.00 each
All YES shares → $0.00 each
Timeline: Shortly after midnight of deadline
```

### Scenario C : Disputed Outcome ⚠️
```
Market: Ambiguous result, conflicting sources

Resolution: Delayed pending review
Polymarket team investigates
Community can flag disputes
Timeline: Can take days to weeks
Your funds: Safe, locked until resolved
```

### Scenario D : Market Cancelled 🔄
```
Reason: Event never happened, question invalid,
        or unresolvable ambiguity

Resolution: All traders refunded fully
You get back exactly what you invested
Timeline: Varies
```

---

## Part 4 : Payout Calculation at Resolution

### Formula
```
Payout = Shares owned × $1.00 (if winning side)
Payout = Shares owned × $0.00 (if losing side)
```

### Real Example
```
You bought NO at 2¢ with $10
Shares = $10 ÷ $0.02 = 500 shares

Market resolves → NO wins

Payout = 500 × $1.00 = $500.00
Auto credited to Cash balance ✅
Profit = $500 - $10 = $490
Return = 4900%
```

---

## Part 5 : Resolution Timeline

### How Long Does It Take?

| Event Type | Typical Resolution Time |
|---|---|
| BTC price markets | Minutes after expiry |
| Sports results | Hours after final whistle |
| Political events | Hours to 24 hours |
| Geopolitical events | Hours to 48 hours |
| Disputed markets | Days to weeks |
| Economic data | Hours after official release |

### What Happens to Your Money During Delay?
```
Funds are locked in smart contract
Cannot be stolen or manipulated
Safe until resolution completes
You can still sell on open market during delay
```

---

## Part 6 : Auto Resolve vs Manual Sell Comparison

| Factor | Auto Resolve | Manual Sell |
|---|---|---|
| Timing | After deadline | Anytime before deadline |
| Payout | $1.00 per share (if win) | Current market price |
| Action needed | None | Click Sell |
| Works offline | Yes ✅ | No |
| Risk | Market resolves against you | Lock in current profit/loss |
| Best used when | Highly confident | Profit showing, uncertain outcome |

### When Auto Resolve Pays More
```
You bought NO at 5¢
Current price = 20¢ (sell value = 4x)
You think NO will win

Sell now   → 4x return
Hold       → 20x return (if NO wins)

Auto resolve is better when confidence is high
```

### When Manual Sell Pays More
```
You bought NO at 5¢
Current price = 40¢ (sell value = 8x)
News just shifted strongly toward YES

Sell now   → 8x return (locked in)
Hold       → potentially 0x if YES wins

Manual sell is better when news shifts against you
```

---

## Part 7 : The Redeem Function

### What is Redeem?
```
Some markets require manual redemption
After resolution → shares show as winning
But money not auto credited

You must click "Redeem" to claim
```

### When Does This Happen?
```
Older markets on Polymarket
Markets using certain smart contracts
Typically shown as "Redeem" button in Positions tab
```

### How to Redeem
```
Portfolio → Positions tab
→ Look for "Redeem" button on resolved market
→ Click Redeem
→ USDC credited to balance
```

> ⚠️ Always check Positions tab after a market resolves
> You may have unclaimed winnings sitting there

---

## Part 8 : Multi-Date Market Resolution

### How Each Date Resolves Independently
```
Market: "US/Israel strikes Iran on...?"

March 2  → Resolves at end of March 2
March 3  → Resolves at end of March 3
March 4  → Resolves at end of March 4

Each date = separate contract
Each resolves independently
Winning one does NOT affect others
```

### Example
```
You hold:
→ NO on March 2 (strike happened = you lose)
→ NO on March 5 (no strike = you win)

March 2 resolves → your March 2 NO = $0
March 5 resolves → your March 5 NO = $1 per share

Independent outcomes, independent payouts
```

---

## Part 9 : What Could Go Wrong?

### Delayed Resolution
```
Problem: Market takes days to resolve
Impact:  Funds locked longer than expected
Action:  Wait — your position is safe
```

### Wrong Resolution
```
Problem: Market resolved incorrectly
Impact:  You lost but should have won
Action:  File dispute via Polymarket support
         Community governance can overturn
```

### Market Cancelled
```
Problem: Market cancelled before resolution
Impact:  You don't win your expected payout
Action:  Full refund automatically credited
```

### Low Liquidity at Resolution
```
Problem: You want to sell before resolution
         but nobody is buying
Impact:  Stuck holding until resolution
Action:  Only bet high-volume markets ($100K+)
```

---

## Part 10 : Key Rules to Remember

```
╔══════════════════════════════════════════════╗
║         AUTO RESOLUTION RULES                ║
╠══════════════════════════════════════════════╣
║ Resolution is automatic — no action needed   ║
║ Winning payout = $1.00 per share             ║
║ Losing payout  = $0.00 per share             ║
║ Check Positions tab for Redeem button        ║
║ Disputed markets can take days               ║
║ Cancelled markets = full refund              ║
║ Multi-date markets resolve independently     ║
║ Funds safe in smart contract during delay    ║
╚══════════════════════════════════════════════╝
```

---

## Next Steps

| I want to... | Go to... |
|---|---|
| Learn BTC candle strategy | [06-candlestick-strategy.md](06-candlestick-strategy.md) |
| Think like a quant trader | [07-quant-mindset.md](07-quant-mindset.md) |
| Understand profit math | [04-profit-loss-calc.md](04-profit-loss-calc.md) |
| Avoid common mistakes | [10-mistakes-and-scams.md](10-mistakes-and-scams.md) |

---

*Resolution is trustless by design the blockchain settles what humans dispute.*