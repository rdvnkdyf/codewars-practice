def remove_char(s):
    # s[1:-1] dilimlemesi, dizenin ilk karakterini (indeks 0) ve son karakterini (indeks -1) atlar.
    # Sonuç olarak, ilk ve son karakterler hariç tüm dizeyi döndürür.
    # Eğer dizenin uzunluğu 2 ise, bu dilimleme boş bir dize ("") döndürür,
    # bu da gereksinimi karşılar.
    return s[1:-1]