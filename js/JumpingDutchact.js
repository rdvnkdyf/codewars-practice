function sc(floor) {
  if (floor <= 1) {
    return "";
  }
  
  let result = "Aa~ ".repeat(floor - 1) + "Pa!";
  
  if (floor <= 6) {
    result += " Aa!";
  }
  
  return result;
}