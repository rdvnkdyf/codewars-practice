/*
Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).
*/

package kata
import("math")
func IsTriangle(a, b, c int) bool {
      var a1 float64 = float64(a)
      var b1 float64 = float64(b)
      var c1 float64 = float64(c)
     if (math.Abs(b1-c1)<a1 && a1<math.Abs(b1+c1))&&(math.Abs(a1-c1)<b1 && b1<math.Abs(a1+c1))&&(math.Abs(a1-b1)<c1 && c1<math.Abs(a1+b1)){
       return true
       
     }
     return false
}

