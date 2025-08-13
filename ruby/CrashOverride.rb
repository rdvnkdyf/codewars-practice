def alias_gen(first_name, surname)
  first_initial = first_name[0]
  surname_initial = surname[0]
  
  if first_initial.match?(/[A-Za-z]/) && surname_initial.match?(/[A-Za-z]/)
    first_initial_upcase = first_initial.upcase
    surname_initial_upcase = surname_initial.upcase
    
    first_alias = FIRST_NAME[first_initial_upcase]
    surname_alias = SURNAME[surname_initial_upcase]
    
    return "#{first_alias} #{surname_alias}"
  else
    return "Your name must start with a letter from A - Z."
  end
end