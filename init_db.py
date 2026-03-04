import sqlite3
import os

# Match the same database path used in app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

DB_PATH = os.path.join(DATA_DIR, "expenses.db")

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()


# Members table
c.execute("""
CREATE TABLE IF NOT EXISTS members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
)
""")


# Expenses table
c.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    member_id INTEGER NOT NULL,
    category TEXT NOT NULL,
    amount REAL NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY(member_id) REFERENCES members(id) ON DELETE CASCADE
)
""")


# Completed payments table
c.execute("""
CREATE TABLE IF NOT EXISTS repayments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    payer TEXT NOT NULL,
    receiver TEXT NOT NULL,
    amount REAL NOT NULL,
    date TEXT NOT NULL
)
""")


# Sample members
members = ["Arjun", "Priya", "Rohan", "Sonia", "Vikram"]

for m in members:
    c.execute(
        "INSERT OR IGNORE INTO members (name) VALUES (?)",
        (m,)
    )


conn.commit()
conn.close()

print("Database initialized successfully.")