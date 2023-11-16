
'''
This is the jabardast problem
1. If node has right subtree, the successor will be left most node of its right subtree - 
    Ex -      2
           1     3
              2.5       -- Successor of 2 is 2.5
2. If node does not have right subtree, successor will be its parent's successor on right
    ex -      4
           2     5
        1    3          --- Successor of 3 is 4 which is its parent's successor on right, this will be done
                            by record and move on

'''

def firstSuccessorBST(root, targetNode):
    result = None
    if targetNode.right:
        node = targetNode.right
        while node:
            result = node
            node = node.left
        return result
    
    else:
        node = root
        while node:
            if node.val < targetNode.val:
                node = node.right
            elif node.val > targetNode.val:
                result = node.val
                node = node.left
            else:
                break
        return result
    

