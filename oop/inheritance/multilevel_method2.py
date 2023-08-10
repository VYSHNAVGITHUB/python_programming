class Person:
    def __init__(self,name,place):
        self.name1=name
        self.location=place
    def printdata(self):
        print(self.name1)
        print(self.location)
class Child(Person):
    def __init__(self,addrs,age,name,place):
        super().__init__(name,place)
        self.addrs=addrs
        self.age=age
class Student(Child):
    def __init__(self,rollno,dep,addrs,age,name,place):
        super().__init__(addrs,age,name,place)
        self.rollno=rollno
        self.dep=dep
    def printstd(self):
        print(self.name1,self.rollno,self.age,self.dep,self.addrs,self.location)
st1=Student(1,"cse","abc",21,"anu",'kochi')
st1.printstd()