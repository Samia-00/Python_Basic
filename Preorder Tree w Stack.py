class Stack :
#Creates an empty stack.
     def __init__( self ):
          self._theItems = list()

#Returns True if the stack is empty or False otherwise.
     def isEmpty( self ):
          return len( self ) == 0

#Returns the number of items in the stack.
     def __len__ ( self ):
          return len( self._theItems )

#Returns the top item on the stack without removing it.
     def peek( self ):
          assert not self.isEmpty(), "Cannot peek at an empty stack"
          return self._theItems[-1]

#Removes and returns the top item on the stack.
     def pop( self ):
          assert not self.isEmpty(), "Cannot pop from an empty stack"
          return self._theItems.pop()

#Push an item onto the top of the stack.
     def push( self, item ):
          self._theItems.append( item )

class Tree:
     def __init__(self,data):
          self.data=data
          self.left=None
          self.right=None
x=Tree('A')
head=x
y=Tree('B')
z=Tree('C')
p=Tree('D')
q=Tree('E')
w=Tree('F')
r=Tree('G')
h=Tree('H')

x.left=y
x.right=z
y.left=p
y.right=q
z.left=w
z.right=r
p.left = h


k=Stack()


root=x
k.push(x)


while not k.isEmpty():

     while root !=None:
          print(root.data)
          if root.right!=None:
               k.push(root.right)
          root=root.left
     root=k.pop()
              


c
"""'''''
s=Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())

'''"""
