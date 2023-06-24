#CREATING NODE-DECLARATION & DEFINITION

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head #temp=first node
            while temp:
                print(temp.data,"->",end=" ")#temp. data means first node data
                temp=temp.next
obj=SLL()
#node creation initialising
n=Node(10)#so n.data in node class will be 10
obj.head=n
n1=Node(20)
obj.head.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
n5=Node(60)
n4.next=n5
obj.display()

    
