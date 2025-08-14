function strCount(str, letter){
  // Initialize a counter to 0. This variable will keep track of the occurrences.
  let count = 0;

  // Use a for loop to iterate over each character of the input string.
  for (let i = 0; i < str.length; i++) {
    // Check if the character at the current index (str[i]) is equal to the target letter.
    if (str[i] === letter) {
      // If the characters match, increment the counter.
      count++;
    }
  }

  // After the loop has finished checking every character, return the final count.
  return count;
}