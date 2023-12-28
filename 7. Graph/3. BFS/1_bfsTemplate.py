"""
Add src to Queue, 
mark it visiting
Loop queue
    pop from queue current, 
    process current
    loop neighbors of current
        if neigh not visited
            add neigh to q
            mark it visiting
        mark current as visited
"""
from queue import Queue
def bfs(src, g, visited):
    q = Queue()
    q.put(src)
    visited[src] = 1 # visiting
    while q.qsize():
        current = q.pop()
        for neigh in g[current]:
            if visited[neigh] != 1 and visited[neigh] != 2:
                q.put(neigh)
                visited[neigh] = 1 # visiting
        visited[current] = 2 # visited

