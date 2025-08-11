package kata


func Zeros(n int) int {
	if n < 0 {
		return 0 // Factorials are not typically defined for negative numbers, so we return 0.
	}

	count := 0
	for i := 5; n/i >= 1; i *= 5 {
		count += n / i
	}

	return count
}