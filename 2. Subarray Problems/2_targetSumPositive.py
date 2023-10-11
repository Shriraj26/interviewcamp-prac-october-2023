'''
Record sum when the numbers are only positive and they sum up to target
Sliding window

'''

def slidingWindow(arr, target):

    start = 0
    end = 1
    currSum = arr[0]

    while start <= end and end < len(arr):

        if currSum == target:
            return [start, end-1]

        elif currSum < target:
            end += 1
            currSum += arr[end]

        else:
            currSum -= arr[start]
            start += 1
            

    return [-1, -1]


print(slidingWindow([1,2,3,5,2], 8))






