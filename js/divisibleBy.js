function divisibleBy(numbers, divisor) {
  // Yeni bir boş dizi oluşturulur.
  let result = [];
  
  // 'numbers' dizisindeki her bir eleman döngüye alınır.
  for (let i = 0; i < numbers.length; i++) {
    // Mevcut sayı, bölen ile kalansız bölünebiliyor mu diye kontrol edilir.
    // Kalansız bölme işlemi, '%' (modülo) operatörü ile yapılır.
    if (numbers[i] % divisor === 0) {
      // Eğer kalansız bölünebiliyorsa, bu sayı 'result' dizisine eklenir.
      result.push(numbers[i]);
    }
  }
  
  // Döngü bittikten sonra, tam bölünen sayıları içeren 'result' dizisi geri döndürülür.
  return result;
}