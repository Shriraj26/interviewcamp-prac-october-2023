"""
Here for union - 
Connect the components based on there ranks
For find -
Use recursion to compress the path, at atmost it will run O(alpha * log (n)) times as log n is height of tree
"""


class UnionFind:
    def __init__(self, size):
        self.size = size
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

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

    def connected(self, x, y):
        return self.find(x) == self.find(y)


uf = UnionFind(10)

uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.root)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
