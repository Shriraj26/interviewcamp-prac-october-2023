# ip - [-4, -2, 0, 2, 4]
# op - [0,4,4,16,16]

def sortedSquares(arr):

    start = 0
    end = len(arr) - 1
    newArr = []

    while start <= end:

        if abs(arr[start]) > abs(arr[end]):
            newArr.append(arr[start] ** 2)
            start += 1
        else:
            newArr.append(arr[end] ** 2)
            end -= 1

    print(newArr[::-1])

arr = [-4, -2, -1, 0, 3, 5]
sortedSquares(arr)

