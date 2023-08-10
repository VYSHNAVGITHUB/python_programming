s=input('enter word')
n=""
for i in s:
    if i not in n:
        n+=i
    else:
        print(i)
        break