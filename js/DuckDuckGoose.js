function duckDuckGoose(players, goose) {
  // Dizideki oyuncu sayısını buluyoruz.
  const playerCount = players.length;

  // Modulo operatörünü kullanarak pozisyonun dizideki indeksini buluyoruz.
  // Oyuncular 1'den başladığı için, goose - 1 yaparak 0 tabanlı indekse çeviriyoruz.
  const chosenIndex = (goose - 1) % playerCount;

  // Seçilen oyuncunun adını döndürüyoruz.
  return players[chosenIndex].name;
}
