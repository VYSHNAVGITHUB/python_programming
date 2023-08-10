range1=int(input("range1"))
range2=int(input("range2"))
for i in range(range1,range2+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)