class stack:
    def __init__(self):
        self.stack=list()
    def push(self,data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        return False
    def pop(self):
        if len(self.stack)<=0:
            return('stack empty')
        return self.stack.pop()
    def size(self):
        return len(self.stack)
s=stack()
print(s.push(5))
print(s.push(7))
print(s.push(9))
print(s.push(11))
print(s.push(6))
print(s.push(5))

print(s.size())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.size())
