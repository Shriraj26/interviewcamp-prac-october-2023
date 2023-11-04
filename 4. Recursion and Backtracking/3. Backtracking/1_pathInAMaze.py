"""
This is a classic backtracking problem, in we this, we determine if there is any path towards end or not.
There are steps involved but I would like to order them like this - 
1. Base case
2. Core Idea
3. Split, Steps recursive call
4. Collect result
5. Memoization
"""

# Out of bounds function
def oob(i, j, m, n):
    if i < 0 or j < 0 or i >= m or j >= n:
        return True
    
    return False

arr = [
    [0,0,0,1,1],
    [0,1,0,0,0],
    [0,0,1,1,0],
    [0,0,0,1,0]
]
m = len(arr) # Rows
n = len(arr[0]) # Columns

memo = [[None for j in range(n)] for i in range(m)]

def pathInAMaze(i, j):

    # Base cases 1. Out of bounds and 2. Wall
    if oob(i, j,m,n) or arr[i][j] == 1:
        return False
    
    # Success!
    if i == m-1 and j == n-1:
        return True
    

    # Check memo for current point, if path not found or cycle
    if memo[i][j] == 'PATH_NOT_FOUND' or memo[i][j] == 'VISITING':
        return False

    # Mark visiting
    memo[i][j] = 'VISITING'

    # Recurse all 4 directions
    paths = [(i+1,j), (i-1,j), (i, j+1), (i,j-1)]

    for path in paths:
        if pathInAMaze(path[0], path[1]):
            return True
        
    # Path not found till here
    memo[i][j] = 'PATH_NOT_FOUND'

    # Return False
    return False


print(pathInAMaze(0, 0))


