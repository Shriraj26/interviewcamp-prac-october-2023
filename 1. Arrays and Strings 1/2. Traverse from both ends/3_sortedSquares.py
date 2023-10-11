# ip - [-4, -2, 0, 2, 4]
# op - [0,4,4,16,16]

def sortedSquares(arr):

    start = 0
    end = len(arr) - 1
    result = [0 for i in range(len(arr))]
    resultEndIndex = len(result) - 1

    while start <= end:

        startSq = arr[start] ** 2
        endSq = arr[end] ** 2
        
        # if the start is greater than end
        if startSq > endSq:
            result[resultEndIndex] = startSq
            start += 1
            
        else:
            result[resultEndIndex] = endSq
            end -= 1

        resultEndIndex -= 1
        print(result)

    # print(result)


arr = [-4, -2, 0, 3, 5]

sortedSquares(arr)
