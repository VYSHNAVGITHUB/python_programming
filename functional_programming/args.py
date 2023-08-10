def printn(*args):
    return args                 #1
print(printn(7,2,5,8,10))


def add(*args):
    sum=0
    for i in args:              #2   add infinit nums
        sum+=i
    return sum
print(add(2,5,6,8,1))



