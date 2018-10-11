import json

data='''[
{"id":"001",
"x":"64",
"name":"Jose"
},
{"id":"002",
"x":"32",
"name":"Alex"
}]'''

info=json.loads(data)
print(type(info))

for i in info:
    print(type(i))
    print (i['id'], i['x'], i['name'])
