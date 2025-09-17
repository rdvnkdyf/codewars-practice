def who_is_paying(name)
  # İsim 2 karakterden uzunsa bu koşul çalışır
  if name.length > 2
    [name, name[0, 2]]
  else
    # İsim 2 karakter veya daha kısa ise bu koşul çalışır
    [name]
  end
end