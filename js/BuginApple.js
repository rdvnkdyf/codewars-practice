function sc(apple) {
  for (let y = 0; y < apple.length; y++) {
    for (let x = 0; x < apple[y].length; x++) {
      if (apple[y][x] === 'B') {
        return [y, x];
      }
    }
  }
}
