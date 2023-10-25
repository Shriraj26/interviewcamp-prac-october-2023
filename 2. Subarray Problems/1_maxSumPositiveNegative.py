'''
Record maximum sum with positive and negative numbers
Kadane's Algo has 2 things - 
1. Record MaxSum ending at index i
2. Record the maximumest sum in whole array by help of point 1

'''

def maxSumPositiveNegative(arr):

    maxSumAtIndex = arr[0]
    maxSumEver = arr[0]

    for i in range(1, len(arr)):

        maxSumAtIndex = max(maxSumAtIndex + arr[i], arr[i])
        maxSumEver = max(maxSumEver, maxSumAtIndex)
    
    return maxSumEver

print(maxSumPositiveNegative([-2, -3, 4, -1, -2, 1, 5, -1]))
