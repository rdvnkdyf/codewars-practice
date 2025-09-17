function isVow(a) {
  // Küçük harf sesli harflerin karakter kodları
  const vowels = {
    97: 'a', // a
    101: 'e', // e
    105: 'i', // i
    111: 'o', // o
    117: 'u', // u
  };

  // Dizideki her elemanı dönüştürmek için `map` metodunu kullan
  return a.map(num => {
    // `vowels` objesinde sayının bir karşılığı var mı kontrol et
    if (vowels[num]) {
      // Varsa, karşılık gelen harfi döndür
      return vowels[num];
    } else {
      // Yoksa, orijinal sayıyı döndür
      return num;
    }
  });
}