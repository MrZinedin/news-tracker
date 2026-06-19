import feedparser
import requests
from sources import SOURCES

def fetch_news():
    articles = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    for source in SOURCES:
        try:
            response = requests.get(source["url"], headers=headers, timeout=10)
            feed = feedparser.parse(response.content)
            print(f"{source['name']}: найдено {len(feed.entries)} записей")
            for entry in feed.entries[:10]:
                articles.append({
                    "title": entry.get("title", "no title"),
                    "link": entry.get("link", "#"),
                    "published": entry.get("published", "no date"),
                    "source": source["name"]
                })
        except Exception as e:
            print(f"Error fetching news from {source['name']}: {e}")

    return articles