from queue import Queue
import collections
prerequisites = [['user', 'admin'], ['Root', 'root'], ['home2', 'user'], ['home1', 'user'], ['home3', 'home1'], ['home3', 'Root']]
def topSortTry():
    
    numCourses = 7
    inDegree = {}
    q = Queue()
    g = {}
    topSortArr = []
    myDict = {}

    # Construct a graph and calculate indegrees
    for dest, src in prerequisites:
        if src not in g:
            g[src] = [dest]
        else:
            g[src].append(dest)
        if inDegree.get(src) == None:
            inDegree[src] = 0
        inDegree[dest] = inDegree.get(dest, 0) + 1
    print(inDegree)
    
    # Put all the indegrees in queue that have indegree zero
    for key, val in inDegree.items():
        if val == 0:
            q.put(key)
    
    # loop queue
    while q.qsize():
        currNode = q.get()
        topSortArr.append(currNode)
        if currNode in g:
            for neigh in g[currNode]:
                inDegree[neigh] -= 1
                if inDegree[neigh] == 0:
                    q.put(neigh)
                    
    
    # print(topSortArr)
    # return at last
    return topSortArr if len(topSortArr) == numCourses else []

print(topSortTry())