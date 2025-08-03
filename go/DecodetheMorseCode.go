package kata

import (
	"strings"
)

// MORSE_CODE is preloaded by the testing environment.
// DO NOT define it here again, as it will cause a redeclaration error.
// You can directly use MORSE_CODE within the DecodeMorse function.

// DecodeMorse decodes a Morse code string into a human-readable string.
func DecodeMorse(morseCode string) string {
	// 1. Trim leading/trailing spaces from the entire message.
	// This ensures "   .... ." is treated the same as ".... .".
	trimmedCode := strings.TrimSpace(morseCode)

	// 2. Split the message into words. Words are separated by "   " (three spaces).
	// Use three spaces explicitly to split words.
	morseWords := strings.Split(trimmedCode, "   ")

	var decodedWords []string // To store the decoded human-readable words

	// 3. Iterate over each Morse word
	for _, morseWord := range morseWords {
		// 4. Split each Morse word into individual character codes.
		// Characters are separated by a single space " ".
		// strings.Fields is robust and handles multiple spaces between characters.
		morseChars := strings.Fields(morseWord)

		var decodedChars []string // To store the decoded human-readable characters for the current word

		// 5. Iterate over each Morse character code and decode it.
		for _, charCode := range morseChars {
			// Directly access the preloaded MORSE_CODE map
			decodedChar := MORSE_CODE[charCode] // MORSE_CODE is available globally from preloaded environment
			decodedChars = append(decodedChars, decodedChar)
		}
		// Join the decoded characters to form a single word.
		decodedWords = append(decodedWords, strings.Join(decodedChars, ""))
	}

	// 6. Join the decoded words with a single space to form the final message.
	return strings.Join(decodedWords, " ")
}