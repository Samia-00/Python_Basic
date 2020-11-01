class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singleNode:
    def __init__(self):
        self.head = None
        self.tail= None
    def insert(self,data):
        node=Node(data)

        if not self.head:
            self.head = node
        else:
            self.tail.next=node
        self.tail =node
def printing(head):
    while head:
        print(head.data)
        head=head.next
if __name__ == '__main__':
    x=int(input())
    y=singleNode()

    for _ in range(x):
        item=int(input())
        y.insert(item)
    printing(y.head)

        
