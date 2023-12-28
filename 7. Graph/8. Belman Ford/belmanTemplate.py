"""
I used the Neetcode's code for this bellman ford - 
"""
class Solution:
    
    def findCheapestPrice(self, n: int, flights: List[List[int]], source: int, dst: int, k: int) -> int:
        dist = [float('inf') for i in range(n)]
        dist[source] = 0

        for i in range(k+1):
            tempDist = dist.copy()
            for src, dest, srcToDestDist in flights:
                if dist[src] != float('inf') and tempDist[dest] > dist[src] + srcToDestDist:
                    tempDist[dest] = dist[src] + srcToDestDist
            dist = tempDist
        return dist[dst] if dist[dst] != float('inf') else -1
    
