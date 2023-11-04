# Sorted Array find 2 numbers that sum to the target

def twoSum(arr, target):

    start = 0
    end = len(arr) - 1

    while start <= end:

        currSum = arr[start] + arr[end]

        if currSum == target:
            return [arr[start], arr[end]]
        
        elif currSum < target:
            start += 1

        else:
            end -= 1

    return [-1, -1]

arr = [1,2,3,4,5]
target = 9

print(twoSum(arr, target))

