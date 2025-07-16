/*
Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings. 
All words must have their first letter capitalized without spaces.
For instance:

CamelCase("hello case")      // => "HelloCase"
CamelCase("camel case word") // => "CamelCaseWord"
Don't forget to rate this kata! Thanks :)

*/

package kata
import("strings")
func CamelCase(s string) string {
    // your code here
     res := strings.Title(s)
     res1:=strings.ReplaceAll(res, " ", "")
    return res1
}

