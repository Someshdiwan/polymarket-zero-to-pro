# Kalshi vs Polymarket Platform Comparison

> Both platforms offer prediction market trading but operate under fundamentally different regulatory frameworks, target different user bases, and provide distinct advantages depending on your location, capital, and trading goals. This document breaks down every meaningful difference.

---

## At a Glance

```
Kalshi     = US-regulated, compliant, direct bank access
             Limited internationally, fewer markets

Polymarket = Global, crypto-native, more markets
             Unregulated, requires crypto infrastructure
```

---

## Part 1 : Regulatory Status

### Kalshi
```
Regulator:  CFTC (Commodity Futures Trading Commission)
Status:     Fully licensed Designated Contract Market (DCM)
Launched:   2021
Legal in:   USA (primary), select other jurisdictions
Meaning:    Same regulatory tier as CME, CBOE
            Your funds are legally protected
            Platform has legal obligations to users
```

### Polymarket
```
Regulator:  None (offshore)
Status:     Decentralised prediction market
Launched:   2020
Legal in:   Global grey area
            Not explicitly banned in most countries
            Not explicitly permitted either
Meaning:    No regulatory protection
            Smart contracts protect funds (not laws)
            Settled 2022 CFTC fine of $1.4M
```

### Why Regulation Matters
```
Kalshi (regulated):
→ Funds protected by US financial law
→ Platform cannot disappear with your money
→ Legal recourse if dispute arises
→ Tax reporting infrastructure built in

Polymarket (unregulated):
→ Smart contract holds funds (trustless)
→ No legal recourse if platform issues arise
→ No formal tax reporting
→ Accessible globally without restriction
```

---

## Part 2 : Deposit and Withdrawal

### Kalshi

| Method | Availability |
|---|---|
| US Bank Transfer (ACH) | ✅ Direct |
| Wire Transfer | ✅ Direct |
| Debit Card | ✅ Direct |
| PayPal | ✅ Direct |
| Crypto | ❌ Not supported |
| UPI / Indian methods | ❌ Not supported |

```
Withdrawal: Direct to US bank account
Timeline:   1-3 business days
Currency:   USD only
KYC:        Strict US identity verification required
            (SSN, US address, government ID)
```

### Polymarket

| Method | Availability |
|---|---|
| USDC (Polygon) | ✅ Primary method |
| ETH (Base/Polygon) | ✅ Supported |
| Binance Connect | ✅ Integrated |
| UPI via AlchemyPay | ✅ Via Bitget/Binance |
| Direct bank transfer | ❌ Not supported |
| Credit/Debit card | ⚠️ Via third party only |

```
Withdrawal: Crypto wallet → Exchange → Bank
Timeline:   Crypto transfer instant,
            Exchange to bank 1-3 days
Currency:   USDC (stable, always $1)
KYC:        Basic (email + wallet)
            No government ID required for trading
```

### For Indian Users Specifically

```
Kalshi:
→ Requires US bank account and SSN
→ Practically inaccessible from India
→ Cannot deposit INR
→ Not recommended for Indian traders

Polymarket:
→ Accessible from India
→ INR → ETH via Bitget + AlchemyPay UPI
→ Withdrawal via Binance P2P → INR
→ Full flow documented in india-specific/ folder
→ Recommended for Indian traders ✅
```

---

## Part 3 : Market Availability

### Kalshi Markets
```
✅ Finance & Economics (Fed, CPI, jobs data)
✅ Politics (US elections, legislation)
✅ Weather (temperature, precipitation)
✅ Sports (major US leagues)
✅ Technology milestones
✅ Entertainment (awards, box office)
❌ Geopolitics (war, strikes, conflicts)
❌ Crypto price markets
❌ International politics (non-US)
```

### Polymarket Markets
```
✅ Geopolitics (best in class)
✅ International politics (global coverage)
✅ Crypto (prices, protocol events, regulation)
✅ Finance & Economics
✅ Sports (global coverage)
✅ Science & Climate
✅ Culture & Entertainment
✅ BTC/ETH short-term price markets
❌ Weather (not available)
```

### Market Depth Comparison

| Category | Kalshi | Polymarket | Winner |
|---|---|---|---|
| US Politics | Deep | Moderate | Kalshi |
| Geopolitics | Minimal | Very Deep | Polymarket |
| Crypto | None | Deep | Polymarket |
| Economics/Fed | Very Deep | Moderate | Kalshi |
| Weather | Yes | No | Kalshi |
| International | Minimal | Deep | Polymarket |
| Sports (US) | Deep | Moderate | Kalshi |
| Sports (Global) | Minimal | Deep | Polymarket |
| Total Markets | ~100-200 | ~1000+ | Polymarket |

---

## Part 4 : Fees and Costs

### Kalshi
```
Trading fee:    0.05% - 0.1% per trade
Withdrawal fee: None
Deposit fee:    None
Spread:         Tight on high volume markets
```

### Polymarket
```
Trading fee:    0% (no platform fee)
Gas fee:        <$0.01 on Polygon/Base
Deposit fee:    Depends on method
                Bitget + AlchemyPay = ₹4
                Binance card = ₹40
Withdrawal fee: Exchange fees apply
Spread:         Wider on low volume markets
```

### Total Cost Comparison for $100 Trade
```
Kalshi:
Entry fee    = $0.05 - $0.10
Exit fee     = $0.05 - $0.10
Total        = ~$0.20 round trip

Polymarket:
Entry gas    = $0.01
Exit gas     = $0.01
Platform fee = $0.00
Total        = ~$0.02 round trip

Winner: Polymarket (significantly cheaper)
```

---

## Part 5 : Liquidity and Volume

