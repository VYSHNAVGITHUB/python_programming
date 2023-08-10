d=dict()
print(d)
print(type(d))

d1={}
print(d1)
print(type(d1))

#   Add element
#   method 1     -  can add single or multiple elements
d.update({1:6,9:5})
print(d)

#   method 2
d[4]=100
print(d)

#   update
d[1]=10
print(d)