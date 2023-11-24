def firstNonRepeatChar(s):

    myDict = {}
    for c in s:
        if c in myDict:
            myDict[c] += 1
        else:
            myDict[c] = 1
    
    for c in s:
        if myDict[c] == 1:
            return c

    return ''


print(firstNonRepeatChar('aabbcc'))
print(firstNonRepeatChar('asubsebusapd'))


