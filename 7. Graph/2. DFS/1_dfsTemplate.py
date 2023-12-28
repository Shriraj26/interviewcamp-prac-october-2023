""" 
TC - O(V + E)
SC - O (V) -- for visited set/dict

Mark Visiting  ------ 1
Process Node
Loop Neighbors that are not visiting or visited
Mark Visited   ------ 2

Unvisited  ------ 0
"""
vertices = [i for i in range(10)]
visit = {}
# add all the vertices in visit dict as unvisited
for v in range(vertices):
    visit[v] = 0

def dfs(g, src):
    visit[src] = 1
    print(src)
    for neigh in g[src]:
        if visit[neigh] != 1 and visit[v] != 2:
            dfs(neigh)
    
    visit[src] = 2


