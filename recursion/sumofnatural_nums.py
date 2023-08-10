def sumofn(n):
    if n==0:
        return n
    else:
        return n+sumofn(n-1)
print(sumofn(5))
