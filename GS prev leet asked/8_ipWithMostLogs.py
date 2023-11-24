def mostLogsIP(s):
    tempArr = []
    for c in s:
        tempArr.append(c.split('-')[0].rstrip())

    myDict = {}
    maxVal = 0
    for elem in tempArr:
        if elem in myDict:
            myDict[elem] += 1
        else:
            myDict[elem] = 1
        maxVal = max(maxVal, myDict[elem])
    result = []
    for key, val in myDict.items():
        if val == maxVal:
            result.append(key)

    return sorted(result)




s = "10.0.0.1 - log entry 1 11", "10.0.0.1 - log entry 2 213", "10.0.0.2 - log entry 1 11", "10.0.0.2 - log entry 2 213"
print(mostLogsIP(s))
