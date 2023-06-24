queue=[]
def enqueue():
    if len(queue)==n:
        print("queue is full")
    else:
        element=input("enter element for queue:")
        queue.append(element)
        print(queue)
def dequeue():
        if not queue:
            print("queue is empty")
        else:
            e=queue.pop(0)
            print(queue)
n=int(input("enter the size of queue:"))
while True:
    print("select the operation 1.push 2.pop 3.quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        break
    else:
        print("enter correct operation:")