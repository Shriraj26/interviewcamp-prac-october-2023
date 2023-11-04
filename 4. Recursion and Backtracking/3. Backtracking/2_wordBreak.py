"""
    1. Check if you can form a valid string from 0 to i
    2. Add that to result
    3. Recurse from i+1 to end and if valid string can be formed too,
        If yes, return true
        If no, remove the string 0 to i from result that should be the last added string
        and mark the memo[i+1] as false
"""

s = 'catsandog'
myDict = ("cats","dog","sand","and","cat")
result = []

memo = [None for i in range(len(s))]
def wordBreak(startIndex):

    # base case if you reached end of the array
    if startIndex == len(s):
        return True
    
    # memo condition
    if memo[startIndex] == 'False':
        return False
    
    for i in range(startIndex, len(s)):

        if s[startIndex: i+1] in myDict:
            
            # Add to result this string
            result.append(s[startIndex: i+1])

            # Check if recursive s from i+1 gives true
            if wordBreak(i+1):
                return True
            else:
                result.pop()
                memo[i+1] = False

    return False


print(wordBreak(0))
print(result)
