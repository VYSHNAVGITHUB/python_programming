# read
f=open('data.txt','r')
# print f
for i in f:
    d=i.rstrip('\n')
    print(d)