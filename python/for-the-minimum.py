"""
Task
Given a list of digits, return the smallest number that could be formed from these digits, using the digits only once (ignore duplicates).

Notes:
Only positive integers will be passed to the function (> 0 ), no negatives or zeros.
Input >> Output Examples
minValue ({1, 3, 1})  ==> return (13)

Explanation:
(13) is the minimum number could be formed from {1, 3, 1} , Without duplications
minValue({5, 7, 5, 9, 7})  ==> return (579)

Explanation:
(579) is the minimum number could be formed from {5, 7, 5, 9, 7} , Without duplications

minValue({1, 9, 3, 1, 7, 4, 6, 6, 7}) return  ==> (134679)

Explanation:
(134679) is the minimum number could be formed from {1, 9, 3, 1, 7, 4, 6, 6, 7} , Without duplications
"""

def min_value(digits):
    # your code here
    str1=""
    digits.sort()
    print (digits)
    length_digits=len(digits)
    for i in range(0,length_digits):
        if(i==length_digits-1):
            str1+=str(digits[i])
            break 
        if (digits[i]!=digits[i+1]):
            str1+=str(digits[i])
        else:
            continue 
    return int(str1)

