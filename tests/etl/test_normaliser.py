from src.etl.normaliser import normalize_year, normalize_ticker
import numpy as np


# normalize_year tests

def test_year_mar_2024():
    assert normalize_year("Mar 2024") == 2024

def test_year_mar_2018():
    assert normalize_year("Mar 2018") == 2018

def test_year_fy24():
    assert normalize_year("FY24") == 2024

def test_year_fy23():
    assert normalize_year("FY23") == 2023

def test_year_2024():
    assert normalize_year("2024") == 2024

def test_year_integer():
    assert normalize_year(2023) == 2023

def test_year_ttm():
    assert normalize_year("TTM") == "TTM"

def test_year_ttm_lowercase():
    assert normalize_year("ttm") == "TTM"

def test_year_with_spaces():
    assert normalize_year(" Mar 2024 ") == 2024

def test_year_none():
    assert normalize_year(None) is None

def test_year_empty():
    assert normalize_year("") is None

def test_year_nan():
    assert normalize_year(np.nan) is None

def test_year_invalid():
    assert normalize_year("abc") is None

def test_year_invalid_format():
    assert normalize_year("Q1 2024") == 2024

def test_year_fy2024():
    assert normalize_year("FY2024") == 2024

def test_year_float():
    assert normalize_year(2024.0) == 2024

def test_year_whitespace():
    assert normalize_year("   2022   ") == 2022

def test_year_old():
    assert normalize_year("Mar 2013") == 2013

def test_year_future():
    assert normalize_year("Mar 2030") == 2030

def test_year_zero():
    assert normalize_year(0) is None


# normalize_ticker tests

def test_ticker_lowercase():
    assert normalize_ticker("tcs") == "TCS"

def test_ticker_uppercase():
    assert normalize_ticker("INFY") == "INFY"

def test_ticker_mixed_case():
    assert normalize_ticker("ReLiAnCe") == "RELIANCE"

def test_ticker_spaces():
    assert normalize_ticker(" tcs ") == "TCS"

def test_ticker_hyphen():
    assert normalize_ticker("bajaj-auto") == "BAJAJ-AUTO"

def test_ticker_number():
    assert normalize_ticker("ltim") == "LTIM"

def test_ticker_none():
    assert normalize_ticker(None) is None

def test_ticker_empty():
    assert normalize_ticker("") is None

def test_ticker_whitespace():
    assert normalize_ticker("   ") is None

def test_ticker_special():
    assert normalize_ticker("m&m") == "M&M"

def test_ticker_dot():
    assert normalize_ticker("drreddy") == "DRREDDY"

def test_ticker_already_clean():
    assert normalize_ticker("HDFCBANK") == "HDFCBANK"

def test_ticker_with_newline():
    assert normalize_ticker("tcs\n") == "TCS"

def test_ticker_with_tab():
    assert normalize_ticker("\tinfy") == "INFY"

def test_ticker_numeric():
    assert normalize_ticker(123) == "123"