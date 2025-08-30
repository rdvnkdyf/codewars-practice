function grader(score) {
  // Puan 0.6'dan küçükse veya 1'den büyükse "F" döndür.
  if (score < 0.6 || score > 1) {
    return "F";
  } 
  // Puan 0.9 veya daha büyükse "A" döndür.
  else if (score >= 0.9) {
    return "A";
  } 
  // Puan 0.8 veya daha büyükse "B" döndür.
  else if (score >= 0.8) {
    return "B";
  } 
  // Puan 0.7 veya daha büyükse "C" döndür.
  else if (score >= 0.7) {
    return "C";
  } 
  // Puan 0.6 veya daha büyükse "D" döndür.
  else if (score >= 0.6) {
    return "D";
  }
}