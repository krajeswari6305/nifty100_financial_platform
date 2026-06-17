SELECT COUNT(*) FROM companies;

SELECT COUNT(*) FROM profitandloss;

SELECT COUNT(*) FROM balancesheet;

SELECT COUNT(*) FROM cashflow;

SELECT COUNT(*) FROM stock_prices;

SELECT broad_sector, COUNT(*)
FROM sectors
GROUP BY broad_sector;

SELECT company_id, MAX(year)
FROM profitandloss
GROUP BY company_id
LIMIT 10;

SELECT company_id, AVG(net_profit_margin_pct)
FROM financial_ratios
GROUP BY company_id
ORDER BY AVG(net_profit_margin_pct) DESC
LIMIT 10;

SELECT company_id, COUNT(*)
FROM stock_prices
GROUP BY company_id
ORDER BY COUNT(*) DESC
LIMIT 10;

SELECT *
FROM companies
LIMIT 5;