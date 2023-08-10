# str=input('enter string')
# s=""
# for i in str:
#     if i in "aeiou":
#         s=s+i
# print("s=",s)
#create string without vowals
word=input('enter string')
s=""
for i in word:
    if i not in "aeiou":
        s=s+i
print(s)



