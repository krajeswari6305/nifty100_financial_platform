from pathlib import Path
import sqlite3
from datetime import datetime
import traceback

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DIR = PROJECT_ROOT / "data" / "raw"
DB_PATH = PROJECT_ROOT / "nifty100.db"
OUTPUT_DIR = PROJECT_ROOT / "output"

SPECIAL_FILES = {
    "companies.xlsx",
    "profitandloss.xlsx",
    "balancesheet.xlsx",
    "cashflow.xlsx",
    "analysis.xlsx",
    "documents.xlsx",
    "prosandcons.xlsx"
}

FILES = {
    "companies": "companies.xlsx",
    "profitandloss": "profitandloss.xlsx",
    "balancesheet": "balancesheet.xlsx",
    "cashflow": "cashflow.xlsx",
    "analysis": "analysis.xlsx",
    "documents": "documents.xlsx",
    "prosandcons": "prosandcons.xlsx",
    "sectors": "sectors.xlsx",
    "stock_prices": "stock_prices.xlsx",
    "financial_ratios": "financial_ratios.xlsx",
    "peer_groups": "peer_groups.xlsx"
}

COMPANY_TABLES = {
    "profitandloss",
    "balancesheet",
    "cashflow",
    "analysis",
    "documents",
    "prosandcons",
    "financial_ratios",
    "stock_prices",
    "sectors"
}


def load_excel(file_name):
    header_row = 1 if file_name in SPECIAL_FILES else 0
    return pd.read_excel(RAW_DIR / file_name, header=header_row)


def standardize_columns(df):
    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace("-", "_", regex=False)
    )
    return df


def main():

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")

    audit_rows = []
    valid_company_ids = set()

    for table_name, file_name in FILES.items():

        print(f"Loading {table_name}...")

        try:
            df = load_excel(file_name)
            df = standardize_columns(df)

            rejected = 0

            # Store valid company IDs after companies table is loaded
            if table_name == "companies":

                df["id"] = df["id"].astype(str).str.strip()

                valid_company_ids = set(df["id"])

            # Filter child tables
            elif table_name in COMPANY_TABLES:

                if "company_id" in df.columns:

                    df["company_id"] = (
                        df["company_id"]
                        .astype(str)
                        .str.strip()
                        .replace({
                            "AGTL": "ATGL"
                        })
                    )

                    before = len(df)

                    df = df[
                        df["company_id"].isin(valid_company_ids)
                    ]

                    rejected = before - len(df)

            rows_loaded = len(df)

            df.to_sql(
                table_name,
                conn,
                if_exists="append",
                index=False,
                chunksize=500
            )

            audit_rows.append({
                "table_name": table_name,
                "rows_loaded": rows_loaded,
                "rows_rejected": rejected,
                "load_time": datetime.now()
            })

            print(
                f"✓ {rows_loaded} rows loaded "
                f"({rejected} rejected)"
            )

        except Exception as e:

            audit_rows.append({
                "table_name": table_name,
                "rows_loaded": 0,
                "rows_rejected": len(df) if "df" in locals() else 0,
                "load_time": datetime.now()
            })

            print(f"\n✗ Error loading {table_name}")
            print(f"Reason: {repr(e)}")
            traceback.print_exc()

    audit_df = pd.DataFrame(audit_rows)

    OUTPUT_DIR.mkdir(exist_ok=True)

    audit_df.to_csv(
        OUTPUT_DIR / "load_audit.csv",
        index=False
    )

    conn.close()

    print("\nLoad completed.")


if __name__ == "__main__":
    main()