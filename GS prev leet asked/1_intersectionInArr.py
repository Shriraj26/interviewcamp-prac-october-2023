arr1 = [1,1,2,3]
arr2 = [1,1,2,2,3]

def findIntersection(nums1, nums2):

    myDict = {}
    for elem in nums1:
        if elem in myDict:
            myDict[elem]+= 1
        else:
            myDict[elem] = 1
    result = []
    for elem in nums2:
        if elem in myDict:
            if myDict[elem] >= 1:
                myDict[elem] -= 1
                result.append(elem)
                if myDict[elem] == 0:
                    del myDict[elem]
                
                
    return result


print(findIntersection(arr1, arr2))

