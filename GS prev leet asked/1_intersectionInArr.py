arr1 = [1,1,2,2,2]
arr2 = [1,1,2,2]

def findIntersection(arr1, arr2):

    myDict = {}
    for elem in nums1:
        if elem in myDict:
            myDict[elem]+= 1
        else:
            myDict[elem] = 0
    result = []
    for elem in nums2:
        if elem in myDict:
            if myDict[elem] > 0:
                myDict[elem] -= 1
                result.append(elem)
            elif myDict[elem] == 0:
                del myDict[elem]
                result.append(elem)

    return result


def intersectionIfBothArraysSorted(arr1, arr2):

