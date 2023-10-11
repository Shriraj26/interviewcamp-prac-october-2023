# Sorted Array find 2 numbers that sum to the target

def twoSum(arr, target):

    start = 0
    end = len(arr) - 1

    while start <= end:

        currentSum = arr[start] + arr[end]

        # base case if start and end match to the target, return that index
        if currentSum == target:
            return [start, end]

        elif currentSum < target:
            start += 1

        elif currentSum > target:
            end -= 1

    return [-1, -1]

arr = [1,3,6,19,22]
target = 0

print(twoSum(arr, target))





