from flask.globals import request
from b_core.platformlayers import constantslayer
from b_core.responsemaster import responses
from b_core.maass.maasslogger import maasslogger
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
        maasslogger(req, str(e),request['modulename'],"SUCCESS")
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
    # if(valHash == "true"):
    maasslogger(request, "Hashing Passed",request['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = constantslayer.checkuserfrmdb(hashchecksumNdata)
        print(">>>>>>>",comparedResults)
        print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        maasslogger(request, str(exCompareUser))
        return str(exCompareUser)
    if(comparedResults['result'] == "Success"):


        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        print(">>>>>>Request",request)
        comparedResults['em_reqid'] = request['em_reqid']
        comparedResults['em_custid'] = request['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")

# CREATE ACCOUNT DEVASAM

def addTemple(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("INSERTED",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(request,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("INSERTINGHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    # if(valHash == "true"):
    #     maasslogger(request, "Hashing Passed")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
    #     if(checksumcompare == "true"):
    try:

        comparedResults = constantslayer.addTempleApi(hashchecksumNdata)
    except Exception as exCompareUser:
        maasslogger(request, str(exCompareUser))
        return str(exCompareUser)
    if(comparedResults['result'] == "Success"):

        print("COMPARde",comparedResults)


        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully inserted"
        print(">>>>>>Request",request)
        comparedResults['em_reqid'] = request['em_reqid']
        comparedResults['em_custid'] = request['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ""
        comparedResults['resp_frm_maass'] = ""
        comparedResults['resp_frm_blockc'] = ""
        comparedResults['resp_frm_mojaloop'] = ""
        comparedResults['resp_frm_rulengn'] = ""
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Failed")
        return responses.standardErrorResponseToBE("INSERTING","Wrong!!")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")

# LIST TEMPLE
def listTempleApi(req):
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
    # if(valHash == "true"):
    #     maasslogger(request, "Hashing Passed")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
    #     if(checksumcompare == "true"):
    try:

        comparedResults = constantslayer.listTempleApi(hashchecksumNdata)
    except Exception as exCompareUser:
        maasslogger(request, str(exCompareUser))
        return str(exCompareUser)
    if(comparedResults['result'] == "Success"):
        print("compare*************",comparedResults)


        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        print(">>>>>>Request",request)
        comparedResults['em_reqid'] = request['em_reqid']
        comparedResults['em_custid'] = request['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")
    
    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")
# CREATE TEMPLE ADMIN
def createTempleAdmin(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("INSERTED",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(request,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("INSERTINGHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    # if(valHash == "true"):
    #     maasslogger(request, "Hashing Passed")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
    #     if(checksumcompare == "true"):
    try:

        comparedResults = constantslayer.createTempleAdminApi(hashchecksumNdata)
    except Exception as exCompareUser:
        maasslogger(request, str(exCompareUser))
        return str(exCompareUser)
    if(comparedResults['result'] == "Success"):

        print("COMPARde",comparedResults)


        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully inserted"
        print(">>>>>>Request",request)
        comparedResults['em_reqid'] = request['em_reqid']
        comparedResults['em_custid'] = request['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ""
        comparedResults['resp_frm_maass'] = ""
        comparedResults['resp_frm_blockc'] = ""
        comparedResults['resp_frm_mojaloop'] = ""
        comparedResults['resp_frm_rulengn'] = ""
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Failed")
        return responses.standardErrorResponseToBE("INSERTING","Wrong!!")



# LIST TEMPLE ADMIN
def listTempleAdminApi(req):
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
    # if(valHash == "true"):
    #     maasslogger(request, "Hashing Passed")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
    #     if(checksumcompare == "true"):
    try:

        comparedResults = constantslayer.listTempleAdminApi(hashchecksumNdata)
    except Exception as exCompareUser:
        maasslogger(request, str(exCompareUser))
        return str(exCompareUser)
    if(comparedResults['result'] == "Success"):


        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        print(">>>>>>Request",request)
        comparedResults['em_reqid'] = request['em_reqid']
        comparedResults['em_custid'] = request['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")
    
    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")

# ADD ACCOUNT
def createAccount(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("INSERTED",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(request,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("INSERTINGHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    # if(valHash == "true"):
    #     maasslogger(request, "Hashing Passed")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
    #     if(checksumcompare == "true"):
    try:

        comparedResults = constantslayer.createAccountApi(hashchecksumNdata)
    except Exception as exCompareUser:
        maasslogger(request, str(exCompareUser))
        return str(exCompareUser)
    if(comparedResults['result'] == "Success"):

        print("COMPARde",comparedResults)


        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully inserted"
        print(">>>>>>Request",request)
        comparedResults['em_reqid'] = request['em_reqid']
        comparedResults['em_custid'] = request['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ""
        comparedResults['resp_frm_maass'] = ""
        comparedResults['resp_frm_blockc'] = ""
        comparedResults['resp_frm_mojaloop'] = ""
        comparedResults['resp_frm_rulengn'] = ""
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Failed")
        return responses.standardErrorResponseToBE("INSERTING","Wrong!!")


# LIST ACCOUNT
def listAccountApi(req):
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
    # if(valHash == "true"):
    #     maasslogger(request, "Hashing Passed")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
    #     if(checksumcompare == "true"):
    try:

        comparedResults = constantslayer.listAccountApi(hashchecksumNdata)
    except Exception as exCompareUser:
        maasslogger(request, str(exCompareUser))
        return str(exCompareUser)
    if(comparedResults['result'] == "Success"):


        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        print(">>>>>>Request",request)
        comparedResults['em_reqid'] = request['em_reqid']
        comparedResults['em_custid'] = request['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")
