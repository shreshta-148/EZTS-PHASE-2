class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class DLL:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("doubly link list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end="")
                temp=temp.next
    def insert_begining(self,data):
        new_node=Node(data)
        temp=self.head
        temp.previous=new_node
        new_node.next=temp
        self.head=new_node
    def insert_end(self,data):
        new_node=Node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp
    def insert_pos(self,pos,data):
        new_node=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        new_node.previous=temp
        new_node.next=temp.next
        temp.next.prev=new_node
        temp.next=new_node
    def delete_begining(self):
        temp=self.head
        self.head=temp.next
        temp.next.previous=None
        temp.next=None
    def delete_end(self):
        prev=self.head
        temp=self.head.next
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
        temp.prev=None
    def delete_pos(self,pos):
        prev=self.head
        temp=self.head.next
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.prev=prev
       # temp.next=temp.prev
       
    
        
node_1=Node("shreshta")
dl=DLL()
dl.head=node_1
print(node_1)#address of node1
print(node_1.data)
print(node_1.next)
print(node_1.prev)
print("\n")
node_2=Node("Akshay")
node_3=Node("sadhvi")
node_4=Node("akshaya")
node_5=Node("varshith")
node_1.next=node_2
node_2.prev=node_1
print(node_2)#address of node2
print(node_2.data)
print(node_1.next)
print(node_2.prev)
print("\n")
node_2.next=node_3
node_3.prev=node_2
print(node_3)#address of node3
print(node_3.data)
print(node_2.next)
print(node_3.prev)
print("\n")
node_3.next=node_4
node_4.prev=node_3
print(node_4)#address of node4
print(node_4.data)
print(node_3.next)
print(node_4.prev)
print("\n")
node_4.next=node_5
node_5.prev=node_4
print(node_5)#address of node5
print(node_5.data)
print(node_4.next)
print(node_5.prev)
dl.display()
print("\n")
dl.insert_begining("annarapu")
dl.display()
print("\n")
dl.insert_end("anjani")
dl.display()
print("\n")
dl.insert_pos(3,"Thatikonda")
dl.display()
print("\n")
dl.delete_begining()
dl.display()
print("\n")
dl.delete_end()
dl.display()
()
print("\n")
dl.delete_pos(2)
dl.display()
