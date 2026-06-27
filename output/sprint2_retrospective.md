# Sprint 2 Retrospective

## Completed Work

- Implemented profitability ratios
- Implemented leverage ratios
- Implemented efficiency ratios
- Implemented CAGR engine
- Implemented cash flow KPIs
- Populated financial_ratios table
- Added edge case logging
- Generated capital allocation patterns

## Formula Decisions

- Returned None for zero denominators
- Returned None for negative equity
- Debt-free companies return Debt to Equity = 0
- Interest Coverage returns None when interest is zero
- CAGR engine handles turnaround, decline, zero base and insufficient data

## Testing

- All KPI unit tests passed
- Edge cases logged successfully

## Outcome

Financial Ratio Engine completed successfully.