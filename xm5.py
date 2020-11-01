class Queue:
    def __init__(self):
        self._qlist=list()
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self._qlist)
    def enqueue(self,item):
        self._qlist.append(item)
    def dequeue(self):
        assert not self.isEmpty(),'cannot dequeue from an empty queue'
        return self._qlist.pop(0)

q=Queue()
print(q.enqueue(3))
print(q.enqueue(4))
print(q.enqueue(6))
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
