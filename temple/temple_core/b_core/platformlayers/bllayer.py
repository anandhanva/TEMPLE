from flask.globals import request
from b_core.platformlayers import constantslayer
from b_core.responsemaster import responses
from b_core.maass import maasslogger
from b_core.statics import staticfunctions



def processLoginRequest(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(request,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    if(valHash == "true"):
        maasslogger(request, "Hashing Passed")
        # checking checksum
        createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
        checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        if(checksumcompare == "true"):
            try:

                comparedResults = constantslayer.checkuserfrmdb(hashchecksumNdata)
            except Exception as exCompareUser:
                maasslogger(request, str(exCompareUser))
                return str(exCompareUser)
            # If success return success response
            if(comparedResults['result'] == "Success"):
                return comparedResults['respdata']
            else:
                maasslogger(request, "Wrong Credentials")
                return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")
    
    else:
        maasslogger(request, str("Hash Mismatch, Incorrect Request"))
        return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")
