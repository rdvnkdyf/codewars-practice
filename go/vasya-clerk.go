/*
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?

Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.

Examples:
Tickets([]int{25, 25, 50}) // => YES
Tickets([]int{25, 100}) // => NO. Vasya will not have enough money to give change to 100 dollars
Tickets([]int{25, 25, 50, 50, 100}) // => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)
*/
package kata

func Tickets(peopleInLine []int) string {
  	// Do the magic
    var sum int=0
   for i:=0;i<len(peopleInLine);i++{
     if peopleInLine[i]==25{
       sum=sum+25
     }else if peopleInLine[i]==50{
       if(sum>25){
         sum=sum-25
       }else{
         return "NO"
       }
     }else if peopleInLine[i]==100{
       if(sum>75){
         sum=sum-75
       }else{
         return "NO"
       }
     }
   }
  	return "YES"
}
