import sys
def highestAvg(arr):

    myDict = {}

    for elem in arr:
        if elem[0] in myDict:
            myDict[elem[0]].append(int(elem[1]))
        else:
            myDict[elem[0]] = [int(elem[1])]

    maxAvg = -sys.maxsize
    for key, val in myDict.items():
        maxAvg = max(maxAvg, sum(val)// len(val))
    
    return maxAvg

    


arr = [["Bob","87"], ["Mike", "35"], ["Bob", "52"], ["Jason","35"], ["Mike", "55"], ["Jessica", "99"]]

print(highestAvg(arr))