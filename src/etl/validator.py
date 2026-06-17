from pathlib import Path
import sqlite3
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DB_PATH = PROJECT_ROOT / "nifty100.db"
OUTPUT_PATH = PROJECT_ROOT / "output" / "validation_failures.csv"


def main():

    conn = sqlite3.connect(DB_PATH)

    failures = []

    # DQ-01: companies.id uniqueness

    duplicates = pd.read_sql_query("""
        SELECT id, COUNT(*) AS cnt
        FROM companies
        GROUP BY id
        HAVING COUNT(*) > 1
    """, conn)

    for _, row in duplicates.iterrows():

        failures.append({
            "rule_id": "DQ-01",
            "severity": "CRITICAL",
            "table_name": "companies",
            "record_id": row["id"],
            "message": "Duplicate company ID"
        })

    validation_df = pd.DataFrame(failures)

    validation_df.to_csv(
        OUTPUT_PATH,
        index=False
    )

    conn.close()

    print(f"Validation completed: {len(validation_df)} failures")


if __name__ == "__main__":
    main()
    