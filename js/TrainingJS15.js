function howManySmaller(arr, n) {
  let count = 0;
  for (let i = 0; i < arr.length; i++) {
    // Sayıyı iki ondalık basamağa yuvarlama
    const roundedNumber = Number(arr[i].toFixed(2));
    
    // n'den küçük olanları sayma
    if (roundedNumber < n) {
      count++;
    }
  }
  return count;
}