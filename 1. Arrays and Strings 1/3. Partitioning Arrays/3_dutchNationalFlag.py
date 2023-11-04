"""
Things to take care of - 
    1. Declare a index which will traverse the aray
    2. index will loop from 0 to end, and not the length of the array!!!
    3. if arr elem greater than pivot, then swap then dont increase the pivot 
        as we have to process the swapped elem later on!!
"""

def dutchNationalFlag(arr, pivot):

    start = 0
    end = len(arr) - 1
    index = 0

    while index < end:

        if arr[index] < pivot:
            arr[index], arr[start] = arr[start], arr[index]
            start += 1
            index += 1
        elif arr[index] > pivot:
            arr[index], arr[end] = arr[end], arr[index]
            end -= 1
        else:
            index += 1

    print(arr)
    
dutchNationalFlag([5,2,4,4,6,4,4,3], 4)