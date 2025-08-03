package kata
import "math"
func Movie(card, ticket int, perc float64) int {
	// Initialize the number of visits
	n := 0

	// Initialize total costs for both systems
	// We use float64 for System B's cost to handle decimals
	// and avoid rounding issues until the final comparison.
	costA := 0.0
	costB := float64(card) // System B starts with the card price

	// Initialize the price of the current ticket for System B.
	// This will be updated in each iteration.
	currentTicketPriceB := float64(ticket)

	// Loop indefinitely until the condition is met
	for {
		n++ // Increment the number of visits

		// Calculate System A's cost for 'n' visits
		costA = float64(ticket * n)

		// Update System B's total cost
		// First ticket for n=1: card + ticket * perc
		// Subsequent tickets: add currentTicketPriceB * perc
		costB += currentTicketPriceB * perc
		currentTicketPriceB *= perc // Update the ticket price for the next iteration

		// Check the condition: ceil(costB) < costA
		// math.Ceil rounds up to the nearest integer.
		if math.Ceil(costB) < costA {
			return n // Return the current number of visits
		}
	}
}