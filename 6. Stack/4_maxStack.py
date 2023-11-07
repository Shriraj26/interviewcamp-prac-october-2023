'''
Refer to this solution - https://www.geeksforgeeks.org/find-maximum-in-a-stack-in-o1-time-and-o1-extra-space/
1. Push - if elem to insert greater than maxElem -
                We insert 2 * x - maxElem 
            else onsert elem normally
2. Pop -  if x > maxElem, that is top of stack is greater than maxElem 
            we update the maxElem to 2 * maxElem - x, and return return (currElem + self.maxElem) // 2
          else return currElem...


'''
class MaxStack:

    def __init__(self):
        self.arr = []
        self.maxElem = None 

    def push(self, x: int) -> None:
        if len(self.arr) == 0:
            self.arr.append(x)
            self.maxElem = x
        else:
            if x > self.maxElem:
                self.arr.append(2 * x - self.maxElem)
                self.maxElem = x
            else:
                self.arr.append(x)
        print(self.arr)

    def pop(self) -> int:
        if len(self.arr) == 0:
            return -1
        
        currElem = self.arr.pop()
        if currElem > self.maxElem:
            self.maxElem = 2 * self.maxElem - currElem
            return (currElem + self.maxElem) // 2
        else:
            return currElem

    def top(self) -> int:
        if len(self.arr) == 0:
            return -1
        return self.arr[-1]

    def peekMax(self) -> int:
        return self.maxElem
        

maxStack = MaxStack()
maxStack.push(10)
maxStack.push(2)
maxStack.push(3)
maxStack.push(40)
maxStack.push(499)
# print(maxStack.peekMax())

print('pop ',maxStack.pop(), ' maxELem ', maxStack.peekMax())
print('pop ',maxStack.pop(), ' maxELem ', maxStack.peekMax())
print('pop ',maxStack.pop(), ' maxELem ', maxStack.peekMax())
print('pop ',maxStack.pop(), ' maxELem ', maxStack.peekMax())
# print(maxStack.peekMax())
# maxStack.push(20)
# print(maxStack.peekMax())
# maxStack.pop()
# print(maxStack.peekMax())
