'''
    start, end and mid, inc start dec mid and then see how it goes...
'''

def binSearch(arr, target):

    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = start + (end - start) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1

        else:
            end = mid - 1

    return -1


print(binSearch([1,2,3,4,5,6,7], 7))
