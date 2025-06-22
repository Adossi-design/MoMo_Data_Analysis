
import sqlite3
import json
import os

DB_PATH = "database/momo.db"
JSON_PATH = "backend/cleaned_data.json"
SCHEMA_PATH = "database/schema.sql"

def init_db():
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        schema = f.read()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.executescript(schema)
    conn.commit()
    conn.close()

def insert_data():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    for record in data:
        cursor.execute("""
            INSERT INTO transactions (body, category, amount, date)
            VALUES (?, ?, ?, ?)
        """, (
            record["body"],
            record["category"],
            record["amount"],
            record["date"]
        ))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    insert_data()
    print("✔ Database created and populated successfully.")
