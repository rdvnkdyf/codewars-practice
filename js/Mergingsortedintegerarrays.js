function mergeArrays(a, b) {
  // İki diziyi birleştir.
  const mergedArray = [...a, ...b];
  
  // Bir Set oluşturarak yinelenen elemanları kaldır.
  const uniqueArray = [...new Set(mergedArray)];
  
  // Benzersiz elemanları içeren diziyi sırala.
  uniqueArray.sort((x, y) => x - y);
  
  // Sıralanmış ve benzersiz diziyi geri döndür.
  return uniqueArray;
}