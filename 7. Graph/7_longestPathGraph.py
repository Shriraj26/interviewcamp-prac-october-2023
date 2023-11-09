# ip - [["NYC","SFO"], ["SFO","LAX"],["LAX","SEA"],["PDX","SEA"]]

import sys


class Node:
    def __init__(self, val, dist):
        self.val = val
        self.dist = dist


ip = [["NYC", "SFO"], ["SFO", "LAX"], ["LAX", "SEA"], ["PDX", "SEA"]]


def topSort(ip):
    g = {}

    for v1, v2 in ip:
        n1 = Node(v1, 0)
        n2 = Node(v2, 0)
        if n1 not in g:
            g[n1] = [n2]
        else:
            g[n1].append(n2)
        if n2 not in g:
            g[n2] = []

    stack = []
    visited = {}

    def dfs(node):
        # mark visiting
        visited[node] = True

        # loop neigh
        for neigh in g[node]:
            if dfs(neigh) is False:
                return False

        stack.append(node)
        return True

    for node in g.keys():
        if visited.get(node) is not None and not (visited[node]):
            if not (dfs(node)):
                return []

    return stack[::-1]


g = {}

stack = topSort(ip)
print("asdasd stack", stack)

diameter = -sys.maxsize
# Child distance = max(child dist, parent dist + 1)
stack = stack[::-1]

for elem in stack:
    print("hehe ", elem.val, end=" ")

for current in stack:
    diameter = max(diameter, current.dist)

    for neigh in g[neigh]:
        if current.dist + 1 > neigh.dist:
            neigh.dist = current.dist + 1

print(diameter)
