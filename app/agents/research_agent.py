from langchain_core.tools import tool
import feedparser
import urllib.parse

@tool("research_agent", return_direct=True)
def research_agent(location: str) -> str:
    """Fetch recent solar and renewable energy policy news for a given location."""
    # Encode location and query for safe URL usage
    query = urllib.parse.quote_plus(f"{location} solar policy OR renewable energy incentives")
    url = f"https://news.google.com/rss/search?q={query}"

    try:
        feed = feedparser.parse(url)
        if not feed.entries:
            return f"No solar or renewable energy policy news found for {location}."

        titles = [entry.title for entry in feed.entries[:3]]
        return f"Recent solar policy headlines for {location}: " + "; ".join(titles)
    except Exception as e:
        return f"Error fetching policy news for {location}: {str(e)}"
