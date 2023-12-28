'''
This is just like min path sum - https://leetcode.com/problems/minimum-path-sum/

In this ques we start from bottom left and go to top right and get the max gold
'''
def maxPathGold(arr):

    m = len(arr)
    n = len(arr[0])

    for i in range(m-1, -1, -1):
        for j in range(n):
            if i == m-1 and j == 0:
                continue
            elif i == m-1:
                arr[i][j] = arr[i][j] + arr[i][j-1]
            elif j == 0:
                arr[i][j] = arr[i][j] + arr[i+1][j]
            else:
                arr[i][j] = arr[i][j] + max(arr[i][j-1], arr[i+1][j])

    print(arr[0][n-1])


arr = [[0,0,0,0,5],
        [0,1,1,1,0],
        [2,0,0,0,0]
]

maxPathGold(arr)