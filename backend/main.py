from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from news_parser import fetch_news

app = FastAPI()

# разрешаю фронтенду обращаться к api
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/api/news")
def get_news():
    # собираю новости и отдаю в json
    news = fetch_news()
    return {"count": len(news), "news": news}