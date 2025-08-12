function suffixSums(a) {
  const n = a.length;
  const b = new Array(n);
  let suffixSum = 0;

  for (let i = n - 1; i >= 0; i--) {
    suffixSum += a[i];
    b[i] = suffixSum;
  }

  return b;
}