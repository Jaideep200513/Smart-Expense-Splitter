import sqlite3
import os

# --- Use /tmp path for Render/Docker ---
DB_PATH = "/tmp/expenses.db"

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

# --- 5 unique sample members ---
sample_members = ["Arjun", "Priya", "Rohan", "Sonia", "Vikram"]
for member in sample_members:
    c.execute("INSERT OR IGNORE INTO members (name) VALUES (?)", (member,))

conn.commit()
conn.close()

print(f"✅ Database created/updated successfully with 5 sample members at: {DB_PATH}")
