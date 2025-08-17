function grow(x) {
  let result = 1;
  for (let i = 0; i < x.length; i++) {
    result *= x[i];
  }
  return result;
}

// Yöntem 2: reduce() metodu kullanarak
// function grow(x){
//   // 'reduce' metodu, bir dizinin her elemanı için bir işlev çalıştırır
//   // ve tek bir değerle sonuçlanır.
//   // İlk parametre (accumulator), birikmiş değeri tutar.
//   // İkinci parametre (currentValue), dizideki mevcut elemandır.
//   // Başlangıç değeri 1 olarak ayarlanmıştır.
//   return x.reduce((accumulator, currentValue) => accumulator * currentValue, 1);
// }