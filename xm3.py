class Stack:
    def __init__(self):
        self._theItems = list()
    def isEmpty(self):
        return len(self) == 0
    def __len__ (self):
        return len(self._theItems)
    def peek(self):
        assert not self.isEmpty(),'cannot peek at an empty stack'
        return self._theItems[-1]
    def pop(self):
        assert not self.isEmpty(),'cannot pop from any empty stack'
        return self._theItems.pop()
    def push(self,item):
        self._theItems.append(item)

s=Stack()
print(s.push(7))
print(s.push(6))
print(s.push(3))
print(s.push(6))
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
