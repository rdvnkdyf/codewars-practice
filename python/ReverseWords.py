def reverse_words(text: str) -> str:
    """
    Bir metindeki her kelimeyi tersine çevirir ve boşlukları korur.

    Args:
        text (str): İşlenecek metin.

    Returns:
        str: Her kelimesi tersine çevrilmiş metin.
    """
    # Metni kelimelere ayır, ancak boşlukları da ayırıcı olarak tutmak için
    # split() metodunu kullanırken boşluk karakterini belirtmeyiz.
    # Ancak bu, ardışık boşlukları tek bir ayırıcı olarak kabul eder.
    # Sorunun gereksinimi olan "boşlukları koruma" için daha iyi bir yaklaşım
    # findall ile kelimeleri ve boşlukları ayrı ayrı bulmaktır.
    
    # Alternatif ve daha temiz bir yol:
    # Metni, bir veya daha fazla boşluk içeren desenle ayırırız.
    # re.split() kullanmak, boşlukları ayırıcı olarak kullanırken
    # boş stringler oluşturacaktır, bu da bize boşlukları koruma imkanı verir.
    import re
    
    # Kelimeleri (alfanümerik karakterler) ve boşlukları ayrı ayrı bulmak için
    # regex kullanılır.
    # (\s+) deseni bir veya daha fazla boşluğu, (\S+) deseni ise boşluk
    # olmayan bir veya daha fazla karakteri (kelime) yakalar.
    parts = re.findall(r'(\s+)|(\S+)', text)
    
    reversed_text = []
    for part_spaces, part_word in parts:
        if part_word:
            # Kelimeyi ters çevir ve listeye ekle
            reversed_text.append(part_word[::-1])
        elif part_spaces:
            # Boşlukları olduğu gibi listeye ekle
            reversed_text.append(part_spaces)
            
    # Tersine çevrilmiş kelimeleri ve boşlukları birleştirerek
    # son metni oluştur
    return "".join(reversed_text)