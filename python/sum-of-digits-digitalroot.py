"""
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
"""
def digital_root(n):
    str1=str(n)
    sum=0 
    #First collection 
    for i in range(0,len(str1)):
        sum+=int(str1[i])
    #Return value if less than 10
    if (sum<10):
        return sum 
    #If it is greater than 10 and less than 100, continue the process.
    elif (10<sum and  sum<100):
        str_sum=str(sum)
        sum2=0
        for i in range(len(str_sum)):
            sum2+=int(str_sum[i])
        #However, for the probability that any transaction is greater than 10, we returned the value of the operation performed in one line
        if(10<sum2):
            return int(str(sum2)[0])+int(str(sum2)[1])
        return sum2