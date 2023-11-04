"""
Here we print the permutations of the array...
We need another array to keep track that we have added that number or not

"""

arr = [1,2,3]
buff = [0,0]

isInBuff = [False for i in range(len(arr))]

def permutations(buffIndex):

    if buffIndex == len(buff):
        print(buff)
        return
    
    for i in range(len(arr)):

        if isInBuff[i] == False:
            buff[buffIndex] = arr[i]
            isInBuff[i] = True
            permutations(buffIndex + 1)
            isInBuff[i] = False

permutations(0)

