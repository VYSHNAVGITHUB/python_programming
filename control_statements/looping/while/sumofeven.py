num=int(input('enter num'))
sum=0
num1=2
while num1<=num:
    if num1%2==0:
        sum+=num
        num1=num1+2
print('sum of even num=',sum)