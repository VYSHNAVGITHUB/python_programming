l=[1,2,3,4,5,6]
sum=int(input("enter sum"))
count=0
for i in l:
    for j in l:
        count+=1
        if i+j==sum:
             print(i,j)
print(count)             