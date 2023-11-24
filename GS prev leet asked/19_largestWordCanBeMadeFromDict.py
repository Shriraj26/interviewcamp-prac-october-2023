"""
Given a dictionary of the words(strings) which contains different words & you are given an input string e.g. “abd”. You need to find the largest word available in the supplied dictionary which can be made using the letters of input string. The returned word can contain only the same no of occurrences of the letters as given in the input string i.e. if a letter is given once then in the output it should be existed only once. Examples:
Question link - https://leetcode.com/discuss/interview-question/760987/Hard-Problem-%3A-was-asked-in-Goldman-Sachs-
TC - O(N * k) where k = 26 as 26 letter alphabets
SC - O(k) where k is 26
"""

def largestWord(myDict, s):

    def canWordBeMade(word, charArr):
        for w in word:
            if charArr[ord(w) - ord('a')] <= 0:
                return False
            charArr[ord(w) - ord('a')] -= 1    
        
        return True

    # Create a 26 length array that stores occurences
    charArr = [0] * 26
    for c in s:
        charArr[ord(c) - ord('a')] += 1
    
    resLen = -float('inf')
    resultWord = ''
    for word in myDict:
        temp = charArr.copy()

        if canWordBeMade(word, temp):
            if len(word) > resLen:
                resLen = len(word)
                resultWord = word

    return resultWord

myDict = ["to", "banana", "toes", "dogs", "ababcd", "elephant"]

print(largestWord(myDict, "ogtdes"))



        
                
