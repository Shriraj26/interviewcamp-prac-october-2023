"""
Given an array, give me length of min subarray whose sum is greater than or equal to target
This can be done using sliding window
"""

def minSubArray(arr, target):

    start = 0
    end = 0
    currSum = arr[start]
    result = float('inf')

    while start < len(arr):

        # If start goes ahead of end
        if end < start:
            end = start
            currSum = arr[start]

        if currSum < target:
            if end == len(arr):
                break
            end += 1
            currSum += arr[end]
        else:
            result = min(result, end - start + 1)
            currSum -= arr[start]
            start += 1
    
    return result if result != float('inf') else 0
