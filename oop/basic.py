# class creation
class Person:
    def read(self):   #method 1
        print("person is reading")
    def walk(self):   #method 2
        print("person is walking")
# reference=object_creation
obj=Person()
# call methods
obj.read()
obj.walk()

obj1=Person()
obj1.read()