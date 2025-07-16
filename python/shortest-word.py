"""
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""
def find_short(s):
    li = list(s.split(" "))
    length_array=[]
    for i in range(0,len(li)):
        length_array.append(len(li[i]))
    
    return min(length_array)

