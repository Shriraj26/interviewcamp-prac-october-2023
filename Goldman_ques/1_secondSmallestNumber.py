'''
TC - O(n)
SC - O(1) as only 2 variables first and second
'''
import sys
def secondSmallesttNum(arr):
    
    first = sys.maxsize
    second = sys.maxsize

    for elem in arr:

        if elem <= first:
            second = first
            first = elem
        elif first < elem and elem < second:
            second = elem
        

    return second


print(secondSmallesttNum([1,4,3,2,1])) # With repeating smaller number
print(secondSmallesttNum([1,4,3,2,6])) # non repeating
    