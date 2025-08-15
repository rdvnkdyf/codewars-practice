function hello(name) {
  if (!name) {
    return 'Hello, World!';
  } else {
    name = name.toLowerCase();
    return 'Hello, ' + name.charAt(0).toUpperCase() + name.slice(1) + '!';
  }
}