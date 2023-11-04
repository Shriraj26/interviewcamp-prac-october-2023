def moveZeroesToEnd(arr):
    pivot = len(arr) - 1

    for i in range(len(arr)-1, -1, -1):

        if arr[i] == 0:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            pivot -= 1

    print(arr)


arr = [4,2,0,1,0,3,0]

moveZeroesToEnd(arr)
