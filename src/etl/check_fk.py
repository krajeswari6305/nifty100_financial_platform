from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = PROJECT_ROOT / "data" / "raw"

companies = pd.read_excel(
    RAW_DIR / "companies.xlsx",
    header=1
)

companies.columns = companies.columns.str.strip().str.lower()

valid_ids = set(companies["id"].astype(str).str.strip())

files = {
    "profitandloss.xlsx": "company_id",
    "balancesheet.xlsx": "company_id",
    "cashflow.xlsx": "company_id",
    "analysis.xlsx": "company_id",
    "documents.xlsx": "company_id",
    "prosandcons.xlsx": "company_id",
    "financial_ratios.xlsx": "company_id",
}

for file_name, column in files.items():

    df = pd.read_excel(
        RAW_DIR / file_name,
        header=1
    )

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
    )

    df[column] = df[column].astype(str).str.strip()

    invalid = set(df[column]) - valid_ids

    print(f"\n{file_name}")

    if invalid:
        print("Invalid company_id values:")
        print(sorted(invalid))
    else:
        print("No issues found.")