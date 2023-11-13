"""
Here we check that - `
1. If node x's root == node y's root, then there is a cycle, return False, after entire union, return True
2. If node x's root == node y's root -> Here we used to increment rank of rootX, but here we return simply.
3. If count of connected component is greater than 1, then its not a tree.

"""


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)

        for u, v in edges:
            if uf.union(u, v) is False:
                return False

        print(uf.count)

        return uf.count == 1


class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        self.count = n

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

            self.count -= 1
        else:
            return False

        return True

    def find(self, x):
        if x == self.root[x]:
            return x

        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)
