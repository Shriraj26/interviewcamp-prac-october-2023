'''
In prev question, you inremented result when there was overlap, and you you did 
prevEnd = min(prevEnd, nextEnd), You did this because you wanted to
'''

def eraseOverlapIntervals(arr) -> int:
    arr.sort()
    result = []
    prevStart, prevEnd = arr[0][0], arr[0][1]
    for nextStart, nextEnd in arr[1:]:
        if prevEnd >= nextStart:
            prevEnd = max(prevEnd, nextEnd)
        else:
            result.append([prevStart, prevEnd])
            prevEnd = nextEnd
            prevStart = nextStart
    
    result.append([prevStart, prevEnd])
    return result

eraseOverlapIntervals([[1,3],[2,6],[8,10],[15,18]])

eraseOverlapIntervals([[1,4],[4,5]])



            