def get_size(w: int, h: int, d: int) -> list[int, int]:
    """
    Bir kutunun toplam yüzey alanını ve hacmini hesaplar.

    Args:
        w (int): Kutunun genişliği.
        h (int): Kutunun yüksekliği.
        d (int): Kutunun derinliği.

    Returns:
        list[int, int]: [toplam yüzey alanı, hacim] şeklinde iki elemanlı bir liste.
    """
    # Hacim = genişlik * yükseklik * derinlik
    volume = w * h * d

    # Yüzey Alanı = 2 * (genişlik*yükseklik + genişlik*derinlik + yükseklik*derinlik)
    surface_area = 2 * (w * h + w * d + h * d)

    # İki değeri bir liste olarak döndür.
    return [surface_area, volume]