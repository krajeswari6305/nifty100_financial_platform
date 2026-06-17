import os
import pandas as pd

RAW_PATH = "data/raw"

for file_name in os.listdir(RAW_PATH):

    if not file_name.endswith((".xlsx", ".xls")):
        continue

    file_path = os.path.join(RAW_PATH, file_name)

    print("\n" + "=" * 80)
    print(f"FILE: {file_name}")

    excel_file = pd.ExcelFile(file_path)

    print(f"Sheets: {excel_file.sheet_names}")

    for sheet in excel_file.sheet_names:

        df = pd.read_excel(file_path, sheet_name=sheet)

        print(f"\nSheet: {sheet}")
        print(f"Shape: {df.shape}")

        print("\nColumns:")

        for col in df.columns:
            print(f" - {col}")

        print("\nFirst 3 rows:")
        print(df.head(3))

        print("\n" + "-" * 80)