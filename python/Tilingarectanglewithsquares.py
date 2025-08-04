def num_tiles(width,height):
    """
    Kare karolarla bir dikdörtgen alanı kaplamak için gereken minimum karo sayısını hesaplar.
    Karoların kenar uzunlukları 2'nin kuvvetleridir.

    Args:
        width (int): Dikdörtgen alanın genişliği.
        height (int): Dikdörtgen alanın yüksekliği.

    Returns:
        int: Gerekli minimum karo sayısı.
    """
    # Temel Durum: Alan kaplanmışsa veya geçersizse 0 döndür.
    if width <= 0 or height <= 0:
        return 0

    # Tutarlı bir mantık için her zaman width'in height'tan büyük veya eşit olmasını sağla.
    if width < height:
        width, height = height, width

    # Alanın kısa kenarına (height) sığan en büyük 2'nin kuvvetini bul.
    # Bu, kullanabileceğimiz en büyük kare karonun boyutudur.
    s = 1
    while s * 2 <= height:
        s *= 2

    # Bu en büyük karodan kaç tane sığabileceğini hesapla.
    # Bu, ana bloktan gelen karo sayısıdır.
    # Örn: 13x11 için s=8. Ana blok (13//8)x(11//8) = 1x1'lik bir alandır.
    count = (width // s) * (height // s)

    # Geriye kalan alanlar için özyinelemeli çağrılar yap.
    # Ana blok yerleştirildikten sonra iki adet kalan dikdörtgen alan oluşur:

    # 1. Ana bloğun sağında kalan dikey şerit: (width % s) x height
    count += num_tiles(width % s, height)

    # 2. Ana bloğun altında kalan yatay şerit: (s * (width // s)) x (height % s)
    count += num_tiles(s * (width // s), height % s)

    return count