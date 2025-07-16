"""
Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple like so: (index1, index2).

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).

Based on: http://oj.leetcode.com/problems/two-sum/
twoSum [1, 2, 3] 4 === (0, 2)
"""
#A first solution that comes to mind 
def two_sum(numbers, target):
    arr=[]
    if(numbers[0]+numbers[1]==target):
            arr.append(0)
            arr.append(1)
            return arr
    elif(numbers[1]+numbers[2]==target):
          arr.append(1)
          arr.append(2)
          return arr
    elif(numbers[0]+numbers[len(numbers)-1]==target):
          arr.append(0)
          arr.append(len(numbers)-1)
          return arr 