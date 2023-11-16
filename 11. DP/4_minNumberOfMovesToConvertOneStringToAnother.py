'''
min Moves = m + n - 2*LCS
where m = length of string X
n = length of string Y
Ex - think of heap and pea
heap -> pea ... 
1. First we need to delete chars from 'heap', these chars are not the LCS that we want- 
    Therefore deletions = len(X) - LCS ==> m - LCS
    m - LCS ... heap -> remove h and p ... O/P -> ea
2. Now, We need to insert the chars to 'ea' to make it 'pea'. Notice, we need to add only one 
    char that is 'p', and this char is len(Y) - LCS !!
    There fore n - LCS ... pea - ea --> p... 

Therefore finally we have 
deletions = m - LCS
insertions = n - LCS
Total = m + n - 2 * LCS

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

        return m + n - 2 * t[m][n]





