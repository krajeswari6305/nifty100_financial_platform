import sqlite3
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

db_path = PROJECT_ROOT / "nifty100.db"
schema_path = PROJECT_ROOT / "db" / "schema.sql"

conn = sqlite3.connect(db_path)

with open(schema_path, "r", encoding="utf-8") as f:
    schema = f.read()

conn.executescript(schema)

conn.commit()
conn.close()

print(f"Database created successfully: {db_path}")