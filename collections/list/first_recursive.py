l=[1,3,5,6,7,8,2,3,1,2,3]
print(len(l))
l1=[]
rep=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        if i not in rep:
            rep.append(i)
print(rep)
