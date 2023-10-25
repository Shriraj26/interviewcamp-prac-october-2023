# Find the subarray that sums to k... positive and negative numbers


def prefixSum(arr, k):

    currSum = arr[0]
    myDict = {0: arr[0]}

    for i in range(1, len(arr)):

        if currSum == k:
            return arr[0:i]
        
        if  myDict.get(currSum - k) is not None:
            return arr[myDict.get(currSum - k) + 1: i ]
        
        currSum += arr[i]
        myDict[currSum] = i

    
print(prefixSum([2,4,-2,1,-3,5,-3], 5))