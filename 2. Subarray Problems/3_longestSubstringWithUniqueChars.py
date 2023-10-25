def longestSubWithUniqueChars(s):

    myDict = {}

    start = 0
    end = 1
    myDict[s[start]] = start
    maxStr = s[start]
    maxLen = 1

    while end < len(s):

        if myDict.get(s[end]) is not None and start <= myDict[s[end]]:
            start = myDict[s[end]] + 1
            
        myDict[s[end]] = end
        
        if end - start + 1 > maxLen:
            maxLen = end - start + 1
            maxStr = s[start: end + 1]

        end += 1

    print(maxStr, maxLen)

    



print(longestSubWithUniqueChars('whatwhywhere'))