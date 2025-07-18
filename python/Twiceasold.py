def twice_as_old(dad_years_old, son_years_old):
    """
    Calculates how many years ago or in how many years a father was/will be
    twice as old as his son.

    Args:
        father_age (int): The current age of the father in years.
        son_age (int): The current age of the son in years.

    Returns:
        int: The absolute number of years ago or in the future when the
             father's age was/will be twice the son's age. This value is
             always greater than or equal to 0.
    """
    # The core idea is that the difference in their ages always remains constant.
    # Let 'x' be the number of years.
    # If in the past, father_age - x = 2 * (son_age - x)
    # If in the future, father_age + x = 2 * (son_age + x)

    # Let 'F' be father_age and 'S' be son_age.
    # We want to find 'x' such that F + x = 2 * (S + x) or F - x = 2 * (S - x)
    # A simpler way to think about it: if the father is twice as old,
    # his age is 2 * (his age - son's age).
    # So, the age of the father when he's twice the son's age is 2 * (father_age - son_age).
    # The number of years difference is then the absolute difference between
    # the current father's age and this calculated "twice as old" age.

    # Calculate the age difference between father and son. This difference is constant.
    age_difference = dad_years_old -  son_years_old

    # When the father is twice as old as the son, the son's age will be equal to
    # the age difference, and the father's age will be twice the age difference.
    # Example: If diff is 30, son is 30, father is 60.
    # The "target father age" when he is twice as old is 2 * age_difference.
    target_father_age = 2 * age_difference

    # The number of years to reach this state (or from this state)
    # is the absolute difference between the current father's age and the target age.
    years_difference = abs(dad_years_old - target_father_age)

    return years_difference