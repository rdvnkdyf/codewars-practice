var a1 = "A",
  a2 = "a",
  b1 = "B",
  b2 = "b",
  c1 = "C",
  c2 = "c",
  d1 = "D",
  d2 = "d",
  e1 = "E",
  e2 = "e",
  n1 = "N",
  n2 = "n";

function Dad() {
  return d1 + a2 + d2;
}

function Bee() {
  return b1 + e2 + e2;
}

function banana() {
  return b2 + a2 + n2 + a2 + n2 + a2;
}

// Corrected answers for the questions
function answer1() {
  // Can global variables be modified? 
  // Yes, they can.
  return "yes";
}

function answer2() {
  // Can local variables be modified? 
  // Yes, they can.
  return "yes";
}

function answer3() {
  // Can global variables be invoked by local variables?
  // Yes, they can be accessed from within local scopes.
  return "yes";
}