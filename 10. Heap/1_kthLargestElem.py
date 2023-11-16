import heapq

def findKthLargest(nums, k) -> int:
    
    minHeap = []
    heapq.heapify(minHeap)
    
    for num in nums:
        if len(minHeap) < k:
            heapq.heappush(minHeap, num)
        else:
            if minHeap[0] < num:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, num)
        
        print(minHeap)
    return minHeap[0]


