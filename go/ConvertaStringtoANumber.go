package kata

import "strconv"

// StringToNumber fonksiyonu, bir stringi tam sayıya dönüştürür.
// Fonksiyon, strconv paketinin Atoi (ASCII to integer) fonksiyonunu kullanır.
// Problemdeki notta belirtildiği gibi, tüm girdiler geçerli bir tam sayı stringi olduğu için hata kontrolü gerekli değildir.
func StringToNumber(str string) int {
	// strconv.Atoi fonksiyonu, bir stringi tam sayıya dönüştürür ve potansiyel bir hata döndürür.
	// Burada hata değeri göz ardı edilir (_) çünkü girdi her zaman geçerli olacaktır.
	num, _ := strconv.Atoi(str)
	return num
}
