def remove_every_other(arr)
  # Yeni bir dizi oluşturmak için bir döngü kullanabilir veya Ruby'nin
  # yerleşik fonksiyonlarından birini kullanabiliriz.
  
  # Yöntem 1: Döngü (each_with_index)
  # Döngü içinde her elemanın dizinini kontrol ederiz.
  result = []
  arr.each_with_index do |element, index|
    result << element if index.even?
  end
  result
  
  # Yöntem 2: select (daha Ruby-vari)
  # Bu yöntem, koşula uyan elemanları seçerek yeni bir dizi oluşturur.
  # arr.select.each_with_index do |element, index|
  #   index.even?
  # end

  # Yöntem 3: En kısa ve en yaygın kullanılan yöntem
  # select metodu, döngü yapısına ihtiyaç duymadan koşullu seçim yapmanızı sağlar.
  # arr.select.with_index { |_, i| i.even? }
  # veya
  # arr.select.with_index { |_, i| i % 2 == 0 }

  # Yöntem 4: Alternatif olarak `step` metodu
  # Bu yöntem, dizinin belli bir adımla elemanlarını seçmek için kullanılabilir.
  # arr.select.with_index do |_, i|
  #   i.step(by: 2).include?(i)
  # end
end