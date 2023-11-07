"""
    DFS works very easy!
    - Mark visited/ visiting
    - Process the current node
    - Visit its neighbors
    - Mark visited if marked visiting earlier

    To make this work on the entire graph - 
        - FOr loop mark all the nodes unvisited
        = For loop in graph, 
            if unvitsited node, 
                dfs visit that node
"""

visited = set()
g = {}

def dfs(node):

    visited.add(node)

    for neighbor in g[node]:

        if neighbor not in visited:
            dfs(neighbor)

    

