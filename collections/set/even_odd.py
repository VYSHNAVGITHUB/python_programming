num={1,3,7,8,54,34,90,12,34}
even=set()
odd=set()
for i in num:
    if i%2==0:
        even.add(i)
    else:
        odd.add(i)
print(even)
print(odd)
