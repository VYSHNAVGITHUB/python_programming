sub1=float(input('enter the score of sub1'))
sub2=float(input('enter the score of sub2'))
sub3=float(input('enter the score of sub3'))
total=sub1+sub2+sub3

print('the total the score of the student is=',total)
print('the average score of the student is',total/3)
if sub1>=50 and sub2>=50 and sub3>=50:
    print("pass")
else:
    print('fail')