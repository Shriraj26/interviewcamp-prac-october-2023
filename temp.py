#abbbccda
import sys
def longestSubstr(s):

    if len(s) == 0:
        return [-1,0]
    start = 0
    end = 1
    resLen = 1
    resIndex = 0

    while end < len(s):

        if s[end] != s[end-1]:
            if resLen < end - start :
                resLen = end - start
                resIndex = start    
            
            start = end
        
        end += 1


    print(resIndex, resLen)
    
# longestSubstr('abbbccda')
# longestSubstr('10000111')
# longestSubstr('aabbbbbCdAA')



def tempFunc():

    s = "CODEGE"
    print("ODG" in s)


tempFunc()



