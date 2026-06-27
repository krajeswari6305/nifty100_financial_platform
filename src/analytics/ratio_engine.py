import sqlite3
import pandas as pd

from src.analytics.ratios import (
    net_profit_margin,
    operating_profit_margin,
    return_on_equity,
    return_on_capital_employed,
    return_on_assets,
)

from src.analytics.cagr import revenue_cagr

from src.analytics.cashflow_kpis import (
    free_cash_flow,
    cfo_quality_score,
    capex_intensity,
    fcf_conversion_rate,
)

DB_PATH = "nifty100.db"

conn = sqlite3.connect(DB_PATH)

companies = pd.read_sql("SELECT * FROM companies", conn)

profit = pd.read_sql("SELECT * FROM profitandloss", conn)

balance = pd.read_sql("SELECT * FROM balancesheet", conn)

cash = pd.read_sql("SELECT * FROM cashflow", conn)