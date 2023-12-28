# Out of bounds function
def oob(i, j, m, n):
    if i < 0 or j < 0 or i >= m or j >= n:
        return True
    return False

arr = [
    [0,0,0,1,1],
    [1,1,0,1,1],
    [0,0,0,0,0],
    [1,1,1,1,0]
]
m = len(arr) # Rows
n = len(arr[0]) # Columns

def pathInAMaze(i, j):

    # Base cases 1. Out of bounds and 2. Wall
    if oob(i, j,m,n) or arr[i][j] == 1 or arr[i][j] == -1:
        return False
    
    # Success!
    if i == m-1 and j == n-1:
        return True
    
    # Mark visiting
    arr[i][j] = -1

    # Recurse all 4 directions
    paths = [(i+1,j), (i-1,j), (i, j+1), (i,j-1)]

    for path in paths:
        if pathInAMaze(path[0], path[1]):
            return True
        
    # Path not found till here
    arr[i][j] = 0

    # Return False
    return False

print(pathInAMaze(0, 0))


