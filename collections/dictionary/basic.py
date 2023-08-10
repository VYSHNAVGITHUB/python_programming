d={"name":"anu","age":19,"place":'kochi','name':"amal"}
print(d)
print(type(d))
print(d.keys())   #list of keys
print(d.values()) #list of values

print(d["place"])
#print(d[0])     KEY ERROR

for i in d:   #i=key
    print(i,d[i])

