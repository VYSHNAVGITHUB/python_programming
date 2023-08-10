# l=[1,4,7,8,9,3,2]
# square=[]
# for i in l:
#     square.append(i**2)
# print(square)

l=[1,4,7,8,9,3,2]
square=[i**2 for i in l]
even=[i for i in l if i%2==0]
print(square)
print(even)