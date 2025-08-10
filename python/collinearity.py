def collinearity(x1, y1, x2, y2):
    """
    Checks if two vectors starting from the origin are collinear.

    Args:
        x1, y1 (int): The coordinates of the first vector.
        x2, y2 (int): The coordinates of the second vector.

    Returns:
        bool: True if the vectors are collinear, False otherwise.
    """
    # First, handle the special case where one or both vectors are the zero vector (0, 0).
    # The zero vector is considered collinear with any other vector.
    if (x1 == 0 and y1 == 0) or (x2 == 0 and y2 == 0):
        return True

    # If neither vector is the zero vector, we can check for collinearity.
    # Two vectors (x1, y1) and (x2, y2) are collinear if (x1, y1) = k * (x2, y2).
    # This means x1 = k*x2 and y1 = k*y2.
    # To avoid division by zero when calculating k (e.g., k = x1/x2 = y1/y2),
    # we can use the cross-multiplication property: x1 * y2 = x2 * y1.
    # This check works for all cases where neither vector is (0,0), including
    # when individual coordinates are zero (e.g., a vector on an axis).
    return x1 * y2 == x2 * y1