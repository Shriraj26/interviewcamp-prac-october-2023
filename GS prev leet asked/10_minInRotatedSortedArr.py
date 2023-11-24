def minInRotatedSortedArr(arr):
    if len(arr) == 0:
        return -1

    lastElem = arr[-1]

    start = 0
    end = len(arr)-1
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] > lastElem:
            start = mid + 1
        
        elif arr[mid] < lastElem and (mid > 0 and arr[mid-1] < arr[mid]):
            end = mid - 1
        else:
            return mid

print(minInRotatedSortedArr([1,2,3,4,5,6]))

print(minInRotatedSortedArr([2, 3, 4, 5, 6, 1]))

print(minInRotatedSortedArr([5, 6, 1, 2, 3, 4]))

print(minInRotatedSortedArr([6, 1, 2, 3, 4,5]))