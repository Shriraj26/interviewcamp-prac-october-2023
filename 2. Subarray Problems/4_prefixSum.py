# Find the subarray that sums to k... positive and negative numbers


def prefixSum(arr, k):

    myDict = {}
    currSum = 0

    for i in range(len(arr)):

        currSum += arr[i]

        if currSum == k:
            return arr[:i+1]
        
        if myDict.get(currSum - k) is not None:

            return arr[myDict.get(currSum - k) + 1: i+1]
        
    return [-1, -1]

    
print(prefixSum([1,2,3], 3))