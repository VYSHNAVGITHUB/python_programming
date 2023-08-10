import  re
rule='[\w_/]+[@][g][m][a][i][l][.][c][o][m]'
s=input("enter string")
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print('valid')
else:
    print("invalid")