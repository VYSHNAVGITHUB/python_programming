import  re
rule='[a][\w\W]{3,8}[b]'
s=input("enter string")
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print('valid')
else:
    print("invalid")