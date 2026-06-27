def net_profit_margin(net_profit, sales):
    if sales == 0:
        return None

    return round((net_profit / sales) * 100, 2)


def operating_profit_margin(operating_profit, sales):
    if sales == 0:
        return None

    return round((operating_profit / sales) * 100, 2)


def check_opm(computed_opm, source_opm):
    if computed_opm is None or source_opm is None:
        return False

    difference = abs(computed_opm - source_opm)

    return difference > 1


def return_on_equity(net_profit, equity_capital, reserves):
    """
    Return on Equity (ROE)
    """

    equity = equity_capital + reserves

    if equity <= 0:
        return None

    return round((net_profit / equity) * 100, 2)




def return_on_capital_employed(
    ebit,
    equity_capital,
    reserves,
    borrowings
):
    """
    Return on Capital Employed (ROCE)
    """

    capital_employed = equity_capital + reserves + borrowings

    if capital_employed <= 0:
        return None

    return round((ebit / capital_employed) * 100, 2)




def return_on_assets(net_profit, total_assets):
    """
    Return on Assets (ROA)
    """

    if total_assets <= 0:
        return None

    return round((net_profit / total_assets) * 100, 2)



def debt_to_equity(borrowings, equity_capital, reserves):
    """
    Debt to Equity Ratio
    """

    if borrowings == 0:
        return 0

    total_equity = equity_capital + reserves

    if total_equity <= 0:
        return None

    return round(borrowings / total_equity, 2)



def high_leverage_flag(debt_to_equity_ratio, broad_sector):
    """
    Returns True if company has very high leverage.
    Financial companies are excluded.
    """

    if broad_sector == "Financials":
        return False

    return debt_to_equity_ratio > 5



def interest_coverage(operating_profit, other_income, interest):
    """
    Interest Coverage Ratio
    """

    if interest == 0:
        return None

    icr = (operating_profit + other_income) / interest

    return round(icr, 2)


def icr_label(icr):
    """
    Returns label for debt-free companies.
    """

    if icr is None:
        return "Debt Free"

    return None



def interest_warning(icr):
    """
    Returns True if Interest Coverage Ratio is below 1.5.
    """

    if icr is None:
        return False

    return icr < 1.5



def net_debt(borrowings, investments):
    """
    Net Debt = Borrowings - Investments
    """

    return round(borrowings - investments, 2)


def asset_turnover(sales, total_assets):
    """
    Asset Turnover Ratio
    """

    if total_assets == 0:
        return None

    return round(sales / total_assets, 2)