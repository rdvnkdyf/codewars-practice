def clonewars(kata_per_day):
    if kata_per_day <= 0:
        return [1, 0]

    num_clones = 1
    total_katas_solved = 0
    
    # Klonların yeteneği azaldığı için, kata çözme işlemi
    # `kata_per_day`'den 1'e kadar her gün devam eder.
    # Döngüyü `kata_per_day` gün boyunca çalıştıracağız.
    for i in range(kata_per_day):
        # Yetenek, her gün bir azalır.
        current_kata_ability = kata_per_day - i
        
        # Mevcut klonlar, o günkü yetenekleri kadar kata çözer.
        katas_solved_today = num_clones * current_kata_ability
        total_katas_solved += katas_solved_today
        
        # Klonlar, yetenekleri 1'in üzerinde olduğu sürece klonlama yapabilirler.
        # Bu, son gün hariç her gün klonlama yapıldığı anlamına gelir.
        if current_kata_ability > 1:
            num_clones *= 2
    
    return [num_clones, total_katas_solved]