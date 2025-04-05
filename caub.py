# clean_news.py
from bs4 import BeautifulSoup

def clean_html(text):
    if text:
        return BeautifulSoup(text, "html.parser").get_text(strip=True)
    return None

def clean_data(news_list):
    for item in news_list:
        item["title"] = clean_html(item["title"])
        item["summary"] = clean_html(item["summary"])
        item["time"] = clean_html(item["time"])
        item["author"] = clean_html(item["author"])
    return news_list
if __name__ == "__main__":
    sample = [{
        "title": "<b>AI tiến bộ</b>",
        "summary": "<p>AI sẽ thống trị.</p>",
        "time": "<span>2025-04-05</span>",
        "author": "<i>Nguyễn Văn A</i>"
    }]
    clean_sample = clean_data(sample)
    print(clean_sample)
