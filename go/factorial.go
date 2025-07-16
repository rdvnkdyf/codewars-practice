/*
Yor task is to write function factorial

https://en.wikipedia.org/wiki/Factorial
*/
package kata

func Factorial(n int) int {
	// put your code here
  var carpim int =1
  for i:=1;i<n+1;i++{
    carpim=carpim*i
  }
  return carpim
}

