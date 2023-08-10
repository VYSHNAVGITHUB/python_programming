class Person:
    def __init__(self,name,place,age):
        self.name1=name
        self.location=place
        self.age=age
    def printdata(self):
        print(self.name1)
        print(self.age)
        print(self.location)
pe1=Person('anu',"kochi",25)
pe1.printdata()