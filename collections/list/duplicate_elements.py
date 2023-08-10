 l=[1,3,5,6,7,8,2,3,1,2,3]
 print(len(l))
 l1=[]
 for i in l:
     if i not in l1:
      l1.append(i)
     else:
         print(i)

lst=[1,0,7,5,9,2,3,5,7,2,0,1,10]
l2=[]
[l2.append(i) for i in lst if i not in l2]
print(i)

