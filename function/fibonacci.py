# n1=0
# n2=1
# for i in range(10):
#     print(n1)
#     nth=n1+n2
#     n1=n2
#     n2=nth

#with function
def fibonacci(terms):
    n1 = 0
    n2 = 1
    for i in range(10):
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
fibonacci(10)
