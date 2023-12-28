"""
Here, you will get a path till destination
and length of path as well...
"""

from queue import Queue

def shortestPathBFS(g, src, dest):

    visited = {}
    q = Queue()

    d = 0
    visited[src] = None
    q.put(src, d)

    while q.qsize():

        currNode, d = q.get()
        if currNode == dest:
            print('Here we can get the distance to reach here, as well as a dict that stores path')
            break

        # loop neigh
        for neigh in g[currNode]:
            if neigh not in visited:
                visited[neigh] = currNode
                q.put(neigh, d+1)

    path = []
    while dest:
        path.append(dest)
        dest = visited.get(dest)
    
    # Now for path - 
    print(path)
    # For the length of path till that-
    print(d)


