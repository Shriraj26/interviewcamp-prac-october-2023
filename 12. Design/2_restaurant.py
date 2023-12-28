from sortedcontainers import SortedSet
from collections import OrderedDict

class AvailableTables:

    def __init__(self, numTables):
        self.sortedSet = SortedSet([i+1 for i in range(numTables)])
        self.customerMap = {}

    def getClosestAvailableTable(self, partysize):
        if partysize in self.sortedSet:
            return partysize
        
        
        print('I got this partysize ', partysize)
        print('set now ', self.sortedSet)
        index = self.sortedSet.bisect_right(partysize)
        if 0 > index > len(self.sortedSet):
            return self.sortedSet[index]
        return -1

    def acquireTable(self, partysize, customerName):
        self.sortedSet.remove(partysize)
        self.customerMap[partysize] = customerName
    
    def releaseTable(self, partysize):
        self.sortedSet.add(partysize)
        del self.customerMap[partysize]

class CustomerQueue:
    def __init__(self):
        self.orderMap = OrderedDict()

    def put(self, key, val):
        self.orderMap[key] = val
    
    def remove(self, key):
        if key not in self.orderMap:
            return -1
        self.orderMap.pop(key)
    


class Restaurant:

    def __init__(self, numTables):
        self.numTables = numTables
        self.customerQueue = CustomerQueue()
        self.availableTables = AvailableTables(numTables)

    def putToWaitlist(self, partysize, customerName):
        self.customerQueue.put(partysize, customerName)
        

    def serveCustomer(self):
        for partysize, customerName in self.customerQueue.orderMap.items():
            closestTable = self.availableTables.getClosestAvailableTable(partysize)
            print('closestTable ', closestTable, ' party ', partysize)
            if closestTable >= partysize:
                self.availableTables.acquireTable(closestTable, customerName)
                self.customerQueue.remove(partysize)
            else:
                pass
            
        
    

r = Restaurant(5)
r.putToWaitlist(2, 'A')
r.putToWaitlist(3, 'B')
r.putToWaitlist(4, 'C')
r.putToWaitlist(5, 'D')
r.putToWaitlist(5, 'E')
r.serveCustomer()


