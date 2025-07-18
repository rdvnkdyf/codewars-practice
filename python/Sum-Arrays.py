def sum_array(a):
    """
    Calculates the sum of numbers in a given array.

    Args:
        numbers (list): A list of numbers (integers or floats, positive or negative).

    Returns:
        float/int: The sum of the numbers in the array. Returns 0 if the array is empty.
    """
    # If the array is empty, return 0 as per the requirement.
    if not a:
        return 0

    # Initialize a variable to store the sum.
    total = 0

    # Iterate through each number in the array and add it to the total.
    for num in a:
        total += num

    # Return the calculated sum.
    return total