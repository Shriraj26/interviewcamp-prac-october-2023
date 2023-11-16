def firstOccurInDupes(root, target):
    node = root
    result = None
    while node:
        if node.val < target:
            node = node.left
        elif node.val > target:
            node = node.right
        else:
            result = node
            node = node.left

    return result



