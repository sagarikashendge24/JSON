# Q8.Tumhare pass four employes ki details hai list mai:-

# a=["neelam","komal","anuradha","Abhishek"]
# b=["programer","trainer","HR","manager"]
# c=[24,24,25,29]
# d=[2400,20000,40000,63000]
# e=["emp1","emp2","emp3","emp4"]
# i=0
# f={}
# while i<len(a):
#     new={"name":a[i],"age":b[i],"designation":c[i],"salary":d[i]}
#     f.update({e[i]:new})
#     print(f)
#     i=i+1   
   

a=["neelam","programer","24","2400"]
keys=["name","desination","age","salary"]
h={}
g={}

b={}
for i in range(len(a)):
    b[keys[i]]=a[i]
l="employee1",(b)   


b=["komal","trainer","24","20000"]
k={}
for i in range(len(b)):
    k[keys[i]]=b[i]
m="employee2",(k)

c=["anuradha","HR","25","40000"]
j={}
for i in range(len(c)):
    j[keys[i]]=c[i]
n="employee3",(j)


d=["Abhishek","manager","29","63000"] 
s={}
for i in range(len(d)):
    s[keys[i]]=d[i]
v="employee4",(s )
z=l,m,n,v
g.update(z)
my=g

import json

write=open("sagarika.json","w") 
json.dump(my,write,indent=6)
write.close()
