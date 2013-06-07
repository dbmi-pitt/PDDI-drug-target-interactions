import json

list = ["hi", "hello"]

f = open("listInJSON.txt", "w")

json.dump(list, f)

f.close()
