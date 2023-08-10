queue=[]
size=int(input("enter size"))
top=0
def enqueue():
    global top
    if top>=size:
        print("queue is full")
    else:
        e=int(input("enter element"))
        queue.append(e)
        print(queue)
        top+=1
def dequeue():
    global top
    if top==0:
        print("queue is empty")
    else:
        queue.remove(queue[0])
        print(queue)
        top-=1
while True:
    option=int(input("enter operation\n1.enqueue\n2.dequeue"))
    if option==1:
        enqueue()
    elif option==2:
        dequeue()
    else:
        print("invalid option")