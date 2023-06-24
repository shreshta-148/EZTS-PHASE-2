class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("empty list")
        else:
            temp=self.head
        while temp:
            print(temp.data,"->",end="")
            temp=temp.next
    def insert_begining(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def Insert_end(self,data):
        new_node=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        new_node.next=None
    def insert_position(self,pos,data):
        new_node=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node
    def delete_begining(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def delete_end(self):
        prev=self.head
        temp=self.head.next
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
    def delete_pos(self,pos):
        prev=self.head
        temp=self.head.next
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        
node_1=Node("shreshta")
SL=SLL()
SL.head=node_1
node_2=Node("akshay")
print(node_1.next)
node_1.next=node_2
print(node_1.next)
#SL.head=node_2
node_3=Node("akshaya")
node_4=Node("sadhvi")
node_2.next=node_3
print(node_2.next)
node_3.next=node_4
print(node_3.next)
SL.insert_begining("Anjani")
SL.display()
print("\n")
print(SL.head.data)
SL.Insert_end("varshith")
SL.display()
print("\n")
SL.insert_position(4,"sumanth")
SL.display()
print("\n")
SL.delete_begining()
SL.display()
print("\n")
SL.delete_end()
SL.display()
print("\n")
SL.delete_pos(2)
SL.display()