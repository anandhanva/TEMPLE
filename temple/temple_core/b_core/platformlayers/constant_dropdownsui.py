from b_core.statics import dbconstants


def getDietybyTempleid(req):
    try:
        dbQuery = {"diety_templeid":req['datafrm']['templeid']}
        req['database'] = "temple"
        req['collection'] = "diety"
        datavalue = dbconstants.MongoAPI(req).read(dbQuery)
        print("listed",datavalue)
        return datavalue  
    except ValueError as e:
        print("EXCEPTION",str(e))
        return str(e)
    except Exception as e:
        print("FAILED",str(e))

def getPoojabyDietyid(req):
    return req

def getKanikkabyDietyid(req):
    try:
        dbQuery = {"kanikka":req['datafrm']['diety_id']}
        req['database'] = "temple"
        req['collection'] = "kanikka"
        datavalue = dbconstants.MongoAPI(req).read(dbQuery)
        print("listed",datavalue)
        return datavalue  
    except ValueError as e:
        print("EXCEPTION",str(e))
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
    return req

def getPrasadambyTempleid(req):
    return req

def getPackageSizebyPrasadam(req):
    
    try:
        dbQuery = {"package_size":req['datafrm']['prasadam_name']}
        req['database'] = "temple"
        req['collection'] = "prasadam"
        datavalue = dbconstants.MongoAPI(req).read(dbQuery)
        print("listed",datavalue)
        return datavalue  
    except ValueError as e:
        print("EXCEPTION",str(e))
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
    return req


def getOfferingbyTempleid(req):
    return req

def getOfferingbyDietyid(req):
    try:
        dbQuery = {"offering_id":req['datafrm']['templeid']}
        req['database'] = "temple"
        req['collection'] = "offering"
        datavalue = dbconstants.MongoAPI(req).read(dbQuery)
        print("listed",datavalue)
        return datavalue  
    except ValueError as e:
        print("EXCEPTION",str(e))
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
    return req
    