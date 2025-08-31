package kata

import (
	"strconv"
)

// Digitize fonksiyonu, verilen negatif olmayan bir sayının basamaklarını ters sırada bir tam sayı dilimine (slice) dönüştürür.
func Digitize(n int) []int {
	// Sayı 0 ise, direkt olarak [0] döndürür.
	if n == 0 {
		return []int{0}
	}

	// Sayıyı string'e çeviriyoruz.
	s := strconv.Itoa(n)

	// Basamakları tutacak bir tam sayı dilimi oluşturuyoruz.
	result := make([]int, 0, len(s))

	// Sayının string temsilini tersten gezerek her karakteri bir basamağa çevirip dilime ekliyoruz.
	for i := len(s) - 1; i >= 0; i-- {
		// Karakteri string'e dönüştürüyoruz.
		digitChar := string(s[i])
		// String'i tekrar tam sayıya çeviriyoruz.
		digit, _ := strconv.Atoi(digitChar)
		// Elde ettiğimiz basamağı sonuç dilimine ekliyoruz.
		result = append(result, digit)
	}

	return result
}