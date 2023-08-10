s=input('enter the string')
v='aeiou'
count=0
for i in s:
    if i in v:
        count=count+1
print("the num of vowals in the string=",count)