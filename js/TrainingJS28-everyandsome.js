function mirrorImage(arr) {
  let result = [-1, -1];

  // Use the some() method to iterate through the array.
  // The loop will stop as soon as the callback function returns a truthy value.
  arr.some((currentValue, index) => {
    // Check if there is a next element in the array.
    if (index < arr.length - 1) {
      const nextValue = arr[index + 1];

      // Convert numbers to strings to check for mirror images.
      const str1 = String(currentValue);
      const str2 = String(nextValue);
      
      // Reverse the second string and compare with the first.
      const reversedStr2 = str2.split('').reverse().join('');
      
      if (str1 === reversedStr2) {
        // If they are, store them in the result array.
        result = [currentValue, nextValue];
        // Return true to stop the some() method's iteration.
        return true;
      }
    }
    // Return false to continue the iteration.
    return false;
  });

  return result;
}