function grabDoll(dolls){
  var bag=[];
  // Loop through each doll in the 'dolls' array.
  for (var i = 0; i < dolls.length; i++) {
    // Check if the bag is already full. If it has 3 dolls, stop the loop.
    if (bag.length === 3) {
      break;
    }
    
    // Check if the current doll is not "Hello Kitty" or "Barbie doll".
    // If it's not one of them, we skip to the next iteration of the loop.
    if (dolls[i] !== "Hello Kitty" && dolls[i] !== "Barbie doll") {
      continue;
    }
    
    // If the doll is "Hello Kitty" or "Barbie doll", add it to the bag.
    bag.push(dolls[i]);
  }
  
  return bag;
}