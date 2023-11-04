def moveZeroesToStart(arr):

    pivot = 0

    for i in range(len(arr)):

        if arr[i] == 0:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            pivot += 1

    print(arr)

arr = [4,2,0,1,0,3,0]
moveZeroesToStart(arr)


    