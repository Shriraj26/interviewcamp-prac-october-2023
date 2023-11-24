"""
TC - O(1), SC - O(1)
Given a 8 * 8 chess board, return the min number of moves to reach the destination.
if cannot reach, then return -1

--- This is intuitive, if u watch the chess board, bishop can move only in diagonnals, then
it would take him max 2 steps to reach the dest.
isWhite func tells is if bishop is at white cell or black cell
1. If souce is at white cell and destination at black cell or vice versa, there is no way to reach
    the dest, so return -1
2. If source == destination, 0 moves required
3. Check the diagonalls - if destination lies on its diagonal, then can reach in one move
4. Else return 2 as it would need 2 moves to reach the dest
"""

def canReachDest(arr, x1, y1, x2, y2):

    # White cells have this property and they lie on points where x%2 == y%2
    def isWhite(x, y):
        return x%2 == y%2

    
    if isWhite(x1, y1) != isWhite(x2, y2):
        return -1
    elif x1 == x2 and y1 == y2:
        return 0
    elif abs(x1 - x2) == abs(y1-y2):
        return 1
    else:
        return 2 

arr = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]
]

# souce on white, dest on black
print(canReachDest(arr, 0,0, 0,1))
# On diagonal
print(canReachDest(arr, 0,0, 7,7))
# Souce == dest
print(canReachDest(arr, 0,0, 0,0))
# 2 moves needed
print(canReachDest(arr, 0,0, 6,0))


