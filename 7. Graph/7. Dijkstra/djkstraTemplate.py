"""
Declare a distance array that will store dist of all the vertices from src, deckare
all verices with infinity, only src with 0
Put src and its dist in min heap
keep popping minHeap
Update the dist of its neighbors if this condition holds -
    if dist[neigh] > dist[src] + destWeight (destWeight you will get it from graph)
In the end, dist array will have all the distances from src to dest

Refer to network delay time for details - https://leetcode.com/problems/network-delay-time/description/
"""
import heapq
def networkDelayTime(self, times: List[List[int]], n: int, src: int) -> int:
        if src is None :
            return None

        g = {i+1 : [] for i in range(n)}
        for source, dest, weight in times:
            g[source].append([dest, weight])
        
        minHeap = []
        visited = set()
        dist = [float('inf') for i in range(n+1)]
        dist[src] = 0
        heapq.heappush(minHeap, (0, src))
        while minHeap:
            _, currNode  = heapq.heappop(minHeap)
            visited.add(currNode)
            for neigh, neighEdgeWeight in g[currNode]:
                if neigh not in visited:
                    if dist[neigh] > dist[currNode] + neighEdgeWeight:
                        dist[neigh] = dist[currNode] + neighEdgeWeight
                        heapq.heappush(minHeap, (dist[neigh], neigh))
        
        res = max(dist[1:])
        return res if res != float('inf') else -1
