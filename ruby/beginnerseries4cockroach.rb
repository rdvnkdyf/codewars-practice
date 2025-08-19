def cockroach_speed(s)
  # 1 km = 100000 cm
  # 1 saat = 3600 saniye
  # Bu nedenle, km/saat'ten cm/saniye'ye dönüştürme faktörü:
  # (100000 cm / 3600 saniye) = 250 / 9
  # Bu işlemi yapmak için float değerleri kullanmak önemlidir.

  # Hızı cm/saniye cinsine dönüştür ve tam sayıya yuvarla.
  # to_i metodu, sayıyı kesirli kısmını atarak tam sayıya dönüştürür.
  (s * 100000 / 3600).to_i
end