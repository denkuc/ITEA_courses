import json

var = "!"

a = {
    "Name": f"Den{var}",
    "Students": ["1", "2", "3"]
}

b = json.dumps(a, indent=1)
print(b)


str_json = '{"name": "Den"}'
c = json.loads(str_json)
print(c)