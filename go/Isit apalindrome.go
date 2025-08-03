package kata
import (
	
	"strings"
) 

func IsPalindrome(str string) bool {
  // Convert the string to lowercase to make the check case-insensitive.
	lowerStr := strings.ToLower(str)

	// Create a new rune slice to reverse the string. Using a rune slice
	// is more robust for handling Unicode characters than a byte slice.
	runes := []rune(lowerStr)
	
	// Iterate from both ends of the string inwards.
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		// Swap the runes to reverse the string.
		runes[i], runes[j] = runes[j], runes[i]
	}

	// Convert the reversed rune slice back to a string.
	reversedStr := string(runes)

	// Compare the original lowercase string with the reversed one.
	return lowerStr == reversedStr
}