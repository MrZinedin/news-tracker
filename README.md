# News Tracker

Внутренний инструмент для отслеживания последних публикаций из казахстанских новостных источников.

## Стек технологий

- **Backend:** Python, FastAPI, feedparser
- **Frontend:** HTML5, CSS3, Vanilla JS
- **Парсинг:** feedparser (RSS)

## Источники новостей

- [Наша Газета](https://ng.kz)
- [Новости Актау и Мангистауской области](https://www.lada.kz)
- [Время — общественно-политическая газета](https://time.kz)
- [Новости Караганды](https://ekaraganda.kz)

## Функциональность

- Сбор новостей по RSS-лентам из 4 источников
- Отображение в виде карточек (заголовок, источник, дата, ссылка)
- Поиск по заголовкам на стороне клиента
- Фильтрация по источнику
- Кнопка обновления новостей

## Локальный запуск

### 1. Клонируй репозиторий

```bash
git clone https://github.com/MrZinedin/news-tracker.git
cd news-tracker
```

### 2. Запусти бэкенд

```bash
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Бэкенд запустится на `http://127.0.0.1:8000`

### 3. Открой фронтенд

Открой файл `frontend/index.html` в браузере.

## Структура проекта

```
news-tracker/
├── backend/
│   ├── main.py          # FastAPI приложение
│   ├── news_parser.py   # RSS парсинг
│   ├── requirements.txt
│   └── sources.py       # Список источников
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
└── README.md
```