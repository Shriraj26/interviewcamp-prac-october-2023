"""
Bipartite -> Think of BFS, ques asked in undirected
same colored nodes not on same level
No odd cycle
node's level != neighbor's level, then you have answer
visited will store the level for each node, from that you can check
in queue, you will put node along with its level...
"""

from queue import Queue


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = {}
        q = Queue()

        def bfsHelper(root):
            visited[root] = 0
            q.put((root, 0))

            while q.qsize() > 0:
                currNode, currLevel = q.get()

                # loop neighbors
                for neigh in graph[currNode]:
                    if neigh not in visited:
                        q.put((neigh, currLevel + 1))
                        visited[neigh] = currLevel + 1
                    elif visited[neigh] == currLevel:
                        return False

            return True

        # Loop all the nodes of graph
        for i in range(len(graph)):
            if i not in visited:
                if bfsHelper(i) == False:
                    return False

        return True
