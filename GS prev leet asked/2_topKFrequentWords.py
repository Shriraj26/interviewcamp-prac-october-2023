'''
TC - O(Nlogk)
SC - O(k) for heap - heap size can be atmost k elements,
     O(n) for the dictionary

In lt, we have self.word > other.word, the thing to note here is that, this is reversed.
Suppose we have 2 words with same freq, the: 3 and is : 3,
In the result we sort the heap with reverse = True, this will mean that higher priority elems
will come first
Therefore, in minHeap, we have to store the elem in reverse order of lexicography.
THus if we store the and then is in heap ... the -> is
When we sort it in reverse, we get correct order- ... is -> the
'''

import heapq
class Pair:

    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    # Doubt here
    def __lt__(self, other):
        return self.word > other.word if self.freq == other.freq else self.freq < other.freq
    
    # def __gt__(self, other):
    #     return self.word > other.word if self.freq == other.freq else self.freq > other.freq

    # def __eq__(self, other):
    #     return self.word == other.word if self.freq == other.freq else self.freq == other.freq

    # def __str__(self) :
    #     return self.word + " " + self.freq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        frequencyCount = collections.defaultdict(int)

        for word in words :
            frequencyCount[word] += 1

        for key in frequencyCount :
            heapq.heappush(heap, Pair(key,frequencyCount[key]))
       
            if len(heap) > k :
                heapq.heappop(heap)

        return [elem.word for elem in sorted(heap, reverse = True)]