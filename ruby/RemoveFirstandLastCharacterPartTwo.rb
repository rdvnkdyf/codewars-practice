def array(string)
  # 1. Verilen dizgeyi virgülle ayırarak bir diziye dönüştür.
  arr = string.split(',')

  # 2. Eğer dizi 3'ten az eleman içeriyorsa (boş, tek veya iki elemanlı), nil döndür.
  if arr.length <= 2
    return nil
  end

  # 3. Dizinin ilk ve son elemanını kaldır.
  # Ruby'de `shift` ilk elemanı, `pop` ise son elemanı kaldırır.
  arr.shift
  arr.pop
  
  # 4. Kalan elemanları boşlukla birleştirerek yeni bir dizge döndür.
  arr.join(' ')
end