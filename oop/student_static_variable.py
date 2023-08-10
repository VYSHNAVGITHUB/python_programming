class Student:
    college="GPTC Muttom"
    def setstudent(self,name,rollno,department):
        self.name=name
        self.num=rollno
        self.dep=department

    def printstdnt(self):
        print(self.name)
        print(self.num)
        print(self.dep)
        print(Student.college)
std1=Student()
std1.setstudent("vyshnav",57,"EEE")
std1.printstdnt()

std2=Student()
std2.setstudent("arun",25,"ECE")
std2.printstdnt()