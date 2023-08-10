import re
x='[P][y]\d{4}'
f=open('reg.txt','r')
f1=open('pyreg.txt','w')
for i in f:
    d=i.rstrip('\n')
    matcher=re.fullmatch(x,d)
    if matcher is not None:
        f1.write(i)
