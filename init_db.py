import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "expenses.db")

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

# ---5 unique sample members ---
print("Adding sample members...")
c.execute("INSERT OR IGNORE INTO members (name) VALUES (?)", ("Arjun",))
c.execute("INSERT OR IGNORE INTO members (name) VALUES (?)", ("Priya",))
c.execute("INSERT OR IGNORE INTO members (name) VALUES (?)", ("Rohan",))
c.execute("INSERT OR IGNORE INTO members (name) VALUES (?)", ("Sonia",))
c.execute("INSERT OR IGNORE INTO members (name) VALUES (?)", ("Vikram",))

conn.commit()
conn.close()
print(f"✅ Database created/updated successfully with 5 sample members at: {DB_PATH}")