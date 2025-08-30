def is_uppercase(inp):
    """
    Bu fonksiyon, bir dizenin tamamının büyük harf olup olmadığını kontrol eder.
    Büyük harf olmayan herhangi bir harf varsa False, aksi takdirde True döndürür.
    Harf içermeyen dizeler (boşluk, sayılar, semboller) True olarak kabul edilir.
    """
    return inp == inp.upper()