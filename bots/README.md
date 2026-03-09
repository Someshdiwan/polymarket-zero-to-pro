# Polymarket Trading Bots

> Automated trading on Polymarket is not about removing human judgment it is about executing that judgment faster, more consistently, and without emotional interference. These bots are tools to operationalise your edge, not replace it.

---

## Structure

```
bots/
├── README.md              ← Overview + learning order + golden rules
├── resources.md           ← Curated repos, APIs, tools, learning path
├── starter-bot/
│   ├── main.py            ← CLI bot: markets, positions, interactive trade
│   ├── requirements.txt
│   └── .env.example       ← All config vars documented
└── ai-strategy-bot/
    ├── main.py            ← Scan + schedule + auto-execute + performance report
    ├── news_fetcher.py    ← NewsAPI + query builder + fallback handling
    ├── market_analyzer.py ← Claude AI probability estimation + edge + EV
    └── requirements.txt
```

---

## Which Bot Should You Use?

```
New to Polymarket API?
→ Start with starter-bot
→ Learn the API, place test trades
→ Understand market data structure

Comfortable with API?
→ Move to ai-strategy-bot
→ Automate news fetching and edge detection
→ Let AI compare probabilities to market prices
```

---

## Prerequisites

```
Python 3.10+
Polymarket account with API keys
Funded Polymarket wallet (USDC on Polygon)
Basic Python knowledge
```

---

## Getting API Keys

```
Step 1 → Go to polymarket.com
Step 2 → Connect wallet
Step 3 → Profile → API Management
Step 4 → Create API key
Step 5 → Save three values:
         API_KEY
         API_SECRET
         API_PASSPHRASE
```

> ⚠️ Never commit API keys to GitHub
> Always use .env files (already in .gitignore)

---

## Golden Rules for Bot Trading

```
1. Always dry-run first (--dry-run flag)
2. Never automate more than $5 per trade
3. Set daily loss limits in code
4. Log every action to file
5. Monitor actively for first week
6. Bots amplify your edge AND your mistakes
```

---

## Recommended Learning Order

```
Day 1-3   → Read Polymarket CLOB API docs
Day 4-7   → Run starter-bot in dry-run mode
Day 8-14  → Run starter-bot with $1 real trades
Day 15-21 → Set up ai-strategy-bot dry-run
Day 22-30 → Run ai-strategy-bot with $1-2 trades
Day 30+   → Refine strategy based on trade log
```

---

## Official API Documentation

```
CLOB API:    https://docs.polymarket.com
GitHub:      https://github.com/Polymarket
py-clob:     https://github.com/Polymarket/py-clob-client
```

---

*A bot without edge is just a faster way to lose money.*