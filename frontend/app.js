const API_URL = "http://127.0.0.1:8000/api/news";
let allNews = [];

// загружаю новости с бэкенда
async function loadNews() {
    document.getElementById("news-grid").innerHTML = "<p>Загрузка...</p>";
    try {
        const response = await fetch(API_URL);
        const data = await response.json();
        allNews = data.news;
        fillSourceFilter(allNews);
        renderNews(allNews);
    } catch (error) {
        document.getElementById("news-grid").innerHTML = "<p>Ошибка загрузки. Нужно проверь что бэкенд запущен.</p>";
        console.error(error);
    }
}

// заполняю фильтр по источникам
function fillSourceFilter(news) {
    const select = document.getElementById("source-filter");
    const sources = [...new Set(news.map(n => n.source))];

    // оставляю первый option "Все источники"
    select.innerHTML = '<option value="">Все источники</option>';
    sources.forEach(source => {
        select.innerHTML += `<option value="${source}">${source}</option>`;
    });
}

// рисую карточки
function renderNews(news) {
    const grid = document.getElementById("news-grid");
    const stats = document.getElementById("stats");
    stats.textContent = `Показано: ${news.length} новостей`;
    if (news.length === 0) {
        grid.innerHTML = "<p>Ничего не найдено.</p>";
        return;
    }
    grid.innerHTML = news.map(item => `
        <div class="card">
            <div class="card-source">${item.source}</div>
            <div class="card-title">
                <a href="${item.link}" target="_blank">${item.title}</a>
            </div>
            <div class="card-date">${item.published}</div>
        </div>
    `).join("");
}

// фильтрую по поиску и источнику
function filterNews() {
    const query = document.getElementById("search").value.toLowerCase();
    const source = document.getElementById("source-filter").value;
    const filtered = allNews.filter(item => {
        const matchTitle = item.title.toLowerCase().includes(query);
        const matchSource = source === "" || item.source === source;
        return matchTitle && matchSource;
    });
    renderNews(filtered);
}

// вешаю события
document.getElementById("search").addEventListener("input", filterNews);
document.getElementById("source-filter").addEventListener("change", filterNews);
document.getElementById("refresh-btn").addEventListener("click", loadNews);

// запускаю при загрузке страницы
loadNews();