# def printdata(**kwargs):
#     return kwargs
# print(printdata(name="anu",rollno=1,dep='cse'))



def vaccinecheck(**kwargs):
    if kwargs["age"]>=18:
        return kwargs["name"]+" eligible"
    else:
        return kwargs["name"]+' not eligible'
print(vaccinecheck(name="anu",age=20))
print(vaccinecheck(name="mega",age=17))
