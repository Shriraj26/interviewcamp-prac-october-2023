'''
TC - O(m * n) as we visit all the cells in the grid
SC - O(m * n) as all the cells can be rotten initially so all the space will be filled with that in
    visited

'''
from queue import Queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])
        visited = set()
        q = Queue()

        # visit all rotten oranges and add them in queue
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.put((i, j, 0))
                    visited.add((i,j))
        
        # Process the queue and visit fresh oranges to mark them rotten
        d = 0
        while q.qsize():
            currI, currJ, d = q.get()
            paths = [(currI + 1, currJ), (currI-1, currJ), (currI, currJ-1), (currI, currJ + 1)]

            for i, j in paths:
                if i >= 0 and i < m and j >= 0 and j < n:
                    if grid[i][j] == 1 and (i,j) not in visited:
                        q.put((i, j, d+1))
                        visited.add((i,j))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    return -1

        return d