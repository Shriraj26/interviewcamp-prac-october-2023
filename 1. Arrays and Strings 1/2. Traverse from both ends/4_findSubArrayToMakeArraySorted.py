import sys

def findMin(arr):
    minElem = sys.maxsize
    for elem in arr:
        minElem = min(minElem, elem)

    return minElem    

    

def findMax(arr):
    maxElem = - sys.maxsize
    for elem in arr:
        maxElem = max(maxElem, elem)
    
    return maxElem
    

def findBump(arr):

    for i in range(len(arr)-1, 0, -1):
        if arr[i] < arr[i-1]:
            return i

def findDip(arr):

    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return i


def findSubArrToMakeEntireArrSorted(arr):

    # Find the first dip from start
    dip = findDip(arr)

    # Find the first bump from end
    bump = findBump(arr)

    # Find min and max in the subarray dip to start
    minElem = findMin(arr[dip: bump + 1])
    maxElem = findMax(arr[dip: bump + 1])
    
    start = 0
    end = 0

    # Go left to include elements greater than the min 
    for i in range(dip, -1, -1):
        if arr[i] < minElem:
            start = i+1
            break

    # Go right to incluse elements less than the max
    for i in range(bump, len(arr)):
        if arr[i] > maxElem:
            end = i - 1
            break

    print(arr[start: end + 1])

    
findSubArrToMakeEntireArrSorted([1,2,4,5,3,7,5,6,8])