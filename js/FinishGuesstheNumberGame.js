class Guesser {
  constructor(number, lives) {
    this.number = number;
    this.lives = lives;
  }
  
  guess(n) {
    // Can sayısı 0 veya daha az ise, hata fırlat.
    if (this.lives <= 0) {
      throw new Error("already dead");
    }

    // Tahmin doğruysa true döndür.
    if (n === this.number) {
      return true;
    } else {
      // Tahmin yanlışsa can sayısını bir azalt ve false döndür.
      this.lives--;
      return false;
    }
  }
}