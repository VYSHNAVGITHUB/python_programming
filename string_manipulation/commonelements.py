s1='abcd'
s2='cdef'
s=''
for i in  s1:
    if i in s2:
        s+=i
print(s)

