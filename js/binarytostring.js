function binaryToString(binary) {
  // İlk '0b' önekinin kaldırılması ve dizeyi '0b' ile bölme.
  // Bu, her bir ikili sayı için bir dizi elemanı oluşturur.
  const binaryArray = binary.split('0b').slice(1);

  // Oluşturulacak metin dizesi için boş bir dizi.
  const stringArray = [];

  // Her bir ikili sayı üzerinde döngü.
  for (const bin of binaryArray) {
    // parseInt kullanarak ikili sayıyı bir ondalık sayıya dönüştürür.
    const decimalValue = parseInt(bin, 2);
    
    // String.fromCharCode kullanarak ondalık sayıyı bir karaktere dönüştürür.
    // Oluşturulan karakteri stringArray dizisine ekler.
    stringArray.push(String.fromCharCode(decimalValue));
  }

  // Oluşturulan tüm karakterleri birleştirerek son dizeyi oluşturur.
  return stringArray.join('');
}