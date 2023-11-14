def inOrder(root):
    stk = []
    arr = []

    node = root

    if node is None:
        return []

    while node or len(stk) > 0:
        if node is not None:
            stk.append(node)
            node = node.left
        else:
            node = stk.pop()
            arr.append(node)
            node = node.right

    return arr
