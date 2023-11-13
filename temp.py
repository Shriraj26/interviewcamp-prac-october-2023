class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        pass


class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        self.count = 0

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def find(self, x, y):
        if x == self.root[x]:
            return x

        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)
