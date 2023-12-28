"""
Refer leetcode for question --- https://leetcode.com/problems/word-search/submissions/
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def oob(i, j, index):
            return i < 0 or j < 0 or i >= m or j >=n or index >= len(word)

        def backtrack(row, col, index):
            # Failure cases
            
            if oob(row, col, index) or board[row][col] != word[index]:
                return False
            
            # Success case
            if index == len(word)-1:
                return True
            # mark something 
            temp = board[row][col]
            board[row][col] = '#'
            
            # loop paths, branches
            paths = [[row + 1, col], [row, col+1], [row-1, col], [row, col-1]]
            for nrow, ncol in paths:
                if backtrack(nrow, ncol, index+1):
                    return True
            board[row][col] = temp
            return False
        
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False


