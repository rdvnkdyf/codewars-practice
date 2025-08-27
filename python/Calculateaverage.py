def find_average(numbers):
    # Dizi boşsa, 0 döndür.
    if not numbers:
        return 0
    
    # Sayıların toplamını hesapla.
    total = sum(numbers)
    
    # Toplamı eleman sayısına bölerek ortalamayı bul.
    return total / len(numbers)