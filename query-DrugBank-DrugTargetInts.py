""" Simple Python script to query http://drugbank.bio2rdf.org/sparql for Drug-target interactions"
    No extra libraries required.

# Authors: Richard D Boyce and Jeremy Jao
#
# May 2013
# 

"""

import json
import urllib2
import urllib
import traceback
import sys 
import pickle

sys.path = sys.path + ['.']
from PDTI_Model import getPDTIDict

#############  GLOBALS ###################################################################

GBM_LIST_F = "GBM_module_RM_PM_geneList.txt"
BRCA_LIST_F = "BRCA_module_RM_PM_geneList.txt"

############## FUNCTIONS  ##################################################################

def query(q,epr,f='application/json'):
    """Function that uses urllib/urllib2 to issue a SPARQL query.
       By default it requests json as data format for the SPARQL resultset"""

    try:
        params = {'query': q}
        params = urllib.urlencode(params)
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        request = urllib2.Request(epr+'?'+params)
        request.add_header('Accept', f)
        request.get_method = lambda: 'GET'
        url = opener.open(request)
        return url.read()
    except Exception, e:
        traceback.print_exc(file=sys.stdout)
        raise e


def queryEndpoint(sparql_service, q):
    print "query string: %s" % q
    json_string = query(q, sparql_service)
    #print "%s" % json_string
    resultset=json.loads(json_string)
    
    return resultset

def getQueryString(geneName, offset, limit):
    return """ 
PREFIX n2:	<http://bio2rdf.org/drugbank_resource:>
PREFIX n3:	<http://bio2rdf.org/drugbank_vocabulary:>
PREFIX n4:	<http://bio2rdf.org/drugbank:>
PREFIX n5:	<http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf:	<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsdh:	<http://www.w3.org/2001/XMLSchema#>

SELECT DISTINCT ?uri ?drugGeneric ?drugURI ?targetURI ?pharmacologicAction ?label
WHERE {
  ?uri a n3:Drug-Target-Interaction; 
     n5:label ?label;
     n3:target ?targetURI;
     n3:drug ?drugURI;
     n3:pharmacological-action ?pharmacologicAction.

  ?targetURI n3:gene-name "%s".

  ?drugURI n5:label ?drugGeneric.
}
# OFFSET %d
LIMIT %d
""" % (geneName, offset, limit)



########### MAIN  #####################################################################

if __name__ == "__main__":

    #geneListF = GBM_LIST_F
    geneListF = BRCA_LIST_F

    f = open(geneListF, "r")
    buf = f.read()
    f.close()
    geneList = buf.strip().split(";")

    pdtiDictD = {}
    sparql_service = "http://drugbank.bio2rdf.org/sparql"

    offset = 0
    limit = 5000

    for geneName in geneList:
        q = getQueryString(geneName, offset, limit) 
        resultset = queryEndpoint(sparql_service, q)

        # while len(resultset["results"]["bindings"]) != 0 and offset < 20000:
        if len(resultset["results"]["bindings"]) != 0:
            # print json.dumps(resultset,indent=1)
            for i in range(0, len(resultset["results"]["bindings"])):
                newPDTI = getPDTIDict()
                newPDTI["uri"] = resultset["results"]["bindings"][i]["uri"]["value"]
                newPDTI["source"] = sparql_service
                newPDTI["drugGeneric"] = resultset["results"]["bindings"][i]["drugGeneric"]["value"]
                newPDTI["drugURI"] = resultset["results"]["bindings"][i]["drugURI"]["value"]
                newPDTI["targetURI"] = resultset["results"]["bindings"][i]["targetURI"]["value"]
                newPDTI["pharmacologicAction"] = resultset["results"]["bindings"][i]["pharmacologicAction"]["value"]
                newPDTI["label"] = resultset["results"]["bindings"][i]["label"]["value"]

                #print "%s" % newPDTI

                if not pdtiDictD.has_key(geneName):
                    pdtiDictD[geneName] = [newPDTI]
                else:
                    pdtiDictD[geneName].append(newPDTI)
                
    #     offset += 10000
    #     q = getQueryString(offset)
    #     resultset = queryEndpoint(sparql_service, q)

    # print "INFO: No results at offset %d" % offset 

    pickleF = "drugbank-dtis.pickle"

    print "%d drug-target mappings found" % len(pdtiDictD.keys())
    print "genes mapped: %s" % pdtiDictD.keys()
    print "mapping data saved to %s" % pickleF

    f = open(pickleF,"w")
    pickle.dump(pdtiDictD, f)
    f.close()
        

