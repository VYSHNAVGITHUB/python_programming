import re
s="aaaabbbbbabaaaab"
matcher=re.finditer("ab",s)
#print(matcher)
count=0
for i in  matcher:
    count+=1
    print("match start at",i.start())
    print("match group",i.group())
print(count)