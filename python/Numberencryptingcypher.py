def cypher(s):
    # Harfleri ve karşılık gelen sayıları içeren bir sözlük oluşturuyoruz.
    cypher_map = {
        'I': '1', 'l': '1',
        'R': '2', 'z': '2',
        'E': '3', 'e': '3',
        'A': '4', 'a': '4',
        'S': '5', 's': '5',
        'G': '6', 'b': '6',  # 'G' ve 'b' harfleri 6'ya denk gelir.
        'T': '7', 't': '7',
        'B': '8',
        'g': '9',  # Teste göre 'g' harfi 9'a denk gelir.
        'O': '0', 'o': '0'  # Teste göre 'O' ve 'o' harfleri 0'a denk gelir.
    }

    # Şifrelenmiş dizeyi oluşturmak için boş bir liste kullanıyoruz.
    cyphered_chars = []

    # Dizenin her karakteri üzerinde döngü yapıyoruz.
    for char in s:
        # Karakterin sözlükte olup olmadığını kontrol ediyoruz.
        # Eğer varsa, karşılık gelen sayıyı listeye ekliyoruz.
        if char in cypher_map:
            cyphered_chars.append(cypher_map[char])
        # Eğer yoksa, orijinal karakteri olduğu gibi bırakıyoruz.
        else:
            cyphered_chars.append(char)

    # Listeyi birleştirerek son şifrelenmiş dizeyi döndürüyoruz.
    return "".join(cyphered_chars)
