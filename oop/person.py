class Person:
    def setvalue(self,name,place,age):
        self.name1=name
        self.location=place
        self.age=age
    def printdata(self):
        print(self.name1)
        print(self.age)
        print(self.location)
pe1=Person()
pe1.setvalue("vyshnav","kochi",23)
pe1.printdata()

pe2=Person()
pe2.setvalue("amal","kochi",24)
pe2.printdata()

