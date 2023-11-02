'''
    This uses the record and move on technique...
    Record a number that is closest to the target
'''

def closestNum(target, closest, mid, arr):
    
    if closest == -1 or abs(arr[mid] - target) < abs(arr[closest] - target):
        return mid
    
    return closest

def numClosestToTarget(arr, target):
    closest = -1

    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = start + (end - start) // 2

        closest = closestNum(target, closest, mid, arr)

        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] > target:
            end = mid - 1

        else:
            start = mid + 1

    return arr[closest]

print(numClosestToTarget([1,2,4,5,7,8,9], 6))



    



