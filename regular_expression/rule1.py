import re
s="abcddd ABC@123"
x='[abc]'
matcher=re.finditer(x,s)
count=0
for i in  matcher:
    count+=1
    print("match start at",i.start())
    print("match group",i.group())
print(count)