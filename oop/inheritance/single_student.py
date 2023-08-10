class Person:
    def setdata(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printdata(self):
        print(self.name)
        print(self.age)
        print(self.place)
class Student(Person):
    coll="mits"
    def setdetails(self,rollno,dep):
        self.roll=rollno
        self.dep=dep
    def printst(self):
        print(self.name,self.place,self.age,self.roll,self.dep,Student.coll)
st=Student()
st.setdetails(1,"cse")
st.setdata("anu","kochi",20)
st.printst()
