"""

dfs func:

    mark node as visiting
    loop neighbor
        if neighbor unvisited,
            if dfs neighbor returns false, return False
        else:
            if neighbor visiting, return True
    
    mark node as visited
    return False as no cycle found

"""

visited = [0 for i in range(n)]
def dfsCycle(node):

    # mark node as visiting
    visited[node] = 1

    for neigh in g[node]:
        if visited[neigh] == 0:
            return dfsCycle(neigh)
        else:
            if visited[neigh] == 1:
                return False
    
    visited[node] = 2
    return False
    