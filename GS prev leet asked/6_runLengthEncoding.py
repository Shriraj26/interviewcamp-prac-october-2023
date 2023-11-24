# SC - O(n), TC - O(n)
def stringConvert(s):
    if s == "":
        return ""
    stk = [[s[0], 1]]
    
    for i in range(1, len(s)):
        if stk[-1][0] == s[i]:
            stk[-1][1] += 1
        else:
            stk.append([s[i], 1])


    newStr = ""
    while stk:
        c, ctr = stk.pop()

        newStr+= str(ctr) + c
        
    return newStr[::-1]

# SC - O(1), TC - O(n)
def stringConvertNoStk(s):
    if s == "":
        return ""

    count = 1
    newStr = s[0]
    for i in range(1,len(s)):
        if s[i-1] == s[i]:
            count += 1
        else:
            newStr += str(count) + s[i]
            count = 1

    newStr += str(count)
    return newStr

print(stringConvertNoStk("aabbb"))
print(stringConvertNoStk(""))
print(stringConvertNoStk("bbaabaabbcccc"))
print(stringConvertNoStk("abcd"))
        

