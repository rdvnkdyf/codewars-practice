def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return "INVALID"

    # m'den küçük n'nin katlarını liste anlama (list comprehension) ile oluştur
    # ve sonra sum() fonksiyonu ile topla.
    # range(n, m, n) ifadesi, n'den başlayıp m'ye kadar (m dahil değil) n adımlarla ilerler.
    # Bu da bize doğrudan n'nin katlarını verir.
    return sum(range(n, m, n))