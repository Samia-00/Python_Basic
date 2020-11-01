class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=Node(10)
Head=a
b=Node(11)
c=Node(17)
d=Node(19)
e=Node(21)
f=Node(23)

a.next=f
b.next=e
e.next=d
d.next=c
f.next=b

def traverse(head):
    current=head
    while current is not None:
        print(current.data)
        current=current.next
traverse(Head)
