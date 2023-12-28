"""
https://leetcode.com/discuss/interview-question/2191439/Google-or-Phone-or-Check-if-path-exists
Given a 2d array where 1 represent a stone and 0 represent water. 
Return true if you can reach to the last row from the first row else false. 
You can travel in all directions (top, bottom, left, right) by one position.
Follow up - 
1. Return the indexes of given path
2. Return how many path exist in the matrix. --- doubt as it should be shortest
"""

def oob(i, j, m, n):
        if i < 0 or j < 0 or i >= m or j >= n:
            return True
        
def ifPathExists(g, dest, m, n):
    
    def dfs(i, j, visited):
        if (i,j) == (m-1, n-1):
            return True
        
        visited.add((i,j))
        paths = [[i+1,j], [i-1,j], [i,j+1], [i,j-1]]
        for path in paths:
            if not oob(path[0],path[1], m, n) and (path[0], path[1]) not in visited and g[path[0]][path[1]] != 0:
                if dfs(path[0], path[1], visited):
                    return True
        return False
    
    # loop only first row - 
    for j in range(n):
        if g[0][j] != 0:
            visited = set()
            if dfs(0,j, visited):
                return True

# Keep on adding all the elements in the path array and pop it too...
# refer unique Paths question...
    

