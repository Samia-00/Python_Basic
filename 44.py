class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.neighbour=None

A=Node('a')
head=A
B=Node('b')
C=Node('c')
D=Node('d')
E=Node('e')

A.next=B
B.next=C
C.next=D
D.next=E



class Edge:
    def __init__(self,node):
        self.node=node
        self.nextEdge=None

x=Edge(B)
y=Edge(C)
z=Edge(D)


x.nextEdge=y
y.nextEdge=z


A.neighbour=x

current=A.neighbour
while current!=None:
    print(current.node.data)
    current=current.nextEdge

















