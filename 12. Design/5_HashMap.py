'''
Neetcode soln - https://www.youtube.com/watch?v=cNWsgbKwwoU
'''
class ListNode:
    def __init__(self, key=-1, val=-1, next = None):
        self.next = next
        self.key = key
        self.val = val

class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for i in range(1000)]
    
    def hash(self, key):
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        currNode = self.map[index]
        while currNode.next:
            if currNode.next.key == key:
                currNode.next.val = value
                return
            currNode = currNode.next
        currNode.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = self.hash(key)
        currNode = self.map[index]
        currNode = currNode.next # we dont want to start from dummy node
        while currNode:
            if currNode.key == key:
                return currNode.val
            currNode = currNode.next
        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        currNode = self.map[index] # We will start from dummy node as we want to delete current node's next, it will be wasy
        while currNode and currNode.next:
            if currNode.next.key == key:
                currNode.next = currNode.next.next
                return
            currNode = currNode.next
    
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)