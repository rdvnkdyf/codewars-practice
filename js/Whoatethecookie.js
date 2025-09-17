function cookie(x) {
  let name;

  // Verinin tipini kontrol et
  if (typeof x === 'string') {
    name = 'Zach';
  } else if (typeof x === 'number') {
    name = 'Monica';
  } else {
    name = 'the dog';
  }

  // Sonuç dizgesini döndür
  return `Who ate the last cookie? It was ${name}!`;
}