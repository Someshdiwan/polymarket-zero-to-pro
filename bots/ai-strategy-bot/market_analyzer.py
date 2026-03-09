"""
market_analyzer.py

Uses Claude AI to analyze Polymarket markets and identify edge opportunities.

Process:
1. Fetch market data from Polymarket
2. Fetch relevant news via news_fetcher.py
3. Send to Claude with structured prompt
4. Parse AI probability estimate
5. Calculate edge vs market price
6. Return actionable signals

Edge threshold: configurable via .env (default 10%)
"""

import os
import json
import logging
import anthropic
from dotenv import load_dotenv
from news_fetcher import fetch_news, build_news_query, format_news_for_ai

load_dotenv()
logger = logging.getLogger(__name__)

ANTHROPIC_API_KEY  = os.getenv("ANTHROPIC_API_KEY")
MIN_EDGE_THRESHOLD = float(os.getenv("MIN_EDGE_THRESHOLD", "0.10"))
MIN_MARKET_VOLUME  = float(os.getenv("MIN_MARKET_VOLUME", "50000"))


# AI Probability Estimator

def estimate_probability(market_question, market_rules, news_context, market_price):
    """
    Ask Claude to estimate the probability of a market resolving YES.

    Args:
        market_question: The market question string
        market_rules: Resolution criteria for the market
        news_context: Formatted news string from news_fetcher
        market_price: Current YES price in cents (0-100)

    Returns:
        Float between 0.0 and 1.0, or None if estimation failed
    """
    if not ANTHROPIC_API_KEY or ANTHROPIC_API_KEY == "your_anthropic_key_here":
        logger.error("ANTHROPIC_API_KEY not configured.")
        return None

    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    prompt = f"""You are a professional prediction market analyst with expertise in probability estimation.

Your task is to estimate the probability that the following market resolves YES.

MARKET QUESTION:
{market_question}

RESOLUTION CRITERIA:
{market_rules}

CURRENT MARKET PRICE:
YES is currently priced at {market_price}¢ (implying {market_price}% probability)

RECENT NEWS:
{news_context}

INSTRUCTIONS:
1. Analyse the question carefully against the resolution criteria
2. Consider the news context and what it implies
3. Apply base rates for this type of event
4. Consider what the market price might be missing
5. Provide your independent probability estimate

IMPORTANT:
- Respond with ONLY a JSON object in this exact format:
{{"probability": 0.XX, "confidence": "low|medium|high", "reasoning": "brief explanation"}}
- probability must be between 0.01 and 0.99
- Do not include any other text, preamble, or markdown
"""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=256,
            messages=[{"role": "user", "content": prompt}],
        )

        raw = message.content[0].text.strip()
        logger.debug(f"AI response: {raw}")

        # Parse JSON response
        result = json.loads(raw)

        probability = float(result.get("probability", 0))
        confidence  = result.get("confidence", "low")
        reasoning   = result.get("reasoning", "")

        # Validate range
        if not 0.01 <= probability <= 0.99:
            logger.warning(f"Probability {probability} out of range. Skipping.")
            return None

        logger.info(f"AI estimate: {probability:.1%} ({confidence} confidence)")
        logger.info(f"Reasoning: {reasoning}")

        return probability

    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse AI response as JSON: {e}")
        return None
    except anthropic.APIError as e:
        logger.error(f"Anthropic API error: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error in estimate_probability: {e}")
        return None



# Edge Calculator

def calculate_edge(ai_probability, market_price_cents):
    """
    Calculate edge between AI estimate and market price.

    Returns:
        dict with edge, direction, and recommendation
    """
    market_prob = market_price_cents / 100
    edge        = ai_probability - market_prob

    if edge > MIN_EDGE_THRESHOLD:
        direction      = "YES"
        recommendation = "BUY YES"
    elif edge < -MIN_EDGE_THRESHOLD:
        direction      = "NO"
        recommendation = "BUY NO"
        edge           = abs(edge)
    else:
        direction      = "NONE"
        recommendation = "SKIP"
        edge           = abs(edge)

    return {
        "edge":           edge,
        "direction":      direction,
        "recommendation": recommendation,
        "ai_probability": ai_probability,
        "market_prob":    market_prob,
    }


def calculate_ev(ai_probability, market_price_cents, stake):
    """Calculate expected value of a bet."""
    price         = market_price_cents / 100
    shares        = stake / price
    profit_if_win = shares - stake
    loss_if_lose  = stake

    return (ai_probability * profit_if_win) - ((1 - ai_probability) * loss_if_lose)


