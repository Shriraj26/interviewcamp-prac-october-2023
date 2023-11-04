"""
Here we use a data structure to store the previously calculated result.
"""

def fiboMemo(n, myDict):

    # Base case -
    if n == 1 or n == 2:
        return 1
    
    if myDict.get(n):
        return myDict[n]
    
    result = fiboMemo(n-1, myDict) + fiboMemo(n-2, myDict)
    myDict[n] = result

    return result

print(fiboMemo(90, {}))
