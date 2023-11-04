def longestSubWithUniqueChars(s):

    myDict = {}

    start = 0
    end = 1
    myDict[s[start]] = start
    maxStr = s[start]
    maxLen = 1

    print(s)
    while end < len(s):

        print(start, end, maxStr)
        if myDict.get(s[end]) is not None and start <= myDict.get(s[end]):
            start = myDict[s[end]] + 1
            
        myDict[s[end]] = end
        print(myDict)
        
        if end - start + 1 > maxLen:
            maxLen = end - start + 1
            maxStr = s[start: end + 1]

        end += 1

    print(maxStr, maxLen)






print(longestSubWithUniqueChars('abba'))