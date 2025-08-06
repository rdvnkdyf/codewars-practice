function twoDecimalPlaces(num) {
  // The toFixed() method formats a number using fixed-point notation.
  // It returns a string representation of the number, with exactly two digits after the decimal point.
  // The number is rounded if necessary.
  // For example, 5.5589 becomes "5.56" and -3.3424 becomes "-3.34".
  return Number(num.toFixed(2));
}
