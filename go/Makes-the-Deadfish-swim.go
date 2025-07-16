/*
Write a simple parser that will parse and run Deadfish.

Deadfish has 4 commands, each 1 character long:

i increments the value (initially 0)
d decrements the value
s squares the value
o outputs the value into the return array
Invalid characters should be ignored.

Parse("iiisdoso") == []int{8, 64}

*/

package kata

func Parse(data string) []int{
  //TODO: write your code here
  var sum int=0
  var reto [] int 
  for i:=0;i<len(data);i++{
    if string(data[i])=="i"{
      sum=sum+1
    }else if string(data[i])=="d"{
      sum=sum-1
    }else if string(data[i])=="s"{
      sum=sum*sum
    }else if string(data[i])=="o"{
      reto=append(reto,sum)
    }else{
      continue
    }
  }
  return reto
}

