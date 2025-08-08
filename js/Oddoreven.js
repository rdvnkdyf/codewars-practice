function oddOrEven(array) {
  // Dizinin boş olması durumunda [0] olarak kabul et
  if (array.length === 0) {
    array = [0];
  }

  // Tüm elemanların toplamını bul
  const sum = array.reduce((accumulator, currentValue) => accumulator + currentValue, 0);

  // Toplamın tek mi çift mi olduğunu kontrol et
  if (sum % 2 === 0) {
    return "even";
  } else {
    return "odd";
  }
}