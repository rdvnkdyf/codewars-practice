package kata

func Past(h, m, s int) int {
  // Verilen saat, dakika ve saniye değerlerini milisaniyeye dönüştürerek topluyoruz.
  // 1 saat = 60 dakika = 3600 saniye = 3,600,000 milisaniye
  // 1 dakika = 60 saniye = 60,000 milisaniye
  // 1 saniye = 1,000 milisaniye

  totalMilliseconds := (h * 3600 * 1000) + (m * 60 * 1000) + (s * 1000)

  return totalMilliseconds
}