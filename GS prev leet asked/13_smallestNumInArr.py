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

print(secondSmallesttNum([1,1,2,3,4,5,6]))
print(secondSmallesttNum([10, 9, 8, 7]))