import json

text = '''
{
    "name": "小明",
    "age": 20,
    "skills": ["python","SQL"],
    "active": true,
    "score": null
}
'''

data = json.loads(text)
print(data)
print(type(data))
print(data["name"])
print(data["skills"][0])
print(data["active"],type(data["active"]))