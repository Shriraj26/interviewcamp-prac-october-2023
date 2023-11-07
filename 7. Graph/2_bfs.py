"""
    1. mark node visited
    2. add to queue
    3. loop q till it is not empty
    4.      remove current node, 
            loop neighbors
                if neighbors not visited
                    mark neighbors visited
                    add to queue

"""


import queue 
visited = set()
g = {}


def bfs2(g, node):

    q = queue.Queue()
    visited = set()

    visited.add(node)
    q.put(node)
    while q.qsize():

        curr = q.get()
        print(curr)

        for neighbor in g[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.put(neighbor)

bfs2(g, 1)
    
