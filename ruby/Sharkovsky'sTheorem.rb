def sharkovsky(a, b)
  # Sayıları 2^k * m şeklinde ayrıştırır (m tek sayıdır).
  def decompose(n)
    power_of_2 = 0
    while n > 0 && n % 2 == 0
      n /= 2
      power_of_2 += 1
    end
    [power_of_2, n]
  end

  # a ve b'yi ayrıştırıyoruz
  power_a, odd_a = decompose(a)
  power_b, odd_b = decompose(b)

  # Sayılar eşitse, a ≺ b koşulu sağlanmaz.
  return false if a == b

  # Durum 1: Her iki sayı da tekse (2'nin kuvveti 0'dır).
  # Örnek: 3 ≺ 5. Küçük olan sayı daha önce gelir.
  if odd_a > 1 && odd_b > 1 && power_a == 0 && power_b == 0
    return a < b
  end

  # Durum 2: a tek, b çift.
  # Tek sayılar sıralamanın en başındadır. a ≺ b doğrudur.
  if odd_a > 1 && power_a == 0 && (power_b > 0 || odd_b == 1)
    return true
  end

  # Durum 3: a çift, b tek.
  # b sıralamanın en başındadır. a ≺ b yanlıştır.
  if (power_a > 0 || odd_a == 1) && odd_b > 1 && power_b == 0
    return false
  end

  # Durum 4: Her iki sayı da 2'nin kuvveti değilse.
  # Örnek: 2*3 ≺ 4*3. Önce 2'nin kuvveti küçük olan gelir.
  if odd_a > 1 && odd_b > 1 && power_a != power_b
    return power_a < power_b
  end
  
  # 2'nin kuvvetleri eşitse, tek çarpanlar karşılaştırılır.
  # Örnek: 2*3 ≺ 2*5. Küçük olan tek çarpan önce gelir.
  if odd_a > 1 && odd_b > 1 && power_a == power_b
    return odd_a < odd_b
  end

  # Durum 5: a 2'nin kuvveti, b değil.
  # 2'nin kuvvetleri en sonda yer alır. Bu durumda a ≺ b yanlıştır.
  if odd_a == 1 && odd_b > 1
    return false
  end

  # Durum 6: b 2'nin kuvveti, a değil.
  # a 2'nin kuvveti olmadığından sıralamada b'den önce gelir.
  if odd_a > 1 && odd_b == 1
    return true
  end

  # Durum 7: Her iki sayı da 2'nin saf kuvvetleriyse.
  # Örnek: 8 ≺ 4 ≺ 2. Küçük kuvvet (büyük sayı) daha sonra gelir.
  if odd_a == 1 && odd_b == 1
    return power_a > power_b
  end
end