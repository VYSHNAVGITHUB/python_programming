stack=[]
size=int(input("enter size"))
top=0
def push():
    global top
    if top>=size:
        print("stack is full")
    else:
        e=int(input("enter element"))
        stack.append(e)
        print(stack)
        top+=1
def pop():
    global top
    if top==0:
        print("stack is empty")
    else:
        stack.pop()
        print(stack)
        top-=1
while True:
    option=int(input("enter operation\n1.push\n2.pop"))
    if option==1:
        push()
    elif option==2:
        pop()
    else:
         print("invalid option")