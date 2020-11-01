class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

A=Tree('a')
head=A
B=Tree('b')
C=Tree('c')
D=Tree('d')
E=Tree('e')
F=Tree('f')
G=Tree('g')
H=Tree('h')
I=Tree('i')
J=Tree('j')

A.left=B
A.right=C
B.left=D
B.right=E
C.left=F
C.right=G
G.left=I
G.right=J

def preorderTrav(subtree):
    if subtree is not None:
        print(subtree.data)
        preorderTrav(subtree.left)
        preorderTrav(subtree.right)
preorderTrav(head)
