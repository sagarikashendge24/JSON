# Q6.Python object key unique key value ko access karne ka program likho?
import json

a={
 "a":  1,
 "a":  2,
 "a":  3, 
 "a": 4,   
 "b": 1, 
 "b": 2
 }

b=open("q6,json","w")
json.dump(a,b)
b.close()