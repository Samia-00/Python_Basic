class Stack:
    def __init__(self):
        self.stack=list()
    def push(self,data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        return False
    def pop(self):
        if len(self.stack)<=0:
            return("stack empty")
        return self.stack.pop()
    def size(self):
        return len(self.stack)==0

class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
a=Tree('A')
head=a
b=Tree('B')
c=Tree('C')
d=Tree('D')
e=Tree('E')
f=Tree('F')
g=Tree('G')
h=Tree('H')

a.left=b
a.right=c
b.left=d
b.right=e
d.left=h
c.left=f
c.right=g

k=Stack()


root=a
k.push(a)


while not k.size():

     while root!=None:
          print(root.data)
          if root.right!=None:
               k.push(root.right)
          root=root.left
     root=k.pop()
               
