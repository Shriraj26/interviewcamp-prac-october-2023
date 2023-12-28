"""
Construct a graph and while doing that, record indegrees of each vertex
Put all the vertices that have zero indegree in a Queue
Loop Queue till its length is not zero
    pop node from queue
    Add it to topsort array
    decrement indegree of all the child nodes of this vertex
    if there is any child with indegree zero, add it to queue
Return topsort array if its length == num vertices else return 0
Also -- you can check in indegree array if any vertex has indegree > 0 then also
there is a cycle!

Refer to this question - https://leetcode.com/problems/course-schedule-ii/submissions/
"""

from queue import Queue
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        inDegree = {i : 0 for i in range(numCourses)}
        q = Queue()
        g = {}
        topSortArr = []

        # Construct a graph and calculate indegrees
        for dest, src in prerequisites:
            if src not in g:
                g[src] = [dest]
            else:
                g[src].append(dest)
            inDegree[dest] += 1
        
        
        # Put all the indegrees in queue that have indegree zero
        for key, val in inDegree.items():
            if val == 0:
                q.put(key)
        
        # loop queue
        while q.qsize():
            currNode = q.get()
            topSortArr.append(currNode)
            if currNode in g:
                for neigh in g[currNode]:
                    inDegree[neigh] -= 1
                    if inDegree[neigh] == 0:
                        q.put(neigh)
        
        # return at last
        return topSortArr if len(topSortArr) == numCourses else []

