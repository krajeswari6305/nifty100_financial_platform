import pytest

from src.analytics.ratios import (
    net_profit_margin,
    operating_profit_margin,
    check_opm,
    return_on_equity,
    return_on_capital_employed,
    return_on_assets,
    debt_to_equity,
    high_leverage_flag,
    interest_coverage,
    icr_label,
    interest_warning,
    net_debt,
    asset_turnover,
)

def test_net_profit_margin_normal():
    assert net_profit_margin(500, 1000) == 50.0


def test_net_profit_margin_zero_sales():
    assert net_profit_margin(100, 0) is None


def test_operating_profit_margin():
    assert operating_profit_margin(250, 1000) == 25.0


def test_check_opm_mismatch():
    assert check_opm(25.0, 20.0) is True


def test_return_on_equity():
    assert return_on_equity(500, 1000, 4000) == 10.0


def test_return_on_equity_negative_equity():
    assert return_on_equity(100, -50, -100) is None


def test_return_on_capital_employed():
    assert return_on_capital_employed(800, 1000, 4000, 2000) == 11.43


def test_return_on_assets():
    assert return_on_assets(500, 10000) == 5.0


def test_debt_to_equity():
    assert debt_to_equity(500, 1000, 4000) == 0.1


def test_debt_to_equity_debt_free():
    assert debt_to_equity(0, 1000, 4000) == 0


def test_high_leverage_flag():
    assert high_leverage_flag(6, "Industrials") is True


def test_interest_coverage():
    assert interest_coverage(1000, 200, 100) == 12.0


def test_icr_label():
    assert icr_label(None) == "Debt Free"


def test_interest_warning():
    assert interest_warning(1.2) is True


def test_net_debt():
    assert net_debt(1000, 200) == 800


def test_asset_turnover():
    assert asset_turnover(1000, 500) == 2.0