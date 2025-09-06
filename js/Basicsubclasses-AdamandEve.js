class Human {
  constructor() {
    this.species = "Homo sapiens";
  }
}

/**
 * Erkek insanları temsil eden alt sınıf (subclass).
 * Human sınıfından kalıtım alır.
 */
class Man extends Human {
  constructor() {
    super();
    this.gender = "male";
  }
}

/**
 * Kadın insanları temsil eden alt sınıf (subclass).
 * Human sınıfından kalıtım alır.
 */
class Woman extends Human {
  constructor() {
    super();
    this.gender = "female";
  }
}

/**
 * God sınıfı, Adem ve Havva'yı yaratmak için bir fabrika görevi görür.
 */
class God {
  /**
   * Adem ve Havva'yı yaratır ve bir dizi içinde döndürür.
   * Adem dizideki ilk insan, Havva ise ikinci insandır.
   * @returns {Human[]}
   */
  static create() {
    const adam = new Man();
    const eve = new Woman();
    return [adam, eve];
  }
}

// Sınıfları test ortamında kullanılabilir hale getirmek için dışa aktarın.
// Bu kısım, Codewars'taki testler için gereklidir.
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { Human, Man, Woman, God };
}
