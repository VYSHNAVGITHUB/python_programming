class Person:
    def __init__(self,name,age,place):
        self.name1=name
        self.age=age
        self.location = place
    def printdata(self):
        print(self.name1)
        print(self.age)
        print(self.location)
f=open("data.txt","r")
l=[]
for i in f:
    data=i.rstrip("\n").split(",")
    name=data[0]
    age=data[1]
    loc=data[2]
    pe=Person(name,age,loc)
    l.append(pe.name1)
    pe.printdata()
print(l)
