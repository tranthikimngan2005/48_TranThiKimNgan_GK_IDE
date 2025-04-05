from crawl_news import crawl_news
from clean_news import clean_data
from save_to_db import save_to_db

if __name__ == "__main__":
    raw = crawl_news()
    cleaned = clean_data(raw)
    save_to_db(cleaned)
