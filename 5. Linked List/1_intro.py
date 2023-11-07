class Node:

    def __init__(self, data):
        self.next = None
        self.data = data

    def getNext(self):
        return self.next
    
    def setNext(self, node):
        self.next = node
    
    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data


class LinkedList:

    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def getHead(self):
        return self.head
    
    def getTail(self):
        return self.tail
    
    def setHead(self, head):
        self.head = head

    def setTail(self, tail):
        self.tail = tail

    def getNthNode(self, n):

        currNode = self.head
        for i in range(1,n+1):
            if currNode.next:
                currNode = currNode.next
            else:
                raise Exception('Next nodes are none')
                return None
        return currNode
    
    