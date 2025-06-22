
from flask import Flask, jsonify, request
import sqlite3
from config import DB_PATH

app = Flask(__name__)

def query_db(query, args=(), one=False):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.execute(query, args)
    rows = cur.fetchall()
    conn.close()
    return (rows[0] if rows else None) if one else rows

@app.route("/api/transactions", methods=["GET"])
def get_transactions():
    category = request.args.get("category")
    query = "SELECT * FROM transactions"
    params = ()

    if category:
        query += " WHERE category = ?"
        params = (category,)

    results = query_db(query, params)
    return jsonify([dict(row) for row in results])

@app.route("/api/summary", methods=["GET"])
def get_summary():
    summary_query = """
        SELECT category, COUNT(*) as count, SUM(amount) as total_amount
        FROM transactions
        GROUP BY category
    """
    results = query_db(summary_query)
    return jsonify([dict(row) for row in results])

if __name__ == "__main__":
    app.run(debug=True)
