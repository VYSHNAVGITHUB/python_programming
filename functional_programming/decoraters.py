def changevalue(func):
    def wrapper(a,b):
        if a<b:
            a,b=b,a
            return func(a,b)
        else:
            return func(a,b)
    return wrapper
@changevalue
def substract(n1,n2):
    print(n1-n2)
substract(5,2)
substract(2,5)

@changevalue
def div(num1,num2):
    print(num1/num2)
div(6,2)
div(2,6)