function ensureQuestion(s) {
  // Dizgenin sonunda soru işareti var mı kontrol et
  if (s.endsWith('?')) {
    // Varsa, orijinal dizgeyi geri döndür
    return s;
  } else {
    // Yoksa, dizgenin sonuna "?" ekleyerek geri döndür
    return s + '?';
  }
}