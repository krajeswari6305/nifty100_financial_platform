from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = PROJECT_ROOT / "data" / "raw"

FILES = [
    "companies.xlsx",
    "profitandloss.xlsx",
    "balancesheet.xlsx",
    "cashflow.xlsx"
]

for file_name in FILES:

    print("\n" + "=" * 80)
    print(file_name)
    print("=" * 80)

    path = RAW_DIR / file_name

    df = pd.read_excel(path, header=None)

    print(df.head(10))