s={1,2,3,4,5,6,7,8,9}
even=set(filter(lambda n:n%2==0,s))
print(even)
odd=set(filter(lambda n:n%2!=0,s))
print(odd)