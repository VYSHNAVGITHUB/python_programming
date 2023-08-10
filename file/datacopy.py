f1=open('data1.txt','r')
f2=open('datacopy.txt','w')
for i in f1:
    f2.write(i)