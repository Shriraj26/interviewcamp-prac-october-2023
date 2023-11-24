# Tc - O(n * k) where k is k itself
# Sc - O(O(n)) if k == n
from queue import Queue
def winnerOfCircularGame(n, k):


    q = Queue()
    for i in range(1,n+1):
        q.put(i)

    while q.qsize() > 1:
        for i in range(k-1):
            q.put(q.get())
        q.get()

    return q.get()

print(winnerOfCircularGame(5, 2))

print(winnerOfCircularGame(6, 5))
