
def longestCommonSubsequence(X: str, Y: str) -> int:
    
    m = len(X)
    n = len(Y)
    
    t = [[-1 for i in range(n+1)] for j in range(m+1)]

    # initialize dp table
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                t[i][j] = 0

    # choice diagram converted to for loops
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])

    return t[m][n]


def recursiveDP(text1, text2):
    dp = [[None for i in range(len(text2)+1)] for i in range(len(text1)+1)]
    
    for i in range(len(text1)+1):
        for j in range(len(text2) + 1):
            if i ==0 or j == 0:
                dp[i][j] = 0
    
    def lcs(m, n):

        if dp[m][n]:
            return dp[m][n]

        if text1[m-1] == text2[n-1]:
            if dp[m-1][n-1] is not None:
                dp[m][n] = 1 + dp[m-1][n-1]
            else:
                dp[m-1][n-1] = lcs(m-1, n-1)
                dp[m][n] = 1 + dp[m-1][n-1]
        else:
            if dp[m][n-1] is not None and dp[m-1][n] is not None:
                dp[m][n] = max(dp[m][n-1], dp[m-1][n])
            else:
                dp[m][n-1] = lcs(m, n-1)
                dp[m-1][n] = lcs(m-1, n)
                dp[m][n] = max(dp[m][n-1], dp[m-1][n])

        return dp[m][n]
    
    return lcs(len(text1), len(text2))

print(recursiveDP('AEGHIOPUC','EHOPC'))