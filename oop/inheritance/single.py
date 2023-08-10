class A:
    def printa(self,num):
        self.num=num
        print("inside A class")
class B(A):
    def printb(self):
        print("inside B class",self.num)

objb=B()
objb.printa(5)
objb.printb()
