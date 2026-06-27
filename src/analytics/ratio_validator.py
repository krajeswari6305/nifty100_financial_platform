import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")

companies = pd.read_sql("""
SELECT id,
       company_name,
       roe_percentage
FROM companies
""", conn)

ratios = pd.read_sql("""
SELECT company_id,
       year,
       return_on_equity_pct
FROM financial_ratios
""", conn)

merged = companies.merge(
    ratios,
    left_on="id",
    right_on="company_id"
)

merged["difference"] = (
    merged["roe_percentage"]
    - merged["return_on_equity_pct"]
).abs()

# Find edge cases (difference > 5%)
edge_cases = merged[merged["difference"] > 5]

# Create log file
with open("output/ratio_edge_cases.log", "w") as f:
    for _, row in edge_cases.iterrows():
        f.write(
            f"{row['company_name']} | {row['year']} | "
            f"Source ROE={row['roe_percentage']} | "
            f"Calculated ROE={row['return_on_equity_pct']} | "
            f"Difference={row['difference']:.2f}% | "
            f"Category=Version Difference\n"
        )

print(f"Edge cases found: {len(edge_cases)}")
print("ratio_edge_cases.log created successfully.")

conn.close()