# PDTI_Model.py
#
# A simple model used to capture relevant values for potential drug-target interactions (PDTI)

## The current model for a PDTI from any of the sources:
# "uri": uri to the PDTI in the source graph
# "drugGeneric": generic name for the drug
# "drugBrand": brand name for the  drug 
# "drugURI": the RDF URI to the drug instance
# "targetURI": the RDF URI to the target instance
# "label": unstructured text explanation of the PDTI
# "pharmacologicAction": text describing the anticipated pharmacologic effect
# "source": uri of the graph from which the PDTI came from

def getPDTIDict():
    return {"uri":None,
            "drugGeneric":None,
            "drugURI":None,
            "targetURI":None,
            "label":None,
            "pharmacologicAction":None,
            "source":None
            }
