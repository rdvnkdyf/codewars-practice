def generate_pairs(n)
  # Sonuçları depolamak için boş bir dizi oluşturulur.
  pairs = []

  # Dış döngü 'a' değişkeni için 0'dan n'ye kadar döner.
  (0..n).each do |a|
    # İç döngü 'b' değişkeni için 'a'dan n'ye kadar döner.
    # Bu, her zaman a <= b koşulunu sağlar.
    (a..n).each do |b|
      # Koşulu sağlayan [a, b] çifti diziye eklenir.
      pairs << [a, b]
    end
  end

  # Çiftleri içeren diziyi döndürür.
  return pairs
end