"""
TC - 
Constructor - O(n)
Union and FInd - O(α(n)) where α(n) is inverse ackerman function.. Avg - O(1)
SC - O(n) for both rank and root array

We can do 3 things here - 
1. Get the number of connected components, provinces etc.
2. Check if graph is valid tree, if u try to connect 2 nodes that have same root, there forms a 
    cycle, thus return False in union function, else True
3. 
"""

class UnionFind:

    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
        self.count = size

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
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
        
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def getCount(self):
        return self.count
    


uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true
