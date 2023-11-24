from queue import Queue
def shortestPathBFS(g, src, dest):

    visited = set()
    visited2 = {}
    q = Queue()

    d = 0
    visited.add(src)
    visited2[src] = None
    q.put(src, d)

    while q.qsize():

        currNode, d = q.get()
        if currNode == dest:
            print('Here we can get the distance to reach here, as well as a dict that stores path')
            break

        # loop neigh
        for neigh in g[currNode]:
            if neigh not in visited:
                visited.add(neigh)
                visited2[neigh] = currNode
                q.put(neigh, d+1)

    path = []
    while dest:
        path.append(dest)
        dest = visited2.get(dest)
    print(path, d)


