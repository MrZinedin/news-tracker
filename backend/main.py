from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from parser import fetch_news

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"]
)

@app.get("/api/news")
def get_news():
    return {"articles": fetch_news()}