function calculateTip(amount, rating) {
  // Oylamayı küçük harfe dönüştürerek büyük/küçük harf duyarsızlığını sağlıyoruz.
  const lowerRating = rating.toLowerCase();

  // Her derecelendirme için bahşiş yüzdesini tanımlayan bir nesne kullanıyoruz.
  const tipPercentages = {
    "terrible": 0,
    "poor": 0.05,
    "good": 0.10,
    "great": 0.15,
    "excellent": 0.20
  };

  // Derecelendirme tanımlanmışsa bahşişi hesaplayın.
  if (lowerRating in tipPercentages) {
    const tipAmount = amount * tipPercentages[lowerRating];
    // Bahşişi her zaman bir üst tam sayıya yuvarlayın.
    return Math.ceil(tipAmount);
  } else {
    // Tanınmayan bir derecelendirme için özel bir string döndürün.
    return "Rating not recognised";
  }
}