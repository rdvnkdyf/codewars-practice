def subset_sum(xs, target):
    """
    Finds a subset of a list of positive numbers that sums to a non-negative target.

    Args:
        xs (list): A list of strictly positive numbers.
        target (int): The non-negative target sum.

    Returns:
        list: A subset of xs that sums to the target, or None if no such subset exists.
    """
    # Use a dictionary to store possible sums and the subsets that create them.
    # We start with the empty set, which sums to 0.
    possible_sums = {0: []}

    # Iterate through each number in the input list.
    for num in xs:
        # Create a temporary dictionary to hold new sums for the current iteration.
        new_sums = {}
        # Iterate over the sums we have found so far.
        for current_sum, current_subset in possible_sums.items():
            # Calculate a new sum by adding the current number.
            new_sum = current_sum + num
            
            # If the new sum is within the target and hasn't been found yet,
            # store it along with the new subset.
            if new_sum <= target and new_sum not in possible_sums and new_sum not in new_sums:
                new_subset = current_subset + [num]
                new_sums[new_sum] = new_subset

        # Merge the new sums into the main dictionary.
        possible_sums.update(new_sums)
    
    # After iterating through all numbers, check if the target sum exists in the final set of possible sums.
    if target in possible_sums:
        return possible_sums[target]

    # If the loop finishes and the target is not found, no solution exists.
    return None