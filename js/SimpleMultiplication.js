function simpleMultiplication(number) {
  // Verilen sayı çift ise (sayının 2'ye bölümünden kalan 0 ise)
  if (number % 2 === 0) {
    // Sayıyı 8 ile çarp
    return number * 8;
  } else {
    // Aksi halde (sayı tek ise), sayıyı 9 ile çarp
    return number * 9;
  }
}