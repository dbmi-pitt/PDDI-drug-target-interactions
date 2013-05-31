import sys,pickle,codecs

sys.path = sys.path + ['.']
from PDTI_Model import getPDTIDict

#picklF = "results/pharmgkb-dtis-BRCA_list-string-matching-no-syns-05232013.pickle"
#outF = "results/pharmgkb-dtis-BRCA_list-string-matching-no-syns-05232013.tsv"
#picklF = "results/drugbank-dtis-BRCA_list-string-matching-no-syns-05232013.pickle"
#outF = "results/drugbank-dtis-BRCA_list-string-matching-no-syns-05232013.tsv"

#picklF = "results/pharmgkb-dtis-GBM_list-string-matching-no-syns-05232013.pickle"
#outF = "results/pharmgkb-dtis-GBM_list-string-matching-no-syns-05232013.tsv"
picklF = "results/drugbank-dtis-GBM_list-string-matching-no-syns-05232013.pickle"
outF = "results/drugbank-dtis-GBM_list-string-matching-no-syns-05232013.tsv"

f = open(picklF,"r")
pdtiDictD = pickle.load(f)
f.close()
        
outstr = ""
for k,v in pdtiDictD.iteritems():
    for d in v:
        outstr += u"%s	%s\r\n" % (k, [d['drugGeneric'], d['uri'], d['pharmacologicAction'], d['label']])
outstr += u"\r\n"

f = codecs.open(outF,"w","utf-8")
f.write(outstr)
f.close()


