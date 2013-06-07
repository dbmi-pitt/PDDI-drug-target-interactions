import json

list = {"a":["hi","goodbye"], "b":"hello"}

f = open("listInJSON.txt", "w")

json.dump(list, f)

f.close()
