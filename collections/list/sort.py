l=[6,4,8,9,2,3,4]
n=[]
while l:
    min=l[0]
    for i in l:
        if i<min:
            min=i
    n.append(min)
    l.remove(min)
print(n)
print(l)