function validateEAN(eanCode) {
  let sum = 0;
  for (let i = 0; i < 12; i++) {
    const digit = parseInt(eanCode[i]);
    if ((i + 1) % 2 === 1) { // Odd position
      sum += digit * 1;
    } else { // Even position
      sum += digit * 3;
    }
  }

  const checksum = parseInt(eanCode[12]);
  let calculatedChecksum;
  if (sum % 10 === 0) {
    calculatedChecksum = 0;
  } else {
    calculatedChecksum = 10 - (sum % 10);
  }

  return checksum === calculatedChecksum;
}