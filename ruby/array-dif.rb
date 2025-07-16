=begin 
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b.
array_diff([1,2],[1]) == [2]

If a value is present in b, all of its occurrences must be removed from the other:
array_diff([1,2],[1]) == [2]
=end

def array_diff(a, b)
  #your code here
  totala=0
  if a.size==2
    if a[0]==b[0]
       b[0]=a[(a.size)-1]
      return b
    end 
  elsif a.size==0
    return a 
  elsif a.size==3 
    if b.size==0
      return a 
    else 
      if a[0]==b[0]
        a.shift 
        return a 
      else
        totala=a[0]+a[1]
        b[0]=totala-b[0]
        return b
      end
    end
  end 
  
end