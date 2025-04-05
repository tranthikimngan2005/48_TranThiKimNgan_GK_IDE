# save_to_db.py
import psycopg2

def create_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS articles (
                id SERIAL PRIMARY KEY,
                title TEXT,
                url TEXT,
                summary TEXT,
                time TEXT,
                author TEXT
            )
        """)
        conn.commit()

def save_articles(conn, articles):
    with conn.cursor() as cur:
        for article in articles:
            cur.execute("""
                INSERT INTO articles (title, url, summary, time, author)
                VALUES (%s, %s, %s, %s, %s)
            """, (article['title'], article['url'], article['summary'], article['time'], article['author']))
        conn.commit()

def connect_db():
    return psycopg2.connect(
        host="db",
        database="newsdb",
        user="postgres",
        password="postgres"
    )
