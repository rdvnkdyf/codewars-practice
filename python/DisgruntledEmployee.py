def off(n):
    # Kapalı kalacak anahtarları saklamak için boş bir liste oluşturun.
    off_switches = []
    
    # 1'den n'nin kareköküne kadar bir döngü oluşturun.
    # Tam kareleri bulmak için i*i işlemini kullanmak daha verimlidir.
    i = 1
    while i * i <= n:
        off_switches.append(i * i)
        i += 1
        
    return off_switches