def get_score(arr) -> int:
        """
        Nintendo Tetris puanlama sistemine göre oyunun son puanını hesaplar.
        
        Args:
            arr: Temizlenen satır sayısını içeren bir dizi.
        
        Returns:
            int: Hesaplanmış toplam puan.
        """
        score = 0
        level = 0
        cleared_lines_total = 0
    
        # Dizi elemanları üzerinde döngü yap
        for lines in arr:
            # Toplam temizlenen satır sayısını güncelle
            cleared_lines_total += lines
            
            # Puanı hesapla ve skora ekle
            # Puan formülü: (seçilen satır puanı) * (seviye + 1)
            if lines == 1:
                score += 40 * (level + 1)
            elif lines == 2:
                score += 100 * (level + 1)
            elif lines == 3:
                score += 300 * (level + 1)
            elif lines == 4:
                score += 1200 * (level + 1)
            
            # Seviye atlamasını kontrol et ve seviyeyi artır
            level = cleared_lines_total // 10
            
        return score