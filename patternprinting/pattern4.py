space=6
for i in range(5):
    for k in range(space):
        print(end=' ')
    space=space-1
    for j in range(i):
        print("*",end=" ")
    print()
