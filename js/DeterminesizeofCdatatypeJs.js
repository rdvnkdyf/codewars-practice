function sizeof(type) {
  // Veri tiplerinin boyutlarını içeren bir harita (map) oluşturuyoruz.
  const sizes = {
    "char": 1,
    "unsigned char": 1,
    "short": 2,
    "unsigned short": 2,
    "int": 2,
    "unsigned int": 2,
    "long": 4,
    "unsigned long": 4,
    "long long": 8,
    "unsigned long long": 8,
    "float": 4,
    "double": 8
  };

  // Eğer girdi bir dize (string) ise, ilkel bir veri tipidir.
  // sizes haritasından boyutunu alıp döndürüyoruz.
  if (typeof type === "string") {
    return sizes[type];
  }

  // Eğer girdi bir nesne ise, struct veya union'dır.
  if (typeof type === "object") {
    // Üyelerin boyutlarını saklamak için bir dizi oluşturuyoruz.
    const memberSizes = type.members.map(member => sizeof(member));

    // Eğer yapı (struct) ise, tüm üyelerin boyutlarının toplamını döndürüyoruz.
    if (type.type === "struct") {
      return memberSizes.reduce((sum, size) => sum + size, 0);
    }

    // Eğer birleşim (union) ise, üyelerin en büyük boyutunu döndürüyoruz.
    if (type.type === "union") {
      // Boş bir union'ın boyutu 0'dır.
      return memberSizes.length > 0 ? Math.max(...memberSizes) : 0;
    }
  }

  // Tanımlanmamış bir durum için varsayılan olarak 0 döndürüyoruz.
  return 0;
}