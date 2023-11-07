'''
1. A Doubly list Node Class
2. A LRU Cache class that has head, tail, hashmap and its capacity
3. Functions that will go in LRU Class but directly not given in the question
    1. AddNode - Add the node to the linkedList
    2. RemoveNode - remove the node from the linkedList
    3. add - add the key value pair to hashmap and call addNode
    4. remove - remove key value pair from hashmap and call removeNode
4. LRU Functions - 
    1. Put - If current len exceeds, remove head, then add node
    2. Get - retrieve the Cache value and set it to most recent

'''

class ListNode:

    def __init__(self, key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.tail = None

class LRU:

    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.head = None
        self.tail = None

    def get(self, key):
        # If the key is not in map or head is none, return
        if key not in self.map or self.head is None:
            return -1

        # Remove the cache from LRU
        node = self.map[key]
        self.remove(key)

        # Add the cache again to LRU so that it is now most recent
        self.add(key, node.val)
        return node.val

    def put(self, key, value):
        # Check if key is not in map
        if key not in self.map:
            # If capacity full, delete the head node
            if len(self.map.keys()) == self.capacity:
                self.remove(self.head.key)
        # Call add function to add the cache
        self.add(key, value)

    def add(self, key, value):
        # Remove the old node if its key in the map
        if key in self.map:
            self.removeNode(self.map[key])
        
        # Create a new node
        newNode = ListNode(key, value)
        # Put in Map
        self.map[key] = newNode
        # Call addNode
        self.addNode(newNode)

    def remove(self, key):
        # Get the node to delete from map
        node = self.map[key]
        if node is None:
            return
        # Call the removeNode
        self.removeNode(node)
        # remove from Map
        del self.map[key]
        

    def addNode(self, node):
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node

    def removeNode(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        if node == self.head:
            self.head = node.next

        if node == self.tail:
            self.tail = node.prev
        

