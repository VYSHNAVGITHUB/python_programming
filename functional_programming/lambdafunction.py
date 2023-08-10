square=lambda n:n**2              #1
print(square(8))


reminder=lambda n1,n2:n1%n2       #2
print(reminder(5,2))

first_letter=lambda s:s[0]        #3
print(first_letter('world'))
print(first_letter('hello'))

rotation=lambda s:s[-2:]+s[:-2]   #4
print(rotation("world"))
print(rotation("apple"))
