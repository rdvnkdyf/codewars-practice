function cutIt(arr){
  // First, find the shortest string length.
  let shortestLength = arr[0].length;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i].length < shortestLength) {
      shortestLength = arr[i].length;
    }
  }

  // Second, cut each string to the shortest length and return the new array.
  let result = [];
  for (let i = 0; i < arr.length; i++) {
    result.push(arr[i].slice(0, shortestLength));
  }
  return result;
}