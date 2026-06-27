def free_cash_flow(operating_activity, investing_activity):
    """
    Free Cash Flow = CFO + Investing Activity

    Investing activity is usually negative.
    Negative FCF is allowed.
    """
    return operating_activity + investing_activity


def cfo_quality_score(cfo, pat):
    """
    CFO Quality Score = CFO / PAT
    """

    if pat == 0:
        return None

    score = cfo / pat

    if score > 1.0:
        return score, "High Quality"

    elif score >= 0.5:
        return score, "Moderate"

    else:
        return score, "Accrual Risk"
    



def capex_intensity(investing_activity, sales):
    """
    CapEx Intensity = abs(Investing Activity) / Sales × 100
    """

    if sales == 0:
        return None

    intensity = abs(investing_activity) / sales * 100

    if intensity < 3:
        label = "Asset Light"
    elif intensity <= 8:
        label = "Moderate"
    else:
        label = "Capital Intensive"

    return round(intensity, 2), label


def fcf_conversion_rate(free_cash_flow, operating_profit):
    """
    FCF Conversion Rate = FCF / Operating Profit × 100
    """

    if operating_profit == 0:
        return None

    rate = (free_cash_flow / operating_profit) * 100

    return round(rate, 2)


def capital_allocation_pattern(cfo, cfi, cff, cfo_pat_ratio=None):
    """
    Classify capital allocation pattern based on CFO, CFI and CFF.
    """

    sign = (
        "+" if cfo >= 0 else "-",
        "+" if cfi >= 0 else "-",
        "+" if cff >= 0 else "-"
    )

    if sign == ("+", "-", "-"):
        if cfo_pat_ratio is not None and cfo_pat_ratio > 1:
            return "Shareholder Returns"
        return "Reinvestor"

    elif sign == ("+", "+", "-"):
        return "Liquidating Assets"

    elif sign == ("-", "+", "+"):
        return "Distress Signal"

    elif sign == ("-", "-", "+"):
        return "Growth Funded by Debt"

    elif sign == ("+", "+", "+"):
        return "Cash Accumulator"

    elif sign == ("-", "-", "-"):
        return "Pre-Revenue"

    elif sign == ("+", "-", "+"):
        return "Mixed"

    return "Unknown"