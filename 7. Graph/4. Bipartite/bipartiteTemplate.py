"""
Node's level if equal to neighbors neighbor, then we have found an odd length cycle
Then return

prereq = here visited dict should have all the nodes initially as 0 for unvisited
"""

class Node:
    def __init__(self, val, state, level):
        self.val = val
        self.state = 0
        self.level = 0

from queue import Queue
def checkBipartite(g, src):
    
    
    
    
    
    
    
    
    q = Queue()
    d = 0
    q.put(src)
    visited[src] = 1

    while q.qsize():
        currNode = q.get()
        for neigh in g[currNode]:
            if visited[neigh] == 0:
                level[neigh] = level.get(currNode, 0) + 1
                visited[neigh] = 1
            else:
                if level.get(neigh, 0) == level.get(currNode, 0):
                    return False

