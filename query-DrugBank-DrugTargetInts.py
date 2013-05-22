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
from PDDI_Model import getPDDIDict


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

def getQueryString(offset):
    return """ 
PREFIX n2:	<http://bio2rdf.org/drugbank_resource:>
PREFIX n3:	<http://bio2rdf.org/drugbank_vocabulary:>
PREFIX n4:	<http://bio2rdf.org/drugbank:>
PREFIX n5:	<http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf:	<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsdh:	<http://www.w3.org/2001/XMLSchema#>

SELECT *
WHERE {
  ?s a n3:Drug-Target-Interaction; 
     n5:label ?label;
     n3:target ?target;
     n3:drug ?drug.

  ?target n3:gene-name ?geneName.

  ?drug n5:label ?drugGeneric.
  ?drug n3:brand ?drugBrand.
}
OFFSET %d
LIMIT 10000
""" % offset


if __name__ == "__main__":

    pddiDictL = []
    sparql_service = "http://drugbank.bio2rdf.org/sparql"

    offset = 0
    q = getQueryString(offset)
    resultset = queryEndpoint(sparql_service, q)

    while len(resultset["results"]["bindings"]) != 0 and offset < 20000:
        #print json.dumps(resultset,indent=1)
        # for i in range(0, len(resultset["results"]["bindings"])):
        #     uri = resultset["results"]["bindings"][i]["s"]["value"]
        #     newPDDI = getPDDIDict()
        #     newPDDI["source"] = sparql_service
        #     newPDDI["uri"] = uri
        #     newPDDI["drug1"] = resultset["results"]["bindings"][i]["d1"]["value"]
        #     newPDDI["drug2"] = resultset["results"]["bindings"][i]["d2"]["value"]
        #     newPDDI["label"] = resultset["results"]["bindings"][i]["label"]["value"]
            
        #     pddiDictL.append(newPDDI)

        # offset += 10000
        # q = getQueryString(offset)
        # resultset = queryEndpoint(sparql_service, q)

    print "INFO: No results at offset %d" % offset 

    f = open("drugbank-ddis.pickle","w")
    pickle.dump(pddiDictL, f)
    f.close()
        

