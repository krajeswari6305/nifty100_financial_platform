import re
import pandas as pd


def normalize_year(value):
    if pd.isna(value):
        return None

    value = str(value).strip()

    if value == "":
        return None

    if value.upper() == "TTM":
        return "TTM"

    # FY2024 -> 2024
    match = re.fullmatch(r"FY\s*(\d{4})", value.upper())
    if match:
        return int(match.group(1))

    # FY24 -> 2024
    match = re.fullmatch(r"FY\s*(\d{2})", value.upper())
    if match:
        return 2000 + int(match.group(1))

    # Mar 2024, Q1 2024, 2024
    match = re.search(r"\b(19\d{2}|20\d{2})\b", value)
    if match:
        return int(match.group(1))

    # Numeric values like 2024.0
    try:
        year = int(float(value))
        if 1900 <= year <= 2100:
            return year
    except (ValueError, TypeError):
        pass

    return None


def normalize_ticker(value):
    if pd.isna(value):
        return None

    value = str(value).strip().upper()

    if value == "":
        return None

    return value