def fac(num):
    fac = 1
    for i in range(1, num + 1):
        fac *= i

    print('The factorial of the', num, "is", fac)
fac(5)
fac(6)