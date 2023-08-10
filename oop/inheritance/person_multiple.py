class Person:
    def setvalue(self,name,place,age):
        self.name1=name
        self.location=place
        self.age=age
    def printdata(self):
        print(self.name1)
        print(self.age)
        print(self.location)
class Parent:
    def setparent(self,addrs,phn):
        self.addrs=addrs
        self.phn=phn
class Employee(Person,Parent):
    def setemp(self,desig,salary):
        self.desig=desig
        self.salary=salary
    def printemp(self):
        print(self.name1,self.desig,self.age,self.salary,self.location)