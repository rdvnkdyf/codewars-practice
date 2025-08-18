def card_game(card1, card2, trump)
      # Kartların sıralamasını belirleyen bir hash oluşturuyoruz
      # 'joker' en yüksek değere sahiptir, bu yüzden en üste yerleştiriyoruz.
      # Normal kartlar için değer sıralaması: 2 < ... < 10 < J < Q < K < A
      card_rankings = {
        '2' => 2, '3' => 3, '4' => 4, '5' => 5, '6' => 6, '7' => 7, '8' => 8,
        '9' => 9, '10' => 10, 'J' => 11, 'Q' => 12, 'K' => 13, 'A' => 14,
        'joker' => 15 # Joker her zaman kazanır
      }

      # Fonksiyonun temel adımları:
      # 1. Aynı kartlar mı kontrolü
      if card1 == card2
        return "Someone cheats."
      end

      # 2. Joker kontrolü
      if card1 == "joker"
        return "The first card won."
      end
      if card2 == "joker"
        return "The second card won."
      end

      # 3. Kartların türlerini ve değerlerini ayrıştırma
      # Son karakter kartın türünü belirtir (♣, ♦, ♥, ♠)
      suit1 = card1[-1]
      suit2 = card2[-1]
      
      # Kartın değerini (rank) bulmak için, son karakter hariç tüm stringi alırız
      rank1 = card1[0..-2]
      rank2 = card2[0..-2]

      # 4. Oyun kurallarını uygulama
      # Durum 1: Her iki kart da koz türünde (trump)
      if suit1 == trump && suit2 == trump
        if card_rankings[rank1] > card_rankings[rank2]
          return "The first card won."
        else
          return "The second card won."
        end
      end

      # Durum 2: Sadece bir kart koz türünde
      if suit1 == trump
        return "The first card won."
      end
      if suit2 == trump
        return "The second card won."
      end
      
      # Durum 3: Kartlar farklı türde ve hiçbiri koz değil
      if suit1 != suit2
        return "Let us play again."
      end

      # Durum 4: Kartlar aynı türde (ama koz değil)
      if suit1 == suit2
        if card_rankings[rank1] > card_rankings[rank2]
          return "The first card won."
        else
          return "The second card won."
        end
      end
      
      # Hiçbir koşul karşılanmazsa, kural dışı bir durum oluşmuştur
      # Bu duruma ulaşılmamalıdır, ancak her olasılığı ele almak için bir dönüş değeri ekliyoruz
      return "Oyun kuralları dışında bir durum oluştu."
    end