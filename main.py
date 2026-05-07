from fastapi import FastAPI
import sqlite3
import os

app = FastAPI()
DB_PATH = os.path.join(os.path.dirname(__file__), "quotes.db")

@app.post("/quotes")
def create_quote(text: str, author: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO quotes (text, author) VALUES (?, ?)",
        (text, author)
    )
    conn.commit()
    conn.close()

    return {"message": "Quote added"}

@app.get("/quotes")
def get_quotes():
    conn = sqlite3.connect("quotes.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM quotes")
    data = cursor.fetchall()
    conn.close()

    return data

@app.put("/quotes/{quote_id}")
def update_quote(quote_id: int, text: str, author: str):
    conn = sqlite3.connect("quotes.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE quotes SET text=?, author=? WHERE id=?",
        (text, author, quote_id)
    )
    conn.commit()
    conn.close()

    return {"message": "Quote updated"}

@app.delete("/quotes/{quote_id}")
def delete_quote(quote_id: int):
    conn = sqlite3.connect("quotes.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM quotes WHERE id=?", (quote_id,))
    conn.commit()
    conn.close()

    return {"message": "Quote deleted"}

def get_db_connection():
    conn = sqlite3.connect("quotes.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/")
def root():
    return {"message": "Quotes API is running"}

@app.get("/quotes")
def get_quotes():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM quotes")
    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]