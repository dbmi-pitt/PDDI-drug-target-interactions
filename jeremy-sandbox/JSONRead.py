import json

f = open("listInJSON.txt", "r")

hi = json.load(f)

print hi
f.close()
