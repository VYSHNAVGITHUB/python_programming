class Employee:
    def __init__(self,name,salary,post):
        self.name=name
        self.salary=salary
        self.post=post
    def displayemp(self):
        print('Name:',self.name,"Salary:",self.salary)
    def desig(self):
        print(self.name,"is working as a",self.post)
emp=Employee('anu',12000,"abc")
emp.displayemp()
emp.desig()

