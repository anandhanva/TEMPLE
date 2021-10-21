
from b_core.statics import dbmodules,dbconstants


def getDietybyTempleid(req):
    
    return req

def getPoojabyDietyid(req):
    try:
        dbQuery = {"pooja_templeid":req['datafrm']['diety_id']}
        req['database'] = "temple"
        req['collection'] = "pooja"
        datavalue =dbconstants.MongoAPI(req).read(dbQuery)
        print("listed",datavalue)
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        return str(e)
    return req

def getKanikkabyDietyid(req):
    return req

def getPrasadambyTempleid(req):
    try:
        dbQuery = {"prasadam_templeid":req['datafrm']['templeid']}
        req['database'] = "temple"
        req['collection'] = "prasadam"
        datavalue =dbconstants.MongoAPI(req).read(dbQuery)
        print("listed",datavalue)
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        return str(e)
    return req

def getPackageSizebyPrasadam(req):
    return req

def getOfferingbyTempleid(req):
    try:
        dbQuery = {"offering_templeid":req['datafrm']['templeid']}
        req['database'] = "temple"
        req['collection'] = "offering"
        datavalue =dbconstants.MongoAPI(req).read(dbQuery)
        print("listed",datavalue)
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        return str(e)
    return req

def getOfferingbyDietyid(req):
    return req