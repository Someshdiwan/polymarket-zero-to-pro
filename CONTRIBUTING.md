# Contributing to polymarket-zero-to-pro

> This project is built from real trading experience. Contributions that add genuine value — real examples, working code, honest analysis — are welcome. Quality over quantity, always.

---

## Ways to Contribute

```
1. Fix errors in existing docs or code
2. Add a new example (real trade walkthrough)
3. Build a script or bot feature from the roadmap
4. Translate docs to another language
5. Report bugs in scripts or bots
6. Suggest improvements via Issues
```

---

## Before You Start

### Read These First

```
ROADMAP.md        — Check if your idea is already planned
docs/             — Understand the existing content standard
examples/         — See the format and depth expected
```

### Check for Existing Issues

```
github.com/yourusername/polymarket-zero-to-pro/issues

If your contribution is already being worked on = comment to collaborate
If not = open an issue to claim it before building
```

---

## Contribution Standards

### For Documentation

**Tone**

```
✅ Professional, direct, finance-respecting
✅ Real numbers, real examples
✅ Honest about risk and losses
❌ Beginner-dumbed-down language
❌ Hype or "get rich quick" framing
❌ Emojis in headers or section titles
```

**Structure**

```
✅ Follow existing doc format (see any docs/ file)
✅ Start with a clear one-line description quote
✅ Use Parts (Part 1, Part 2...) for long docs
✅ End with Quick Reference table and Next Steps
✅ End with an italic closing line
```

**Content Rules**

```
✅ Cite real market examples with real numbers
✅ Include both winning and losing scenarios
✅ Show the math, not just the conclusion
✅ Be honest when something is risky or uncertain
❌ Do not recommend specific trades or outcomes
❌ Do not include referral links or promotions
```

---

### For Code (Scripts and Bots)

**Standards**

```python
# Every file must have:
# 1. Module docstring with description and usage examples
# 2. Docstrings on every function
# 3. Error handling with meaningful messages
# 4. CLI with argparse (no bare scripts)
# 5. Colorama for terminal output
# 6. DRY_RUN default = True for any trading code
```

**Testing**

```
Before submitting:
✅ Script runs without errors: python script.py --help
✅ All CLI flags work as documented
✅ Dry run mode works and produces clear output
✅ No hardcoded API keys or credentials
✅ .env.example updated if new env vars added
```

**Style**

```
Follow PEP 8
Max line length: 100 characters
Use f-strings (not .format() or %)
Group imports: stdlib → third party → local
```

---

## Pull Request Process

### Step 1 — Fork and Branch

```bash
git fork https://github.com/yourusername/polymarket-zero-to-pro
git checkout -b feature/your-contribution-name

# Branch naming conventions:
# docs/add-arbitrage-guide
# scripts/add-news-alert
# fix/portfolio-tracker-csv-export
# examples/ipl-betting-strategy
```

### Step 2 — Build Your Contribution

```
Follow the standards above
Test locally before committing
Keep commits focused — one change per commit
```

### Step 3 — Update Relevant Files

```
New doc added?        → Mark ✅ in ROADMAP.md
New env var added?    → Update bots/starter-bot/.env.example
New dependency added? → Update relevant requirements.txt
```

### Step 4 — Submit PR

```
Title format:
  [docs]    Add arbitrage strategy guide
  [scripts] Add news_alert.py
  [fix]     Fix portfolio tracker CSV headers
  [examples] Add IPL betting case study

PR description must include:
  → What this adds or fixes
  → How to test it
  → Reference to roadmap item if applicable
```

---

## Issues

### Reporting a Bug

```
Title: [bug] Brief description

Include:
  → Which file / script
  → Exact command you ran
  → What happened vs what you expected
  → Python version and OS
```

### Requesting a Feature

```
Title: [feature] Brief description

Include:
  → What problem it solves
  → Which roadmap phase it fits
  → Any implementation ideas
```

---

## What We Accept and Do Not Accept

### Accept ✅

```
Real trade examples (your own, anonymised if preferred)
Strategy guides based on documented edge
Scripts that provide genuine utility
Bug fixes and improvements to existing code
Translations of existing docs
Clarifications and corrections
```

### Do Not Accept ❌

```
Referral links or affiliate promotions
Unrealistic return claims or "get rich quick" framing
Strategies without honest risk disclosure
Code that accesses private data without consent
AI-generated content without human review
```

---

## Code of Conduct

```
Be direct and honest
Respect other contributors' work
Credit sources and original authors
No spam, self-promotion, or off-topic content
Disagree with data, not arguments
```

---

## Recognition

Contributors are credited in commit history and `CONTRIBUTORS.md` after first merged PR.

---

*Good contributions make the next trader better. That is the only metric that matters here.*
