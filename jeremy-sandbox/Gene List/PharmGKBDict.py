# PharmGKBDict.py
#
# A class for PharmGKB gene data. The class provides methods to read
# the Phamgkb gene file and store relevant data in a dictionary to a
# pickle for later use
#
# Jeremy Jao, Dr. Richard Boyce
# University of Pittsburgh: DBMI
# 6/19/2013
# 


import csv
import sys
import cPickle

csv.field_size_limit(sys.maxint)

class PharmGKBDict:
    
    def __init__(self):
        self.data = {}

    def readData(path):
        with open(path, 'rb') as f:
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
                    self.data.update({row[4]: e})

    def writeData(path):
        with open(path, 'w') as f:
            cPickle.dump(d, f)
