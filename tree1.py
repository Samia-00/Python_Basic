class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
a=Tree('A')
Head=a
b=Tree('B')
c=Tree('C')
d=Tree('D')
e=Tree('E')
f=Tree('F')
g=Tree('G')
h=Tree('H')

a.left=b
b.left=d
b.right=e
d.left=h
a.right=c
c.left=f
c.right=g

def preorderTrav(subtree):
    if subtree is not None:
        print(subtree.data)
        preorderTrav(subtree.left)
        preorderTrav(subtree.right)
preorderTrav(a)


def preorderTrav(subtree):
    if subtree is not None:
        #print(subtree.data)
        preorderTrav(subtree.left)
        preorderTrav(subtree.right)
        print(subtree.data)
preorderTrav(a)

def preorderTrav(subtree):
    if subtree is not None:
        #print(subtree.data)
        preorderTrav(subtree.left)
        print(subtree.data)
        preorderTrav(subtree.right)
        #print(subtree.data)
preorderTrav(a)
