from src.analytics.cashflow_kpis import (
    free_cash_flow,
    cfo_quality_score,
    capex_intensity,
    fcf_conversion_rate,
    capital_allocation_pattern,
)


def test_free_cash_flow():
    assert free_cash_flow(1000, -300) == 700


def test_negative_fcf():
    assert free_cash_flow(500, -700) == -200


def test_cfo_quality_high():
    assert cfo_quality_score(1200, 1000)[1] == "High Quality"


def test_cfo_quality_moderate():
    assert cfo_quality_score(700, 1000)[1] == "Moderate"


def test_cfo_quality_low():
    assert cfo_quality_score(300, 1000)[1] == "Accrual Risk"


def test_cfo_quality_zero_pat():
    assert cfo_quality_score(500, 0) is None


def test_capex_asset_light():
    assert capex_intensity(-20, 1000)[1] == "Asset Light"


def test_capex_moderate():
    assert capex_intensity(-60, 1000)[1] == "Moderate"


def test_capex_capital_intensive():
    assert capex_intensity(-150, 1000)[1] == "Capital Intensive"


def test_fcf_conversion():
    assert fcf_conversion_rate(700, 1000) == 70.0


def test_fcf_conversion_zero():
    assert fcf_conversion_rate(100, 0) is None


def test_reinvestor():
    assert capital_allocation_pattern(100, -50, -20) == "Reinvestor"


def test_shareholder_returns():
    assert capital_allocation_pattern(100, -50, -20, 1.5) == "Shareholder Returns"


def test_cash_accumulator():
    assert capital_allocation_pattern(100, 50, 20) == "Cash Accumulator"