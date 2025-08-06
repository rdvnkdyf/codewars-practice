function alphanumeric(string) {
  // The regular expression `^[a-zA-Z0-9]+$` checks for the following:
  // ^: Asserts the start of the string.
  // [a-zA-Z0-9]: Matches any uppercase letter (A-Z), lowercase letter (a-z), or digit (0-9).
  // +: Ensures that there is one or more of the allowed characters. This handles
  //    the "at least one character" requirement and implicitly excludes empty strings.
  // $: Asserts the end of the string. This ensures that no other characters (like
  //    whitespaces or underscores) are present anywhere in the string.
  return /^[a-zA-Z0-9]+$/.test(string);
}