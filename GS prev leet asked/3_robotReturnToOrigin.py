# Tc - O(n) SC - O(1)
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for m in moves:
            if m == 'U':
                x, y = x, y+1
            elif m == 'D':
                x, y = x, y-1
            elif m == 'L':
                x, y = x-1, y
            elif m == 'R':
                x, y = x+1, y
        return (x, y) ==(0, 0)