def prime(n):
    for i in range (2,n):
        if n%i==0:
            return "not prime"
            break
    else:
        return "prime"
print(prime(17))