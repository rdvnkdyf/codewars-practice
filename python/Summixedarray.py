def sum_mix(arr):
    """
    Bir dizideki tam sayıları ve sayısal dizeleri toplar.

    :param arr: İçerisinde hem int hem de str tipinde sayısal değerler bulunan liste.
    :return: Tüm değerlerin sayı olarak toplamı (int).
    """
    # Toplamı tutmak için bir değişken başlat
    total = 0
    
    # Dizideki her bir öğe üzerinde döngü
    for item in arr:
        # Öğeyi bir tamsayıya dönüştür ve toplam değişkene ekle
        # int() fonksiyonu hem sayıları hem de sayısal dizeleri tamsayıya çevirir
        total += int(item)
    
    # Hesaplanan toplamı döndür
    return total