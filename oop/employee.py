class Employee:
    def setemployee(self,name,id,desig,salary):
        self.name=name
        self.id=id
        self.desig=desig
        self.salary=salary

    def printempl(self):
        print(self.name,self.id,self.desig,self.salary)
emp1=Employee()
emp1.setemployee("vyshnav",1,"devoloper",25000)
emp1.printempl()