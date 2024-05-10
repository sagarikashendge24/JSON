# Q3.python oject ko json string mai convert karne ka program likhiy?
import json
c={"Name":"Ram", 
     "Class":13, 
     "Age": 23445}
a= json.dumps(c)
print(a)
print(type(a))     
