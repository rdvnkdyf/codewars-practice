function integrate(coefficient, exponent) {
  // Üsse 1 ekle
  const newExponent = exponent + 1;

  // Yeni üsse bölerek yeni katsayıyı bul
  const newCoefficient = coefficient / newExponent;

  // Sonucu istenen formatta bir dizge olarak döndür
  return `${newCoefficient}x^${newExponent}`;
}