# Market Scanner

def analyze_market(market):
    """
    Full analysis pipeline for a single market.

    Args:
        market: Market dictionary from Polymarket API

    Returns:
        Analysis result dictionary or None if no signal
    """
    question   = market.get("question", "")
    rules      = market.get("description", "No rules provided")
    volume     = float(market.get("volume", 0))
    yes_price  = float(market.get("outcomePrices", [0.5])[0]) * 100
    market_id  = market.get("conditionId") or market.get("id")

    logger.info(f"Analyzing: {question[:60]}...")

    # Volume filter
    if volume < MIN_MARKET_VOLUME:
        logger.debug(f"Skipping low volume market: ${volume:,.0f}")
        return None

    # Skip near-resolved markets (>95¢ or <5¢)
    if yes_price > 95 or yes_price < 5:
        logger.debug(f"Skipping near-resolved market: YES at {yes_price:.1f}¢")
        return None

    # Fetch news
    query        = build_news_query(question)
    articles     = fetch_news(query, hours_back=48)
    news_context = format_news_for_ai(articles)

    # AI probability estimate
    ai_prob = estimate_probability(question, rules, news_context, yes_price)

    if ai_prob is None:
        logger.warning(f"Could not get AI estimate for: {question[:40]}")
        return None

    # Calculate edge
    edge_result = calculate_edge(ai_prob, yes_price)

    if edge_result["recommendation"] == "SKIP":
        logger.info(f"No edge found. Edge: {edge_result['edge']:.1%}")
        return None

    # Calculate EV
    ev = calculate_ev(
        ai_prob if edge_result["direction"] == "YES" else 1 - ai_prob,
        yes_price if edge_result["direction"] == "YES" else 100 - yes_price,
        stake=2.0,
    )

    result = {
        "market_id":      market_id,
        "question":       question,
        "direction":      edge_result["direction"],
        "recommendation": edge_result["recommendation"],
        "yes_price":      yes_price,
        "no_price":       100 - yes_price,
        "ai_probability": ai_prob,
        "market_prob":    edge_result["market_prob"],
        "edge":           edge_result["edge"],
        "ev_on_2usd":     ev,
        "volume":         volume,
        "articles_found": len(articles),
    }

    logger.info(f"SIGNAL: {edge_result['recommendation']} | Edge: {edge_result['edge']:.1%} | EV: ${ev:.2f}")

    return result


def scan_markets(markets):
    """
    Scan a list of markets and return all signals found.

    Args:
        markets: List of market dicts from Polymarket API

    Returns:
        List of analysis results with edge above threshold
    """
    signals = []

    logger.info(f"Scanning {len(markets)} markets for edge...")

    for i, market in enumerate(markets, 1):
        logger.info(f"Progress: {i}/{len(markets)}")
        result = analyze_market(market)
        if result:
            signals.append(result)

    # Sort by edge descending
    signals.sort(key=lambda x: x["edge"], reverse=True)

    logger.info(f"Found {len(signals)} signals above {MIN_EDGE_THRESHOLD:.0%} threshold")

    return signals


# Signal Display

def display_signals(signals):
    """Print signals in readable format."""
    if not signals:
        print("\nNo edge opportunities found in current markets.")
        return

    print(f"\n{'='*70}")
    print(f"EDGE OPPORTUNITIES FOUND: {len(signals)}")
    print(f"{'='*70}\n")

    for i, s in enumerate(signals, 1):
        print(f"Signal #{i}")
        print(f"  Question:    {s['question'][:65]}...")
        print(f"  Action:      {s['recommendation']}")
        print(f"  Market:      YES {s['yes_price']:.1f}¢ | NO {s['no_price']:.1f}¢")
        print(f"  AI Estimate: {s['ai_probability']:.1%}")
        print(f"  Edge:        {s['edge']:.1%}")
        print(f"  EV ($2 bet): ${s['ev_on_2usd']:+.2f}")
        print(f"  Volume:      ${s['volume']:,.0f}")
        print(f"  Market ID:   {s['market_id']}")
        print()


# Quick Test

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Test with a mock market
    test_market = {
        "id": "test_001",
        "question": "Will US Federal Reserve cut rates in May 2026?",
        "description": "Resolves YES if the Federal Reserve announces a rate cut at the May 2026 FOMC meeting.",
        "volume": "2500000",
        "outcomePrices": ["0.35", "0.65"],
    }

    result = analyze_market(test_market)

    if result:
        display_signals([result])
    else:
        print("No signal found for test market.")
        