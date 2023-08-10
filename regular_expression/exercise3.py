import  re
rule='\W+[a-zA-Z]'
s=input("enter string")
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print('valid')
else:
    print("invalid")