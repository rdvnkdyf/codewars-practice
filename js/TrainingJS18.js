function splitAndMerge(string, separator) {
  // İlk olarak, string'i boşluklara göre kelimelere ayırırız.
  const words = string.split(' ');
  
  // Her bir kelimeyi alıp, karakterlerine ayırırız ve belirtilen ayırıcı ile birleştiririz.
  const mergedWords = words.map(word => {
    return word.split('').join(separator);
  });
  
  // Son olarak, birleştirilmiş kelimeleri tekrar boşluklarla bir araya getirerek bir cümle oluştururuz.
  return mergedWords.join(' ');
}