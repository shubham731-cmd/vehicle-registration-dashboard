import sqlite3
from pathlib import Path

def setup_database():
    Path("data/database").mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect("data/database/vehicle_data.db")
    with open("src/database/schema.sql", "r") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
    print("Database setup complete ✅")

if __name__ == "__main__":
    setup_database()
