def add(n1,n2):
    print(n1+n2)
def sub(n1,n2):
    print(n1-n2)
def mul(n1,n2):
    print(n1*n2)
def div(n1,n2):
    print(n1/n2)
while True:
    option=int(input("select an operation\n1.add\n2.sub\n3.mul\n4.div\n5.stop"))

    if option==5:
        break
    elif option>0 and option<5:
        n1=int(input("enter num1"))
        n2=int(input("enter num2"))

        if option==1:
            add(n1,n2)
        elif option==2:
            sub(n1,n2)
        elif option==3:
            mul(n1,n2)
        else:
            div(n1,n2)
    else:
        print("invalid option")

