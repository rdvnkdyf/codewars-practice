def two_highest(list)
  # Eğer liste boşsa, hemen boş bir dizi döndür.
  if list.empty?
    return []
  end

  # uniq metodu ile listedeki yinelenen elemanları kaldır.
  # Ardından, sort metodu ile en yüksekten en düşüğe doğru sırala
  # ve ilk iki elemanı al.
  # take(2) metodu, dizinin ilk iki elemanını döndürür.
  list.uniq.sort.reverse.take(2)
end
