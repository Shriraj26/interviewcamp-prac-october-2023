"""
Input - 1 2 3 4 5 6 7, and buffer - 3
Output - 1 2 3, 1 2 4, .... 4 5 6, 4 6 7, 5 6 7
"""

buff = [0,0,0]
arr = [1,2,3,4,5,6,7,8]

def combinations(bufferIndex, startIndex):

    # Case where bufferindex is out of bounds
    if bufferIndex == len(buff):
        print(buff)
        return
    
    # if array index is OOB
    if startIndex == len(arr):
        return
    
    for i in range(startIndex, len(arr)):

        # Fill the buffer
        buff[bufferIndex] = arr[i]

        # Recursive call
        combinations(bufferIndex + 1, i + 1)

combinations(0, 0)