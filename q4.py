# Q4.python dictionary (sort by key)object ko json data ::mai convert karne ka program?

import json
a={
    '4':5,
    '6':7,
    '1':3,
    '2':4
}
b=open("q4.json","w")
json.dump(a,b,sort_keys=True)
b.close()