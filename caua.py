# crawl_news.py
import requests
from bs4 import BeautifulSoup

def crawl_news():
    url = "https://vnexpress.net/cong-nghe/ai"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.select(".item-news")[:5]  # Lấy 5 bài đầu
    news_data = []

    for article in articles:
        title_tag = article.select_one("h3.title-news a")
        summary_tag = article.select_one("p.description")
        time_tag = article.select_one("span.time")

        title = title_tag.get("title", "").strip() if title_tag else None
        url = title_tag.get("href") if title_tag else None
        summary = summary_tag.get_text(strip=True) if summary_tag else None
        time = time_tag.get_text(strip=True) if time_tag else None
        author = None  # Không có tác giả ngoài trang chủ

        news_data.append({
            "title": title,
            "url": url,
            "summary": summary,
            "time": time,
            "author": author
        })

    return news_data

if __name__ == "__main__":
    news = crawl_news()
    for n in news:
        print(n)
