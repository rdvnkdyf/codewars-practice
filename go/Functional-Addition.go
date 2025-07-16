/*
Create a function add(n)/Add(n) which returns a function that always adds n to any number

Note for Java: the return type and methods have not been provided to make it a bit more challenging.

var addOne = Add(1)
addOne(3) // 4
Note:solved with closures in go
*/

package kata

func Add(int) func(int)int {
  i:=1
return func(int) int{
 i=i+3
 return i
}
}