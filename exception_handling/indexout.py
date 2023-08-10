l=[1,2,3]
index=int(input('enter index'))
try:
    print(l[index])
# except:
#     print("index out error")

except Exception as e:
    print(e)
finally:
    print("in finally")