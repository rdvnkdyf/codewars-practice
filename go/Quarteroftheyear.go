package kata

// QuarterOf fonksiyonu, 1'den 12'ye kadar olan bir ay numarasına göre yılın çeyreğini döndürür.
// Ay 1-3 ise 1. çeyrek, 4-6 ise 2. çeyrek, 7-9 ise 3. çeyrek ve 10-12 ise 4. çeyrektir.
func QuarterOf(month int) int {
	if month >= 1 && month <= 3 {
		return 1
	} else if month >= 4 && month <= 6 {
		return 2
	} else if month >= 7 && month <= 9 {
		return 3
	} else {
		// 10, 11 ve 12. aylar 4. çeyreğe aittir.
		return 4
	}
}