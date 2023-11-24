# TC - O(m * n) where m is length of all the words in the dict and n is length of substring
def longest(s, arr):

    maxStrLen = 0
    for elem in arr:
        if s in arr:
            maxStrLen = max( maxStrLen, len(elem))

    return maxStrLen

arr = ["CODGE", "ODG", "LODGES", "SODG", "dodge", "mODJ", "LODGESSSS"]
s = "ODG"

print(longest(s, arr))
