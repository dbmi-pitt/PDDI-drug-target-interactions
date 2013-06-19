import csv
import sys
import cPickle

# Jeremy Jao, Dr. Richard Boyce
# University of Pittsburgh: DBMI
# 6/18/2013
# 
# This program is really nice. What I did is I make a dictionary list based on the symbol; this is the KEY. The value of the symbol is a dictionary of the row! Then it will store the dictionary with CPickle so we don't run this
# script everytime we want to see the dictionary.
# One problem is that some keys are not symbols but are dates. We should fix this later, but that is an easy fix.
# Other problem is the keys are unsorted. It will still be forever better than my funny algorithm. Python's so useful..........
#
# Reason for a value as a dictionary for the key is because we can make use of the other values inside with a key, so it's just easier to find things.
# I can also do it based on the PharmGKB ID if need be but this seems like this is best for our use.
# I have a pickleReader.py that will read whatever is in the dictionary.

class PharmGKBDict:
    csv.field_size_limit(sys.maxint)
    
    d = {}
    
    pharmID = ''
    entrezID = ''
    ensembleID = ''
    name = ''
    alternateNames = ''
    alternateSymbols = ''
    isVIP = ''
    hasVariantAnnotation = ''
    reference = ''
    cpicGuide = ''
    
    with open('genes.tsv', 'rb') as f:
        reader = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
        for i, row in enumerate(reader):
            if i == 0:
                pharmID = row[0]
                entrezID = row[1]
                ensembleID = row[2]
                name = row[3]
                alternateNames = row[5]
                alternateSymbols = row[6]
                isVIP = row[7]
                hasVariantAnnotation = row[8]
                reference = row[9]
                cpicGuide = row[10]
            else:
                
                referenceString = row[9].split(',')
                referenceList = []
                for col in referenceString:
                    referenceList.append(col)
                    
                altSymbString = row[6].split(',')
                altSymbolsList = []
                for col in altSymbString:
                    altSymbolsList.append(col)
                
                e = {pharmID: row[0], entrezID: row[1], ensembleID: row[2], name: row[3], alternateNames: row[5], alternateSymbols: altSymbolsList, isVIP: row[7], hasVariantAnnotation: row[8], reference: referenceList, cpicGuide: row[10]}
                d.update({row[4]: e})
                
    files = open('geneDictionary.pickle', 'w')
    cPickle.dump(d, files, protocol=0) # dunno what protocol means......