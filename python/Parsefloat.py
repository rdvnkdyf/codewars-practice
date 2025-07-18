def parse_float(string):
    """
    Attempts to convert a string or list to a float.

    Args:
        value (str or list): The input to be converted.

    Returns:
        float: The converted float number if successful.
        str: 'none' if conversion is not possible (e.g., invalid string, or a list).
    """
    # Check if the input is a string
    if isinstance(string, str):
        try:
            # Attempt to convert the string to a float
            return float(string)
        except ValueError:
            # If a ValueError occurs (e.g., string is not a valid number), return 'none'
            return None
    # If the input is not a string (e.g., it's a list, int, bool, etc.),
    # it cannot be directly converted to a float by float() in the way expected,
    # so return 'none'.
    else:
        return None