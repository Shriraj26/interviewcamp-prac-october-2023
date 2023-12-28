'''
Give me the min num of intervals to remove to make the intervals non overlapping
Compare prevEnd to the nextStart, if overlap, then count++, and prevEnd = min(prevEnd, nextEnd)
else prevEnd = nextEnd
'''
class Solution:
    def eraseOverlapIntervals(self, arr: List[List[int]]) -> int:
        arr.sort()
        result = 0
        prevStart, prevEnd = arr[0][0], arr[0][1]
        for nextStart, nextEnd in arr[1:]:
            if prevEnd > nextStart:
                result += 1
                prevEnd = min(prevEnd, nextEnd)
            else:
                prevEnd = nextEnd
        return result

            