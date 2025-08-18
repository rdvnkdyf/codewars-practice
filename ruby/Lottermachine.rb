def lottery(str)
      # Benzersiz rakamları tutmak için bir dizi oluştururuz.
      # Rakamların ilk görünüm sırasını korumak için bir hash veya set kullanabiliriz.
      # Ama en basit yaklaşım, bir dizi kullanıp her rakamı eklemeden önce
      # dizide olup olmadığını kontrol etmektir.
      unique_integers = []
    
      # Gelen string'i karakterlerine ayırıp her birini döngüye alırız.
      str.each_char do |char|
        # Karakterin bir rakam olup olmadığını kontrol ederiz.
        if char >= '0' && char <= '9'
          # Eğer rakam daha önce unique_integers dizisine eklenmediyse, ekleriz.
          unless unique_integers.include?(char)
            unique_integers << char
          end
        end
      end
    
      # unique_integers dizisi boşsa, "One more run!" mesajını döndürürüz.
      if unique_integers.empty?
        "One more run!"
      else
        # Aksi halde, benzersiz rakamları birleştirip string olarak döndürürüz.
        unique_integers.join
      end
    end