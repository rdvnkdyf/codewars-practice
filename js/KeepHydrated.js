function litres(time) {
  // Verilen zamanı 0.5 ile çarpıyoruz.
  const totalLitres = time * 0.5;

  // Math.floor() kullanarak sonucu aşağı doğru yuvarlıyoruz.
  return Math.floor(totalLitres);
}