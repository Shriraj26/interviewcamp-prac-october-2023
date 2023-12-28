class Node:
    def __init__(self, key=-1, next=None):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.map = [Node() for _ in range(1000)]                

    def size(self):
        return len(self.map)

    def hash(self, key):
        return key % self.size()

    def add(self, key: int) -> None:
        index = self.hash(key)
        currNode = self.map[index]
        while currNode.next:
            if currNode.next.key == key:
                return
            currNode = currNode.next
        currNode.next = Node(key)

    def remove(self, key: int) -> None:
        index = self.hash(key)
        currNode = self.map[index]
        while currNode and currNode.next:
            if currNode.next.key == key:
                currNode.next = currNode.next.next
            currNode = currNode.next

    def contains(self, key: int) -> bool:
        index = self.hash(key)
        currNode = self.map[index]
        while currNode:
            if currNode.key == key:
                return True
            currNode = currNode.next
        return False
            


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)