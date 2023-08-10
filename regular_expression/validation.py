import  re
rule='[K][L]\d{2}[A-Z]{2}\d{4}'
s=input("enter string")
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print('valid')
else:
    print("invalid")