"""
Print Letter combinations of a phone number - 
2 1 3 --> AD, AE, AF, BD, ...... CE, CF
"""

# Initialize a dictionary A to Z
myDict = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}

letters = '213'
newStr = ''
for s in letters:
    if s == '0' or s == '1':
        continue
    newStr += s

buff = ['' for i in range(len(newStr))]


def phoneCombo(startIndex, buffIndex, buff):

    # Base Case - 
    if buffIndex == len(buff):
        print(''.join(buff))
        return
    if startIndex == len(newStr):
        return
    
    for i in range(startIndex, len(newStr)):
        for char in myDict[newStr[i]]:
            buff[buffIndex] = char
            phoneCombo(i + 1, buffIndex + 1, buff)


phoneCombo(0, 0, buff)
