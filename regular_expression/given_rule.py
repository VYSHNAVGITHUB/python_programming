import  re
rule='\d[a-zA-Z]+\d'
s=input("enter string")
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print('valid')
else:
    print("invalid")