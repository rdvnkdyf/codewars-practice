class SiegeState {
  constructor() {
    this.canMove = false;
    this.damage = 20;
  }
}

class TankState {
  constructor() {
    this.canMove = true;
    this.damage = 5;
  }
}

class Tank {
  constructor() {
    // Tankın başlangıç durumunu TankState olarak ayarlayın
    this.state = new TankState();
  }

  get canMove() {
    // Mevcut durum nesnesinin canMove özelliğini döndürür
    return this.state.canMove;
  }

  get damage() {
    // Mevcut durum nesnesinin damage özelliğini döndürür
    return this.state.damage;
  }
}