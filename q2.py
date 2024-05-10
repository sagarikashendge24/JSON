# Q2.python object to json data

# dump():-python object -json file

import json
a={  "name":"David",
     "class":"I",
     "age":6,
     "color":"red"}


k=open("q2.json","w") 
json.dump(a,k,indent=12)              
k.close()