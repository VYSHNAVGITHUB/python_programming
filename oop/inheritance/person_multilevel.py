class Person:
    def setvalue(self,name,place):
        self.name1=name
        self.location=place
    def printdata(self):
        print(self.name1)
        print(self.location)
class Child(Person):
    def setchild(self,addrs,age):
        self.addrs=addrs
        self.age=age
class Student(Child):
    def setstd(self,rollno,dep):
        self.rollno=rollno
        self.dep=dep
    def printstd(self):
        print(self.name1,self.rollno,self.age,self.dep,self.addrs,self.location)
st1=Student()
st1.setvalue("amal","kochi")
st1.setchild("abc",956465224)
st1.setstd(3,"ece")
st1.printstd()