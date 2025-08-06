function firstNonConsecutive(arr) {
  // Iterate through the array starting from the second element (index 1).
  // We compare each element with its preceding element.
  for (let i = 1; i < arr.length; i++) {
    // Check if the current element is not exactly 1 greater than the previous element.
    if (arr[i] !== arr[i - 1] + 1) {
      // If it's not consecutive, return the current element.
      return arr[i];
    }
  }

  // If the loop completes, it means all elements are consecutive.
  // In this case, return null as per the problem description.
  return null;
}