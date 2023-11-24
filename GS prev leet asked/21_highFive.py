"""
Here we are using sorted Contaiers that is like TreeMap in Java, this will sort the keys in
our dictionary!
TC - O(n * logn * logk) as -   
    n to traverse all the marks of students, 
    log(n) to insert marks in sorted Dict
    log(k) to insert marks in the heap of size k, here k is 5 
    Final TC - O(nlogn)
SC - O(unique ids of students), For heap we need size k but heap will only
    be created of size 5 this its constant.
"""

import heapq
from sortedcontainers import SortedDict

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        myDict = SortedDict()
        for iD, marks in items:
            if iD not in myDict:
                minHeap = []
                heapq.heappush(minHeap, marks)
                myDict[iD] = minHeap
            else:
                currHeap = myDict[iD]
                heapq.heappush(currHeap, marks)
                if len(currHeap) > 5:
                    heapq.heappop(currHeap)
        
        result = []
        for key, val in myDict.items():
            score = 0
            currHeap = myDict[key]
            while len(currHeap) > 0:
                score += heapq.heappop(currHeap)
            result.append([key, score//5])
        
        return result