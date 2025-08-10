function bubblesortOnce(a) {
  // Dizinin bir kopyasını oluşturarak orijinal diziyi değiştirmeyiz.
  let arr = [...a];
  
  // Dizinin sonuna kadar döngü oluşturuyoruz.
  for (let i = 0; i < arr.length - 1; i++) {
    // İki komşu elemanı karşılaştırıyoruz.
    if (arr[i] > arr[i + 1]) {
      // Eğer ilk eleman daha büyükse, yerlerini değiştiriyoruz.
      let temp = arr[i];
      arr[i] = arr[i + 1];
      arr[i + 1] = temp;
    }
  }
  
  // Tek bir geçiş (pass) sonrası oluşan yeni diziyi döndürüyoruz.
  return arr;
}