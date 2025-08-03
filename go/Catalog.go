package kata

import (
	"fmt"
	"regexp"
	"strings"
)

func Catalog(s string, article string) string {
	// Split the catalog string into individual product blocks.
	// Each block is separated by a blank line ("\n\n").
	productBlocks := strings.Split(s, "\n\n")

	// Regular expressions to extract name, price, and quantity.
	// Using non-greedy quantifiers (.*?) to ensure correct matching.
	nameRegex := regexp.MustCompile(`<name>(.*?)</name>`)
	prxRegex := regexp.MustCompile(`<prx>(.*?)</prx>`)
	qtyRegex := regexp.MustCompile(`<qty>(.*?)</qty>`)

	var resultLines []string

	for _, block := range productBlocks {
		// Trim spaces from the block to handle any minor formatting inconsistencies
		trimmedBlock := strings.TrimSpace(block)
		if trimmedBlock == "" {
			continue // Skip empty blocks
		}

		// Extract product details using regex
		nameMatch := nameRegex.FindStringSubmatch(trimmedBlock)
		prxMatch := prxRegex.FindStringSubmatch(trimmedBlock)
		qtyMatch := qtyRegex.FindStringSubmatch(trimmedBlock)

		// Ensure all necessary parts were found
		if len(nameMatch) < 2 || len(prxMatch) < 2 || len(qtyMatch) < 2 {
			// This case ideally shouldn't happen based on problem statement ("valid catalog extract")
			// but it's good practice for robustness.
			continue
		}

		productName := nameMatch[1]
		price := prxMatch[1]
		quantity := qtyMatch[1]

		// Check if the product name contains the article (case-insensitive search if needed, but problem implies exact match on name fragment)
		// The example "table saw" for "saw" implies a substring match.
		if strings.Contains(productName, article) {
			// Format the output string as specified
			// "product name > prx: $price qty: quantity"
			formattedLine := fmt.Sprintf("%s > prx: $%s qty: %s", productName, price, quantity)
			resultLines = append(resultLines, formattedLine)
		}
	}

	// If no matching lines were found, return "Nothing".
	if len(resultLines) == 0 {
		return "Nothing"
	}

	// Join all found lines with a newline character.
	return strings.Join(resultLines, "\n")
}