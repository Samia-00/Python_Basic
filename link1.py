class linkedlist:
    def __init__ (self):
        self.head=Node
    def __repr__(self):
        nodes =[]
        current_node=self.head.next
        while current_node:
            nodes.append(repr(current_node))
            current_node=current_node.next
        return ",".join(nodes)
    def append(self,data):
        pass
    def prepend(self,data):
        pass
    def insert(self,data,new_data):
        pass
    def search(self,item):
        pass
    def remove(self,item):
        pass
            
