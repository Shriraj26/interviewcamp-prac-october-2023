def firstOccurInDupes(root, target):
    node = root

    while node:
        if node.val < target:
            node = node.left
        elif node.val > target:
            node = node.right
        else:
            return node

    return None
