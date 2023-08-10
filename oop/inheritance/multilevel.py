class A:
    def printA(self):
        print("inside A class")
class B(A):
    def printB(self):
        print("inside B class")
class C(B):
    def printC(self):
        print("inside C class")
objc=C()
objc.printC()
objc.printA()
objc.printB()
