def checkIfNumExistsInStack(arr, target):

    tempStack = []

    while len(arr) > 0:
        currNum = arr.pop()
        if currNum == target:
            print(tempStack)
            print(arr)
            return True
        tempStack.append(currNum)
    
    while len(tempStack):
        arr.append(tempStack.pop())
    
    print(tempStack)
    print(arr)
    return False


arr =[1,2,3,4,5]

print(checkIfNumExistsInStack(arr, 2))