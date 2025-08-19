function isValid(idn) {
  // Düzenli ifade, kurallara uyan bir deseni kontrol eder.
  // ^: Dizgenin başlangıcı
  // [a-zA-Z_$]: İlk karakterin bir harf, alt çizgi veya dolar işareti olmasını sağlar.
  // [a-zA-Z0-9_$]*: Geri kalan karakterlerin sıfır veya daha fazla sayıda harf, rakam, alt çizgi veya dolar işareti olmasını sağlar.
  // $: Dizgenin sonu
  return /^[a-zA-Z_$][a-zA-Z0-9_$]*$/.test(idn);
}