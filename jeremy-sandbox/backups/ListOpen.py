import pickle

hi = open("list.pickle", "r")

print pickle.load(hi)

hi.close()
