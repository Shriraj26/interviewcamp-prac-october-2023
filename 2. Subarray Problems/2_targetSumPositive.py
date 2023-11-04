'''
Record sum when the numbers are only positive and they sum up to target
Sliding window!!
Here in loop do start < len array
'''

def slidingWindow(arr, target):

    start = 0
    end = 0
    currSum = arr[0]

    while start < len(arr):

        # Check if start goes ahead of end
        if start > end:
            end = start
            currSum = arr[start]

        if currSum == target:
            return arr[start: end+1]
        
        elif currSum < target:

            # Check if end is less than array length
            if end < len(arr) - 1:
                end += 1
                currSum += arr[end]
            else:
                return [-1, -1]
        else:

            # Increase the start
            currSum -= arr[start]
            start += 1

    return [-1, -1]

print(slidingWindow([1,28,3,5,2], 8))








'''
start = 0
    end = 0
    currSum = arr[0]

    while start < len(arr):

        if start > end:
            end = start
            currSum = arr[start]

    
        if currSum == target:
    
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

'''