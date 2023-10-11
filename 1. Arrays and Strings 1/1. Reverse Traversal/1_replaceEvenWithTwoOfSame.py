def replaceEvenWithTwoOfSame(arr):

    start = findLastIndex(arr)
    end = len(arr) - 1

    while start >= 0:

        # if the elem is even, replace it twice with end index
        if arr[start] % 2 == 0:
            arr[end] = arr[start]
            end -= 1
            arr[end] = arr[start]
            end -= 1
        # if elem is odd, replace it just once
        else:
            arr[end] = arr[start]
            end -= 1
        
        start -= 1
    
    print(arr)


# Finds the last index of array where it is not -1
def findLastIndex(arr):
    
    for i in range(len(arr)-1, -1, -1):
        if arr[i] != -1:
            return i


# arr = [1,2,3,4,5,-1,-1]

# arr = [1]

# arr = [2,2,2,-1,-1,-1]

arr = [1,2,3,4,5,-1,-1]

replaceEvenWithTwoOfSame(arr)





