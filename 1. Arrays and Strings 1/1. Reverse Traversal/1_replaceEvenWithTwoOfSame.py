def replaceArrayOddEven(arr):

    # Find the last index of array from where it is not -1
    start = findLastIndex(arr)
    end = len(arr) - 1


    # Loop the array in reverse
    while start >= 0:

        # For even numbers, replace it twice!
        if arr[start] % 2 == 0:
            arr[end] = arr[start]
            end -= 1
            arr[end] = arr[start]
            end -= 1
        
        else:
            arr[end] = arr[start]
            end -= 1

        start -= 1


    print(arr)


def findLastIndex(arr):

    for i in range(len(arr)-1, -1, -1):
        if arr[i] != -1:
            return i
        

replaceArrayOddEven([1,2,5,6,8,-1,-1,-1])
