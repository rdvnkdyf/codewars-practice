package kata

// PositiveSum fonksiyonu, bir tam sayı dilimindeki (slice) tüm pozitif sayıların toplamını döndürür.
// Eğer toplanacak pozitif sayı yoksa, toplam 0'a eşittir.
func PositiveSum(numbers []int) int {
	var sum int
	for _, number := range numbers {
		if number > 0 {
			sum += number
		}
	}
	return sum
}