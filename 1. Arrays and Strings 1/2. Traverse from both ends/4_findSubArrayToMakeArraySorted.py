import sys

def findMin(arr):
    minNum = sys.maxsize
    for elem in arr:
        if elem < minNum:
            minNum = elem

    return minNum

def findMax(arr):

    maxNum = - sys.maxsize
    for elem in arr:
        if elem > maxNum:
            maxNum = elem

    return maxNum


def findBump(arr):

    for i in range(len(arr)-1, 0, -1):
        if arr[i] < arr[i-1]:
            return i
    


def findDip(arr):

    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return i


def findSubArrToMakeEntireArrSorted(arr):

    bump = findBump(arr)
    dip = findDip(arr)


    minNum = findMin(arr[dip: bump+1])
    maxNum = findMax(arr[dip: bump+1])
    
    
    end = -1
    for i in range(bump, len(arr)-1):
        if arr[i+1] > maxNum:
            end = i
            break
            

    for i in range(dip, -1, -1):
        if arr[i-1] < minNum:
            print(arr[i-1], minNum)
            start = i
            break

    print(arr[start: end+1])


findSubArrToMakeEntireArrSorted([1,2,4,5,3,7,5,6,8])