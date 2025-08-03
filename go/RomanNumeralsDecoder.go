package kata

// Decode converts a Roman numeral string to its integer value.
func Decode(roman string) int {
	// Define a map to store the value of each Roman symbol.
	romanMap := map[rune]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}

	total := 0
	lastVal := 0

	// Iterate through the Roman numeral string from right to left.
	for i := len(roman) - 1; i >= 0; i-- {
		// Get the value of the current symbol.
		currentVal := romanMap[rune(roman[i])]

		// If the current value is less than the last value, it's a subtractive case.
		if currentVal < lastVal {
			total -= currentVal
		} else {
			// Otherwise, add the value.
			total += currentVal
		}
		
		// Update the lastVal for the next iteration.
		lastVal = currentVal
	}

	return total
}