### Kalshi
```
Total platform volume: Growing rapidly post-CFTC win
Major markets:         $500K - $5M per market
Minor markets:         $10K - $100K
Institutional traders: Yes (growing)
Market makers:         Professional firms
```

### Polymarket
```
Total platform volume: $1B+ monthly (as of 2026)
Major markets:         $1M - $10M per market
Minor markets:         $1K - $50K
Institutional traders: Yes (significant)
Market makers:         Automated + manual
```

### Impact on Trading
```
Higher liquidity = tighter spreads = better prices
Both platforms have sufficient liquidity for
retail traders betting under $1000 per position

For large positions ($10K+):
Polymarket has deeper liquidity on most markets
Kalshi has deeper liquidity on US economics markets
```

---

## Part 6 : User Experience

### Kalshi
```
Interface:    Clean, professional, TradingView-like
Mobile app:   Yes (iOS and Android)
Web app:      Yes
Charts:       Good
Order types:  Market, Limit
API:          Yes (developer access)
Onboarding:  Longer (KYC intensive)
```

### Polymarket
```
Interface:    Modern, news-oriented layout
Mobile app:   No dedicated app (mobile browser)
Web app:      Yes (primary)
Charts:       Basic price history
Order types:  Market, Limit
API:          Yes (CLOB API, well documented)
Onboarding:  Fast (wallet connect, no heavy KYC)
```

---

## Part 7 : Trust and Security

### Kalshi
```
Fund safety:    CFTC regulated = legal protection
Counterparty:   Kalshi as central counterparty
Hack risk:      Traditional web2 security
Fraud risk:     Low (regulated entity)
Track record:   Clean since 2021
```

### Polymarket
```
Fund safety:    Smart contract (trustless)
                Funds held on Polygon blockchain
                Not custodied by Polymarket
Counterparty:   Smart contract (no human counterparty)
Hack risk:      Smart contract risk (audited)
Fraud risk:     Low (decentralised)
Track record:   One regulatory fine (2022, resolved)
```

### Which is Safer?
```
For regulatory safety:   Kalshi ✅
For custodial safety:    Polymarket ✅
                         (you control your funds)

Polymarket paradox:
→ Less regulatory protection
→ But more actual fund control
→ No single company can freeze your assets
→ Smart contract is transparent and auditable
```

---

## Part 8 : Tax Implications

### Kalshi (US Users)
```
1099 forms issued automatically
Gains treated as Section 1256 contracts
60/40 tax treatment (60% long-term, 40% short-term)
Clear legal framework
Straightforward reporting
```

### Polymarket (India)
```
Crypto asset tax = 30% flat (no deductions)
1% TDS on transfers above threshold
No official guidance specific to prediction markets
Treated as cryptocurrency gains
Self-reporting required
No automatic tax forms
```

### India Tax Reality
```
Every winning trade = 30% tax liability
₹10,000 profit → ₹3,000 tax owed
Must be self-reported in ITR
Keep records of all transactions
Consult a CA familiar with crypto taxation
```

---

## Part 9 : Which Platform for Which Trader

### Choose Kalshi If:
```
✅ You are based in the United States
✅ You want regulatory protection
✅ You trade US economics / Fed markets heavily
✅ You want direct bank account integration
✅ You prefer traditional finance infrastructure
✅ You trade weather markets
✅ Compliance and tax reporting matter to you
```

### Choose Polymarket If:
```
✅ You are based in India or outside the US
✅ You want access to geopolitics markets
✅ You want crypto integration
✅ You want more market variety
✅ You are comfortable with crypto infrastructure
✅ You want lower fees
✅ You want self-custody of funds
```

### Use Both If:
```
✅ You trade US economics → Kalshi
✅ You trade geopolitics / crypto → Polymarket
✅ You want regulatory + market diversity
✅ You have both USD bank and crypto wallet
```

---

## Part 10 — Side by Side Summary

| Feature | Kalshi | Polymarket |
|---|---|---|
| Regulation | CFTC ✅ | None ⚠️ |
| India accessible | ❌ | ✅ |
| INR deposit | ❌ | ✅ Via crypto |
| Direct bank withdrawal | ✅ | ❌ |
| Market count | ~200 | ~1000+ |
| Geopolitics | Minimal | Excellent |
| Crypto markets | None | Excellent |
| Weather markets | Yes | No |
| Fees | Low | Very low |
| Mobile app | Yes | Browser only |
| Fund custody | Kalshi | You (wallet) |
| Tax reporting | Automatic | Manual |
| KYC requirement | Strict (US ID) | Light |
| Recommended for India | ❌ | ✅ |

---

## Quick Reference

```
╔══════════════════════════════════════════════════╗
║           PLATFORM SELECTION SUMMARY             ║
╠══════════════════════════════════════════════════╣
║ India-based trader      → Polymarket             ║
║ US-based trader         → Kalshi primary         ║
║ Geopolitics focus       → Polymarket             ║
║ US economics focus      → Kalshi                 ║
║ Crypto markets          → Polymarket             ║
║ Regulatory safety       → Kalshi                 ║
║ Fund self-custody        → Polymarket            ║
║ Maximum market access   → Both                   ║
╚══════════════════════════════════════════════════╝
```

---

## Next Steps

| I want to... | Go to... |
|---|---|
| Avoid mistakes and scams | [10-mistakes-and-scams.md](10-mistakes-and-scams.md) |
| Learn quant mindset | [07-quant-mindset.md](07-quant-mindset.md) |
| Understand market types | [08-market-types.md](08-market-types.md) |
| Build a trading bot | [bots/README.md](../bots/README.md) |

---

*Two platforms. Different strengths. The best traders use both.*