"""
Deep explore from one node, count + 1 when finished exploring
We did this by both dfs and bfs
"""
from queue import Queue


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = {i: [] for i in range(n)}
        visited = set()
        # Create a graph g
        for v1, v2 in edges:
            g[v1].append(v2)
            g[v2].append(v1)

        def dfsHelper(root):
            visited.add(root)

            # explore neigh
            for neigh in g[root]:
                # if not visited, dfs
                if neigh not in visited:
                    dfsHelper(neigh)

        def bfsHelper(root):
            q = Queue()
            q.put(root)
            visited.add(root)

            while q.qsize():
                currNode = q.get()

                # loop neigh
                for neigh in g[currNode]:
                    if neigh not in visited:
                        q.put(neigh)
                        visited.add(neigh)

        count = 0
        for i in range(n):
            if i not in visited:
                dfsHelper(i)
                count += 1

        return count
