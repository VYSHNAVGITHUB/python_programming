l=[1,5,8,6,12,52,54]
def square(n):
    return n**2
newl=list(map(square,l))      #normal method
print(newl)

newl1=list(map(lambda n:n**2,l))      # using lambda fn
print(newl1)
