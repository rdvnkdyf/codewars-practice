package kata

func BouncingBall(h, bounce, window float64) int {
	if h <= 0 || bounce <= 0 || bounce >= 1 || window >= h {
		return -1
	}

	count := 1 // Initial drop down
	currentHeight := h * bounce

	for currentHeight > window {
		count += 2 // Bouncing up and down
		currentHeight *= bounce
	}

	return count
}