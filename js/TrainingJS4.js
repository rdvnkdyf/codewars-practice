function getLength(arr){
  // Dizinin uzunluğunu döndürür.
  return arr.length;
}

function getFirst(arr){
  // Dizinin ilk elemanını döndürür.
  return arr[0];
}

function getLast(arr){
  // Dizinin son elemanını döndürür.
  return arr[arr.length - 1];
}

function pushElement(arr){
  var el=1;
  // 'el' değişkenini dizinin sonuna ekler.
  arr.push(el);
  return arr;
}

function popElement(arr){
  // Dizinin son elemanını çıkarır ve onu döndürür.
  arr.pop();
  return arr;
}