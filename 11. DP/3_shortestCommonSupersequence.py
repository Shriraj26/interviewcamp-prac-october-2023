'''
SCS = m + n - LCS
Ex - geek, eke
Ans - geeke
'''
class Solution:
    def longestCommonSubsequence(self, X: str, Y: str) -> int:
        
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

        return m + n - t[m][n]





