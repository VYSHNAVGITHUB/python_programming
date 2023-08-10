d={1:100,2:200,3:300,4:400,5:500}
value=int(input('enter value to check'))
if value in d.values():
    print("present")
else:
    print("not present")