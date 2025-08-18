function findAB(numbers, c) {
  for (let i = 0; i < numbers.length; i++) {
    for (let j = i; j < numbers.length; j++) {
      if (numbers[i] * numbers[j] === c) {
        // [2,2] hatası için özel kontrol
        if (i === j) {
          // Eğer aynı eleman kendiyle çarpılıyorsa, dizide bu elemandan bir tane daha olmalı.
          // Basit bir `indexOf` kontrolü kullanılabilir.
          if (numbers.indexOf(numbers[i], i + 1) === -1) {
            continue; // İkinci bir aynı eleman yoksa, bu çifti atla.
          }
        }
        return [numbers[i], numbers[j]];
      }
    }
  }
  return null;
}