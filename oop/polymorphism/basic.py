# 1.overloading
# class A:
#     def printa(self):
#         print("inside A class")
# class B(A):
#     def printa(self,num):
#         self.num=num
#         print("inside B class")
# objb=B()
# objb.printa()
# objb.printa(5)

# 2.overriding
class Parent:
    def buyphone(self):
        print("buy nokia")
class Child(Parent):
    def buyphone(self):
        print("buy i-phone")
objc=Child()
objc.buyphone()