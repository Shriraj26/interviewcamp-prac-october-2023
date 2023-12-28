"""
This is a complete BST class to construct a BST from array,
add a node,
delete a node
"""
from queue import Queue
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None
        self.capacity = 0

    def size(self):
        return self.capacity
    
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if root.val > val:
            return searchBST(root.left)
        elif root.val < val:
            return searchBST(root.right)
        else:
            return root

    def successor(self, root):
        curr = root.right
        while curr.left:
            curr = curr.left
        return curr.val

    def predeccessor(self, root):
        curr = root.left
        while curr.right:
            curr = curr.right
        return curr.val

    def addNode(self, key):
        self.root = self.addNodeHelper(self.root, key)

    def addNodeHelper(self, root, key):
        if not root:
            return TreeNode(key)
        if root.val > key:
            root.left = self.addNodeHelper(root.left, key)
        elif root.val < key:
            root.right = self.addNodeHelper(root.right, key)
        return root

    def deleteNode(self, key):
        self.root = self.deleteNodeHelper(self.root, key)

    def deleteNodeHelper(self, root, key) -> TreeNode:
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNodeHelper(root.left, key)
        elif root.val < key:
            root.right = self.deleteNodeHelper(root.right, key)
        else:

            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                root.val = self.successor(root)
                root.right = self.deleteNodeHelper(root.right, root.val)
        return root

    def oob(self,index):
        return index < 0 or index >= self.capacity

    def buildBST(self, arr):
        self.capacity = len(arr)
        self.root = self.buildBSTHelper(arr, 0, self.size() - 1)

    def buildBSTHelper(self, arr, start, end):
        if start > end or self.oob(start) or self.oob(end):
            return None
        mid = start + (end - start) // 2
        root = TreeNode(arr[mid])
        root.right = self.buildBSTHelper(arr, mid+1, end)
        root.left = self.buildBSTHelper(arr, start, mid-1)
        return root
    
    def traverseBST(self, root):
        if not root:
            return []
        q = Queue()
        q.put(root)
        level = 0
        result = []
        while q.qsize():
            result.append([])
            counter = q.qsize()
            while counter:
                curr = q.get()
                result[level].append(curr.val)
                if curr.left:
                    q.put(curr.left)
                if curr.right:
                    q.put(curr.right)
                counter -= 1
            level += 1
        return result


bst = BST()
bst.buildBST([1,2,3,3.5, 4,5,6])
print(bst.traverseBST(bst.root))
