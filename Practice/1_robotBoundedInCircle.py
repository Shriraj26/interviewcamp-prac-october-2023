'''
Have 2 things- 

1. Direction X and Direction Y
2. Position X and position Y

Intuition - 
1. If you do 'G', you are just moving ahead, just add the direction to current x and y
    x, y = x + dirX, y + dirY
2. If you are going left, the x and y direction will be swapped, but, 
    x will be -ve x as you go on left. Ex. if you are facing north ^ and 
    you want to go left, < 
    dirX = - dirY
    dirY = dirX
3. If you are going right, then x and y direction will be swapped, but
    Here y will be -ve y . Ex. if you are facing south and 
    you want to go right, then y will decrease right!
    dirX = dirY
    dirY = -dirX
4. Finally if you arrive at initial position, or your direction changed in a 
    single iteration, then you are bounded in the circle

'''

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        dirX, dirY = 0, 1

        for i in instructions:
            if i == 'G':
                x, y = x + dirX, y + dirY
            elif i == 'L':
                dirX, dirY = -dirY, dirX
            elif i == 'R':
                dirX, dirY = dirY, -dirX
            
        return (x, y) == (0, 0) or (dirX, dirY) != (0, 1)
    