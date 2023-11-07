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

    def __init__(self):
        self.head = None
        self.tail = None

    def appendNode(self, node):

        if self.head is None:
            self.head = node
            
        else:
            self.tail.next = node
        
        self.tail.setNext(node)

    def sortO12(self, node):

        # Create diff ll for zero, one and 2
        zeroLL = LinkedList()
        oneLL = LinkedList()
        twoLL = LinkedList()

        while node:
            if node.data == 0:
                zeroLL.appendNode(node)
            elif node.data == 1:
                oneLL.appendNode(node)
            else:
                twoLL.appendNode(node)

            node = node.next

        # Remove the trailing next pointers to the formed LLS
        if zeroLL.next:
            zeroLL.next = None
        if oneLL.next:
            oneLL.next = None
        if twoLL.next:
            twoLL.next = None

        # Append the LLS
        result = LinkedList()
        result.appendLinkedList(zeroLL, result)
        result.appendLinkedList(oneLL, result)
        result.appendLinkedList(twoLL, result)

        # Finally return the sorted LL
        return result


    def appendLinkedList(toAppend, original):

        # if toAppend is none or toappend's head is None, return
        if toAppend is None or toAppend.head is None:
            return
        
        original.appendNode(toAppend)
        original.tail = toAppend.tail