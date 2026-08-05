def interpret_correlation(value):
    """
    Interpret correlation strength.
    """

    value = abs(value)

    if value < 0.2:
        return "Very Weak"
    elif value < 0.4:
        return "Weak"
    elif value < 0.6:
        return "Moderate"
    elif value < 0.8:
        return "Strong"
    else:
        return "Very Strong"