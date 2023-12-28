

def oob(i, j):
	return i < 0 or j < 0 or i >= m or j >= n

def isOnBorder(i, j):
    neighbors = [[i+1,j], [i-1,j], [i,j+1], [i,j-1]]
	# Check if its neighbor is out bf bounds then return True
    for nrow, ncol in neighbors:
        if oob(nrow, ncol) or grid[nrow][ncol] == 0:
            return True
    return False

def dfs(i, j, count):
    # Failure cases
    if oob(i, j) or grid[i][j] == 0 or (i,j) in visited:
        return
    
    visited.add((i, j))
    if isOnBorder(i, j):
        grid[i][j] = count
    
    neighbors = [[i+1,j], [i-1,j], [i,j+1], [i,j-1]]
    for nrow, ncol in neighbors:
        dfs(nrow, ncol, count)



			
grid = [[0, 0, 0, 0, 0, 0],
[0, 1, 1, 0, 1, 1],
[1, 1, 1, 1, 0, 1],
[0, 1, 1, 0, 1, 1],
[0, 0, 0, 0, 1, 0]]

m, n= len(grid), len(grid[0])

visited = set()
count = 2
for i in range(m):
	for j in range(n):
		if grid[i][j] == 1 and (i,j) not in visited:
			dfs(i, j, count)
			count += 1

# for i in range(m):
#     for j in range(n):
#         if grid[i][j] == 1 and (i,j) not in visited:
#               dfsCount(i, j)
#               count += 1

print('Count is ', count)
print(grid)
