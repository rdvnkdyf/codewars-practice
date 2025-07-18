def merge_arrays(arr1, arr2):
    """
    Merges two sorted integer arrays (ascending or descending) into a single
    ascending-sorted array with unique elements.

    Args:
        arr1 (list): The first sorted list of integers.
        arr2 (list): The second sorted list of integers.

    Returns:
        list: A new list containing all unique elements from both input arrays,
              sorted in ascending order.
    """
    # If both arrays are empty, return an empty array
    if not arr1 and not arr2:
        return []

    # Normalize arrays to be in ascending order
    if arr1 and arr1[0] > arr1[-1]:
        arr1.reverse()
    if arr2 and arr2[0] > arr2[-1]:
        arr2.reverse()

    # Combine and convert to a set to remove duplicates, then convert back to list
    combined_set = set(arr1 + arr2)

    # Convert the set to a list and sort it in ascending order
    result_array = sorted(list(combined_set))

    return result_array