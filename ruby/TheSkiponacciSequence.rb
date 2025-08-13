def skiponacci(n)
  if n == 1
    return "1"
  end

  fib = [0, 1]
  while fib.length < n + (n / 2)
    fib << fib[-1] + fib[-2]
  end
  
  result = []
  (1..n).each do |i|
    if i.odd?
      result << fib[i].to_s
    else
      result << "skip"
    end
  end
  
  return result.join(" ")
end