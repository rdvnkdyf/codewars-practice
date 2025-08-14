function validate(username, password){
  // Check if the password contains malicious characters.
  if (password.includes("||") || password.includes("//")) {
    // If it does, return the error message immediately.
    return "Wrong username or password!";
  } else {
    // Otherwise, proceed with the normal login process.
    var database = new Database();
    return database.login(username, password);
  }
}