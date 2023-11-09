class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        g = {}
        for edge in edges:
            if edge[0] not in g:
                g[edge[0]] = [edge[1]]
            else:
                g[edge[0]].append(edge[1])
            

        visited = [0 for i in range(n)]

        # 0 is not visited, we dont need that much
        # 1 is visiting
        # 2 Path found
        def dfs(node):
            
            # If Path found
            if visited[node] == 2:
                return True

            # if no edge, check if its destination
            if node not in g:
                return node == destination

            # Mark as visiting
            visited[node] = 1

            for neigh in g[node]:

                # If cycle or dfs gives false, return False
                if visited[neigh] == 1 or dfs(neigh) == False:
                    return False
            
            visited[node] = 2
            return True

        return dfs(source)

