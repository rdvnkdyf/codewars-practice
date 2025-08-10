function perfectRoots(n) {
  // İkinci kökün tam sayı olup olmadığını kontrol et
  let kok2 = Math.pow(n, 1/2);
  if (kok2 !== Math.floor(kok2)) {
    return false;
  }
  
  // Dördüncü kökün tam sayı olup olmadığını kontrol et
  let kok4 = Math.pow(n, 1/4);
  if (kok4 !== Math.floor(kok4)) {
    return false;
  }
  
  // Sekizinci kökün tam sayı olup olmadığını kontrol et
  let kok8 = Math.pow(n, 1/8);
  if (kok8 !== Math.floor(kok8)) {
    return false;
  }
  
  // Tüm kökler tam sayıysa true döndür
  return true;
}