function animal(obj) {
  return `This ${obj.color} ${obj.name} has ${obj.legs} legs.`;
}

// Örnek kullanım:
const myAnimal = {
  name: "dog",
  legs: 4,
  color: "white"
};

const sentence = animal(myAnimal);
console.log(sentence); // "This white dog has 4 legs."