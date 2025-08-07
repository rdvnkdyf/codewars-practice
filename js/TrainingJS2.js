let v1 = 50,
    v2 = 100,
    v3 = 150,
    v4 = 200,
    v5 = 2,
    v6 = 250;

function equal1(){
  let a = v1,   // v1 = 50
      b = v1;   // v1 = 50
  return a + b; // 50 + 50 = 100
}

// Lütfen yukarıdaki örneğe bakarak aşağıdaki fonksiyonları tamamlayın
function equal2(){
  let a = v3,  // v3 = 150
      b = v1;  // v1 = 50
  return a - b; // 150 - 50 = 100
}

function equal3(){
  let a = v1,  // v1 = 50
      b = v5;  // v5 = 2
  return a * b; // 50 * 2 = 100
}

function equal4(){
  let a = v4,  // v4 = 200
      b = v5;  // v5 = 2
  return a / b; // 200 / 2 = 100
}

function equal5(){
  let a = v6,  // v6 = 250
      b = v3;  // v3 = 150
  return a % b; // 250 % 150 = 100
}
