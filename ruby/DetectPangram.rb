def pangram?(string)
  ('a'..'z').all? { |letter| string.downcase.include?(letter) }
end