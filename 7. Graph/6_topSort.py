def topSort():
    g = {i: [] for i in range(numCourses)}

    for v1, v2 in prerequisites:
        g[v2].append(v1)

    stack = []
    visited = [0 for i in range(numCourses)]

    def dfs(node):
        # mark visiting
        visited[node] = 1

        # loop neigh
        for neigh in g[node]:
            if visited[neigh] == 1:
                return False
            if visited[neigh] == 0:
                if dfs(neigh) is False:
                    return False

        visited[node] = 2
        stack.append(node)
        return True

    for node in g.keys():
        if visited[node] == 0:
            if not (dfs(node)):
                return []

    return stack[::-1]
