'''
a min heap will mantain the end meet times, the meeting will only end
or get popped from the heap if there is a start time greater than or 
equal top of the heap. 
'''
class Solution:
    def minMeetingRooms(self, arr: List[List[int]]) -> int:
        arr.sort()
        minHeap = []
        for i in range(len(arr)):
            meetStart = arr[i][0]
            meetEnd = arr[i][1]
            if minHeap and meetStart >= minHeap[0]:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, meetEnd)
        return len(minHeap)
                