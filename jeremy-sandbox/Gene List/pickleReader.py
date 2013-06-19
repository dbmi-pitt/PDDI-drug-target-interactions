# Jeremy Jao
# University of Pittsburgh: DBMI
# 6/18/2013
#
# This is the thing that returns the dictionary of the key. we can edit more code to return different values in the keys (gene) in each dictionary inside the dictionary.
# my sys.argv isn't working in my situation due to my IDE (nor do I not know how it would work.... but yeah........... It's easy to code this.

import cPickle
#import sys
#
#arg = sys.argv[0]

print "Displaying dictionary for " + "MESTIT1"

hi = open("geneDictionary.pickle", "r")

hello = cPickle.load(hi)

print hello["MESTIT1"]