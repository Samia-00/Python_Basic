class stack:
    def __init__(self):
        self.queue=list()
    def enqueue(self,data):
        if data not in self.queue:
            self.queue.append(data)
            return True
        return False
    def dequeue(self):
        if len(self.queue)<=0:
            return('queue empty')
        return self.queue.pop(0)
    def size(self):
        return len(self.queue)
s=stack()
print(s.enqueue(5))
print(s.enqueue(7))
print(s.enqueue(9))


print(s.size())
print(s.dequeue())
print(s.dequeue())
print(s.dequeue())
