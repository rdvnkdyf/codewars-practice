function pickIt(arr){
  let odd = [], even = [];
  // Loop through each number in the input array 'arr'.
  for (let i = 0; i < arr.length; i++) {
    const number = arr[i];

    // Check if the number is odd or even using the modulo operator.
    if (number % 2 !== 0) {
      // If the remainder when divided by 2 is not 0, it's odd.
      odd.push(number);
    } else {
      // Otherwise, it's even.
      even.push(number);
    }
  }
  
  return [odd,even];
}