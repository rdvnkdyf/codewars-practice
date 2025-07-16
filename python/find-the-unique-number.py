"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

Find the unique number (this kata)
Find the unique string
Find The Unique
"""
def find_uniq(arr):
    # your code here
    sum1=sum(arr)
    piece=0
    result=0
    arr.sort()
    for i in range(len(arr)):
        if(arr[i]==arr[i+1]):
                  piece+=1
        #a simple solution, but if it satisfies 3, it can satisfy this condition.
        if(piece==3):
            break
        
        
    
    if(piece==3):
        result=sum1-(arr[0]*(len(arr)-1))
    
    return result
        
