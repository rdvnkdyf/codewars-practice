Number.prototype.times = function (f) {
  // `this` anahtar kelimesi, metodun çağrıldığı sayıyı temsil eder.
  // `Math.floor(this)` kullanarak sayının tam kısmını alıyoruz.
  // Bu, (5.5).times() gibi durumlarda beklenmeyen sonuçları engeller.
  for (let i = 0; i < Math.floor(this); i++) {
    // Döngü değişkenini (i) argüman olarak fonksiyona iletiyoruz.
    f(i);
  }
};