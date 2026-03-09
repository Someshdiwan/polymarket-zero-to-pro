# Bot Resources & Open Source Repos

> A curated list of open source tools, libraries, and repositories for building Polymarket trading bots. Verified and ranked by quality.

---

## Official Polymarket Repositories

| Repo | Description | Language |
|---|---|---|
| [py-clob-client](https://github.com/Polymarket/py-clob-client) | Official Python client for the CLOB API | Python |
| [polymarket-agents](https://github.com/Polymarket/agents) | Official AI agent framework by Polymarket | Python |
| [clob-client](https://github.com/Polymarket/clob-client) | Official TypeScript CLOB client | TypeScript |
| [order-utils](https://github.com/Polymarket/order-utils) | Utilities for signing and hashing orders | TypeScript |
| [python-order-utils](https://github.com/Polymarket/python-order-utils) | Python version of order utilities | Python |

---

## Community Bots (Open Source)

| Repo | Description | Stars | Language |
|---|---|---|---|
| [polymarket-trading-bot](https://github.com/discountry/polymarket-trading-bot) | Simple starter bot, good for learning | ⭐ | Python |
| [Polymarket-Trading-Bot](https://github.com/dylanpersonguy/Polymarket-Trading-Bot) | Advanced bot with strategy modules | ⭐⭐ | Python |
| [polymarket-bot](https://github.com/frederik-uni/polymarket-bot) | Lightweight market scanner | ⭐ | Python |

> ⚠️ Always audit community code before using with real funds
> Never run unknown code with your private key loaded

---

## API Documentation

| Resource | URL |
|---|---|
| CLOB API Docs | https://docs.polymarket.com |
| Gamma API (market data) | https://gamma-api.polymarket.com |
| CLOB API base URL | https://clob.polymarket.com |
| Strapi API (markets) | https://strapi-matic.poly.market |

---

## Essential Python Libraries

```
py-clob-client    Official Polymarket Python SDK
anthropic         Claude AI API client
web3              Ethereum/Polygon blockchain interaction
python-dotenv     Environment variable management
requests          HTTP requests
schedule          Job scheduling
colorama          Colored terminal output
tabulate          Table formatting in terminal
```

Install all at once:
```bash
pip install py-clob-client anthropic web3 python-dotenv requests schedule colorama tabulate
```

---

## News & Data APIs

| API | Free Tier | Best For |
|---|---|---|
| [NewsAPI](https://newsapi.org) | 100 req/day | General news fetching |
| [GDELT Project](https://gdeltproject.org) | Unlimited | Geopolitical event data |
| [Alpha Vantage](https://alphavantage.co) | 25 req/day | Financial data |
| [CryptoCompare](https://cryptocompare.com) | 100K req/month | Crypto price data |
| [Chainlink](https://chain.link) | On-chain | Decentralised price oracles |

---

## AI APIs for Probability Estimation

| API | Model | Cost per 1K tokens |
|---|---|---|
| [Anthropic](https://anthropic.com) | Claude Sonnet | ~$0.003 |
| [OpenAI](https://openai.com) | GPT-4o | ~$0.005 |
| [Groq](https://groq.com) | Llama 3.1 | Free tier available |
| [Perplexity](https://perplexity.ai) | Sonar | ~$0.001 (includes search) |

> Perplexity Sonar is worth exploring — it combines web search + LLM in one API call,
> useful for combining news fetching and analysis into a single request.

---

## Blockchain Tools

| Tool | URL | Purpose |
|---|---|---|
| PolygonScan | https://polygonscan.com | Track transactions on Polygon |
| Revoke.cash | https://revoke.cash | Revoke token approvals |
| DeBank | https://debank.com | Portfolio tracker across chains |
| Tenderly | https://tenderly.co | Simulate transactions before sending |

---

## Learning Resources

### Polymarket Specific
```
Official Blog:    https://polymarket.com/blog
API Docs:         https://docs.polymarket.com
Discord:          https://discord.gg/polymarket
Twitter/X:        https://twitter.com/polymarket
```

### Prediction Markets Theory
```
Forecasting Primer:   https://www.gjopen.com/faq
Superforecasting:     Philip Tetlock (book)
Calibration training: https://www.calibratedhive.com
Metaculus:            https://metaculus.com (practice forecasting)
```

### Python Trading
```
Algorithmic Trading with Python: Chris Conlan (book)
QuantLib:                        https://quantlib.org
Backtrader:                      https://backtrader.com (backtesting)
```

---

## Useful One-Liners

### Fetch all active markets
```python
from py_clob_client.client import ClobClient
client = ClobClient("https://clob.polymarket.com", chain_id=137)
markets = client.get_markets()
print(f"{len(markets)} markets found")
```

### Get market by condition ID
```python
market = client.get_market("0xabc123...")
print(market["question"], market["outcomePrices"])
```

### Check your balance
```python
balance = client.get_balance()
print(f"Balance: ${balance} USDC")
```

---

## Security Resources

| Tool | Purpose |
|---|---|
| [Revoke.cash](https://revoke.cash) | Remove wallet approvals |
| [WalletGuard](https://walletguard.app) | Browser extension for transaction safety |
| [Tenderly](https://tenderly.co) | Simulate transactions before executing |
| [CryptoScamDB](https://cryptoscamdb.org) | Check if a site is a known scam |

---

## Community & Discussion

```
Polymarket Discord:   https://discord.gg/polymarket
Polymarket Subreddit: https://reddit.com/r/polymarket
Manifold Markets:     https://manifold.markets (practice with fake money)
PredictIt:            https://predictit.org (US regulated, real money)
```

---

## Recommended Learning Path

```
Week 1  → Read all docs/ files in this repo
Week 2  → Set up starter-bot in dry-run mode
Week 3  → Study py-clob-client official examples
Week 4  → Set up ai-strategy-bot in dry-run mode
Week 5  → Paper trade, track predictions manually
Week 6  → First live trades ($1-2 per bet)
Month 2 → Refine strategy based on trade log data
Month 3 → Build custom modules for your edge categories
```

---

*The best bot is the one that implements your edge not someone else's.*