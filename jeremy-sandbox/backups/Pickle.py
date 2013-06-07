import pickle

list = ("hi", "hello")

File = "list.pickle"

f = open(File,"w")
pickle.dump(list, f)
f.close()
