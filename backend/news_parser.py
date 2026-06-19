import feedparser
from datetime import datetime
from sources import SOURCES

def parse_date(entry) -> str:
    # достаю дату из rss и перевожу в нормальный вид
    if hasattr(entry, "published_parsed") and entry.published_parsed:
        dt = datetime(*entry.published_parsed[:6])
        return dt.strftime("%d.%m.%Y %H:%M")
    return "Дата неизвестна"

def fetch_news() -> list[dict]:
    # прохожу по каждому источнику и собираю новости
    all_news = []
    for source in SOURCES:
        try:
            feed = feedparser.parse(source["url"])
            for entry in feed.entries[:17]:
                news_item = {
                    "title": entry.get("title", "Без заголовка").strip(),
                    "link": entry.get("link", "#"),
                    "published": parse_date(entry),
                    "source": source["name"],
                }
                all_news.append(news_item)
        except Exception as e:
            # если источник не работает просто пропускаю его
            print(f"[ОШИБКА] {source['name']}: {e}")
            continue

    # новые новости сверху
    all_news.sort(key=lambda x: x["published"] if x["published"] != "Дата неизвестна" else "", reverse=True)
    return all_news