def hofstadter_q(n):
    if n <= 0:
        return None

    # Base cases for the sequence
    if n <= 2:
        return 1

    # Use a list to store the sequence values for efficient lookup.
    # We use 1-based indexing for convenience by starting with a placeholder at index 0.
    q_sequence = [0, 1, 1]

    # Iteratively build the sequence up to the desired term 'n'.
    for i in range(3, n + 1):
        # Apply the recursive formula using the values stored in our list.
        # Q(i) = Q(i - Q(i-1)) + Q(i - Q(i-2))
        next_q_value = q_sequence[i - q_sequence[i - 1]] + q_sequence[i - q_sequence[i - 2]]
        q_sequence.append(next_q_value)

    # Return the nth term from our completed sequence list.
    return q_sequence[n]