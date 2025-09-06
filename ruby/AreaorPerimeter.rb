def area_or_perimeter(l, w)
  # Eğer uzunluk ve genişlik eşitse, şekil bir karedir.
  # Bu durumda alanını (l * w) hesaplayıp döndürür.
  if l == w
    return l * w
  # Aksi takdirde, şekil bir dikdörtgendir.
  # Bu durumda çevresini (2 * (l + w)) hesaplayıp döndürür.
  else
    return 2 * (l + w)
  end
end