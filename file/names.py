f1=open('name.txt','r')
f2=open('namewitha.txt','w')
for i in f1:
    if i[0]=="a":
        f2.write(i)

