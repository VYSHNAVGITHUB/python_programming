s='abcdaaabceffjkld'
e=''
for i in s:
    if i not in e:
        e+=i
    else:
        print(i)        