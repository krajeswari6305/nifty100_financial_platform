from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = PROJECT_ROOT / "data" / "raw"

FILES = [
    "companies.xlsx",
    "profitandloss.xlsx",
    "balancesheet.xlsx",
    "cashflow.xlsx",
    "analysis.xlsx",
    "documents.xlsx",
    "prosandcons.xlsx",
    "sectors.xlsx",
    "stock_prices.xlsx",
    "financial_ratios.xlsx",
    "peer_groups.xlsx"
]

for file_name in FILES:
    path = RAW_DIR / file_name

    df = pd.read_excel(path)

    SPECIAL_FILES = {
        "companies.xlsx",
        "profitandloss.xlsx",
        "balancesheet.xlsx",
        "cashflow.xlsx",
        "analysis.xlsx",
        "documents.xlsx",
        "prosandcons.xlsx"
    }

    header_row = 1 if file_name in SPECIAL_FILES else 0

    df = pd.read_excel(path, header=header_row)

    for col in df.columns:
        print(col)