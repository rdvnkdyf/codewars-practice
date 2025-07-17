def logical_calculator(booleans, operator):


    # Eğer dizi boşsa hata fırlatıyoruz. Problemde en az 1 eleman olacağı belirtilmiş olsa da,
    # bu tür kontroller iyi bir programlama pratiğidir.
    if not booleans:
        raise ValueError("Giriş dizisi boş olamaz.")

    # Dizinin ilk elemanını başlangıç sonucumuz olarak belirliyoruz.
    result = booleans[0]

    # Dizinin ikinci elemanından başlayarak (indeks 1) diğer elemanlar üzerinde dönüyoruz.
    for i in range(1, len(booleans)):
        current_value = booleans[i] # Dizinin mevcut elemanı

        # Belirtilen operatöre göre mantıksal işlemi uyguluyoruz.
        if operator == "AND":
            result = result and current_value
        elif operator == "OR":
            result = result or current_value
        elif operator == "XOR":
            # Python'da XOR işlemi için '^' operatörü kullanılır.
            result = result ^ current_value
        else:
            # Geçersiz bir operatör girildiğinde hata fırlatıyoruz.
            raise ValueError("Geçersiz operatör. 'AND', 'OR' veya 'XOR' olmalıdır.")

    # Tüm işlemler bittikten sonra nihai sonucu döndürüyoruz.
    return result