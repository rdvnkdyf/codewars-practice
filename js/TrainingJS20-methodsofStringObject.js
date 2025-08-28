function topSecret(str) {
  let decrypted = "";
  for (let i = 0; i < str.length; i++) {
    let char = str[i];
    let charCode = str.charCodeAt(i);

    // Decrypt uppercase letters
    if (charCode >= 65 && charCode <= 90) {
      charCode = charCode - 3;
      if (charCode < 65) {
        charCode = charCode + 26;
      }
      char = String.fromCharCode(charCode);
    }
    // Decrypt lowercase letters
    else if (charCode >= 97 && charCode <= 122) {
      charCode = charCode - 3;
      if (charCode < 97) {
        charCode = charCode + 26;
      }
      char = String.fromCharCode(charCode);
    }
    
    decrypted += char;
  }
  return decrypted;
}

//question1: The top secret file number is...
answer1 = "2765";
//question2: Super agent's name is...
answer2 = "Hemjr";
//question3: He stole the treasure is...
answer3 = "John's wife";
