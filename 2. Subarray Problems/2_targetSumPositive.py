'''
Record sum when the numbers are only positive and they sum up to target
Sliding window

'''

def slidingWindow(arr, target):

    start = 0
    end = 0
    currSum = arr[0]

    while start <= end and end < len(arr):

        print(currSum)
        if currSum == target:
            print(currSum, target, start, end)
            return arr[start:end+1]
        
        elif currSum < target:
            if end < len(arr):
                end += 1
                currSum += arr[end]
            else:
                return [-1, -1]

        else:
            currSum -= arr[start]
            start += 1

    return [-1, -1]


print(slidingWindow([1,2,3,5,2], 8))






