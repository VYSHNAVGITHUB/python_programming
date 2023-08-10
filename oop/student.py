class Student:
    def setstudent(self,name,rollno,department,college):
        self.name=name
        self.num=rollno
        self.dep=department
        self.college=college
    def printstdnt(self):
        print(self.name)
        print(self.num)
        print(self.dep)
        print(self.college)
std1=Student()
std1.setstudent("vyshnav",57,"EEE","GPTC Mutttom")
std1.printstdnt()