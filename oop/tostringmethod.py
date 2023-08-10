class Person:
    def __init__(self,name,place,age):
        self.name1=name
        self.location=place
        self.age=age
    def printdata(self):
        print(self.name1)
        print(self.age)
        print(self.location)
    def __str__(self):
        return self.name1+str(self.age)
pe1=Person("anu","kochi",21)
pe1.printdata()
print(pe1)
print(pe1.name1)
print(pe1.age)