import re
s="aaa abbb aaaaa aa @ 123"
x='a$'
matcher=re.finditer(x,s)
count=0
for i in  matcher:
    count+=1
    print("match start at",i.start())
    print("match group",i.group())
print(count)