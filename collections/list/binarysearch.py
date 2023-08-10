l=[1,6,2,7,8,9,34,56,78,11,99,21]
e=100
l.sort()
low=0
upper=len(l)-1
flag=0
count=0
while low<=upper:
    count+=1
    middle_index=(low+upper)//2
    if e==l[middle_index]:
        flag=1
        break
    elif e>l[middle_index]:
        low=middle_index+1
    elif e<l[middle_index]:
        upper=middle_index-1
if flag==1:
    print("present")
else:
    print("not present")