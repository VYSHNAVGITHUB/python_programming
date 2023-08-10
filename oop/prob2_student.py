class Student:
    def __init__(self,rollno,name,dep):
        self.num=rollno
        self.name=name
        self.dep=dep
    def printstd(self):
        print(self.rollno)
        print(self.name)
        print(self.dep)
f=open('student.txt','r')
l=[]
for i in f:
    data=i.rstrip("\n").split(',')
    rollno=data[0]
    name=data[1]
    dep=data[2]
    st=Student(rollno,name,dep)
    l.append(st.name)
    st=printstd()
print(l)

