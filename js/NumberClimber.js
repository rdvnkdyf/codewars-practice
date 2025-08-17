function climb(n) {
  // Geçici bir dizi oluşturarak diziyi sondan başa doğru inşa ediyoruz.
  const tempSequence = [];
  let current = n;

  // 'current' 1'e eşit olana kadar döngüye devam ediyoruz.
  while (current >= 1) {
    // Mevcut sayıyı geçici diziye ekliyoruz.
    tempSequence.push(current);

    // Bir önceki sayıyı bulmak için tersine işlem yapıyoruz.
    // Eğer sayı çiftse, ikiye bölüyoruz.
    if (current % 2 === 0) {
      current /= 2;
    } 
    // Eğer sayı tekse, 1 çıkarıp ikiye bölüyoruz.
    else {
      current = (current - 1) / 2;
    }
  }

  // Geçici dizi azalan sırada olduğu için,
  // .reverse() veya .unshift() kullanmadan manuel olarak tersine çeviriyoruz.
  const finalSequence = [];
  for (let i = tempSequence.length - 1; i >= 0; i--) {
    finalSequence.push(tempSequence[i]);
  }
  
  return finalSequence;
}