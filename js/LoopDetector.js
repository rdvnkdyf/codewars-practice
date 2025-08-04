function hasLoop(indices) {
  // If the input array is empty, there's no traversal possible, so no loop.
  if (indices.length === 0) {
    return false;
  }

  // Use a Set to store visited indices for efficient lookup.
  const visited = new Set();
  let currentIndex = 0; // Start traversal at index 0.

  // Loop indefinitely until a loop is detected or termination occurs.
  while (true) {
    // Check if the current index is out of bounds.
    // If it is, the traversal terminates.
    if (currentIndex < 0 || currentIndex >= indices.length) {
      return false;
    }

    // Check if the current index has been visited before.
    // If it has, a loop is detected.
    if (visited.has(currentIndex)) {
      return true;
    }

    // Mark the current index as visited.
    visited.add(currentIndex);

    // Move to the next index in the chain.
    currentIndex = indices[currentIndex];
  }
}