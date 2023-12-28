"""

"""
W = 50
wt = [10, 20, 30]
val = [60, 100, 120]
n = len(wt)

dp = [[-1 for i in range(W+1)] for j in range(n+1)]

# init dp
for i in range(n+1):
    for j in range(W+1):
        if i == 0 or j == 0:
            dp[i][j] = 0

def knapsackRecursive(n, W):

    if dp[n][W] != -1:
        return dp[n][W]

    if wt[n-1] <= W:
        dp[n][W] = max(val[n-1] + knapsackRecursive(n-1, W-wt[n-1]), knapsackRecursive(n-1, W))
    else:
        dp[n][W] = knapsackRecursive(n-1, W)
    return dp[n][W]

print(knapsackRecursive(n, W))
    
    
    

