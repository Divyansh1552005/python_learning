import json

data = {
    "name" : "Divyansh",
    "age" : "21",
}

json_string = json.dumps(data, indent=2)
print(json_string)

print(type(json_string))

data2 = json.loads(json_string)

print(type(data2))
