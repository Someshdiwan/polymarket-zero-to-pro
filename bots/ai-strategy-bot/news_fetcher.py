"""
news_fetcher.py

Fetches relevant news articles for Polymarket markets.
Used by market_analyzer.py to provide context for AI probability estimation.

Supports:
- NewsAPI (newsapi.org) — free tier available
- Direct web search fallback
"""

import os
import requests
import logging
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_URL = "https://newsapi.org/v2/everything"


# Core News Fetcher

def fetch_news(query, hours_back=24, max_articles=5):
    """
    Fetch recent news articles for a given query.

    Args:
        query: Search query string (e.g. "Iran Israel strike")
        hours_back: How many hours back to search
        max_articles: Maximum number of articles to return

    Returns:
        List of article dictionaries with title, description, url, publishedAt
    """
    if not NEWS_API_KEY or NEWS_API_KEY == "your_newsapi_key_here":
        logger.warning("NEWS_API_KEY not set. Using fallback.")
        return _fallback_news(query)

    try:
        from_time = (datetime.now() - timedelta(hours=hours_back)).strftime("%Y-%m-%dT%H:%M:%S")

        params = {
            "q":          query,
            "from":       from_time,
            "sortBy":     "publishedAt",
            "language":   "en",
            "pageSize":   max_articles,
            "apiKey":     NEWS_API_KEY,
        }

        response = requests.get(NEWS_API_URL, params=params, timeout=10)
        response.raise_for_status()

        data     = response.json()
        articles = data.get("articles", [])

        logger.info(f"Fetched {len(articles)} articles for: {query}")

        return [
            {
                "title":       a.get("title", ""),
                "description": a.get("description", ""),
                "source":      a.get("source", {}).get("name", ""),
                "url":         a.get("url", ""),
                "published":   a.get("publishedAt", ""),
            }
            for a in articles
            if a.get("title") and "[Removed]" not in a.get("title", "")
        ]

    except requests.exceptions.RequestException as e:
        logger.error(f"NewsAPI request failed: {e}")
        return _fallback_news(query)
    except Exception as e:
        logger.error(f"Unexpected error in fetch_news: {e}")
        return []


def _fallback_news(query):
    """
    Fallback when NewsAPI is unavailable.
    Returns empty list with warning.
    In production, replace with your preferred news source.
    """
    logger.warning(f"No news available for: {query}. AI will use base rates only.")
    return []


# Market-Specific Query Builder

def build_news_query(market_question):
    """
    Convert a Polymarket question into an optimised news search query.

    Args:
        market_question: Full market question string

    Returns:
        Optimised search query string
    """
    # Remove common question words
    remove_words = [
        "will", "who", "when", "what", "does", "is", "are",
        "the", "a", "an", "by", "in", "on", "at", "to",
        "?", "...", "—"
    ]

    words  = market_question.lower().split()
    filtered = [w for w in words if w not in remove_words]

    # Take most meaningful words (first 6)
    query  = " ".join(filtered[:6])

    logger.debug(f"Built query: '{query}' from: '{market_question}'")
    return query


def format_news_for_ai(articles):
    """
    Format news articles into a clean string for AI consumption.

    Args:
        articles: List of article dicts from fetch_news()

    Returns:
        Formatted string of news summaries
    """
    if not articles:
        return "No recent news articles found for this market."

    lines = []
    for i, article in enumerate(articles, 1):
        lines.append(f"Article {i}:")
        lines.append(f"  Source:    {article['source']}")
        lines.append(f"  Published: {article['published'][:10]}")
        lines.append(f"  Title:     {article['title']}")
        lines.append(f"  Summary:   {article['description']}")
        lines.append("")

    return "\n".join(lines)


# Quick Test

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    test_question = "Will US strike Iran on March 3?"
    query         = build_news_query(test_question)

    print(f"Query: {query}")
    articles      = fetch_news(query, hours_back=48)
    formatted     = format_news_for_ai(articles)

    print(formatted)
    