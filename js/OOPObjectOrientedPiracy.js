class Ship {
  constructor(draft, crew) {
    this.draft = draft
    this.crew = crew
  }

  
  isWorthIt() {
    // Her mürettebat üyesi geminin ağırlığına 1.5 birim ekler.
    const crewWeight = this.crew * 1.5;
    
    // Mürettebatın ağırlığını çıkararak geminin gerçek ağırlığını (ganimetle birlikte) hesapla.
    const treasureDraft = this.draft - crewWeight;
    
    // Kalan ağırlık 20'den fazlaysa, gemi ganimete değer demektir.
    return treasureDraft > 20;
  }
}

// Codewars'taki testler için sınıfı dışa aktarın.
if (typeof module !== 'undefined' && module.exports) {
  module.exports = Ship;
}