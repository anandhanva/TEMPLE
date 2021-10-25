import json
from flask.globals import request
from b_core.platformlayers import constantslayer,constant_dropdownsui
from b_core.responsemaster import responses
from b_core.maass.maasslogger import maasslogger
from b_core.statics import staticfunctions,blconstants




def processLoginRequest(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed",req['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.checkuserfrmdb(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123456")
        maasslogger(req, str(exCompareUser), "LOGIN", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
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
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("INSERTED",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(request,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("INSERTINGHASH",str(e))

    maasslogger(request,"hashing passes",request['modulename'],"SUCCESS")

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
        maasslogger(req, str(exCompareUser))
        return str(exCompareUser)
    if(comparedResults['result'] == "Success"):

        print("COMPARde",comparedResults)


        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully inserted"
        print(">>>>>>Request",request)
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
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
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(request,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    maasslogger(request,"hashing passes",request['modulename'],"SUCCESS")

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
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("INSERTED",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(request,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("INSERTINGHASH",str(e))
    maasslogger(request,"hashing passess",request['modulename'],"SUCCESS")
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
    maasslogger(request,"hashing passess",request['modulename'],"SUCCESS")

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
        # maasslogger(req, str(e))
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
    maasslogger(request,"hashing passes",request['modulename'],"SUCCESS")
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
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(request,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    maasslogger(request,"hashing passess",request['modulename'],"SUCCESS")

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
        # print(">>>>>>Request",request)
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
        # comparedResults['resp_frm_mojaloop'] = ""
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")

#===============================================================================================================
#ACCOUNT STATEMENT - FINANCE ADMIN

def accstmtfrmdb(req):
#Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("ACCOUNT STATEMENT",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(request,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("ACCOUNTSTATEMENTHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(request, "Hashing Passed",request['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.accstmtfrmdb(hashchecksumNdata)
        comparedResults = blconstants.accstmtfrmdbApi(hashchecksumNdata)
    except Exception as exCompareUser:
        maasslogger(request, str(exCompareUser))
        return str(exCompareUser)
    # If success return success response
    if(comparedResults['result'] == "Success"):

        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully printed"
        comparedResults['em_reqid'] = request['em_reqid']
        comparedResults['em_custid'] = request['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ""
        comparedResults['resp_frm_maass'] = ""
        comparedResults['resp_frm_blockc'] = ""
        comparedResults['resp_frm_mojaloop'] = ""
        comparedResults['resp_frm_rulengn'] = ""
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")

# CREATE FIN ADMIN
def createFinAdmin(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
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
    maasslogger(request,"hashing passes",request['modulename'],"SUCCESS")
    #     maasslogger(request, "Hashing Passed")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
    #     if(checksumcompare == "true"):
    try:

        comparedResults = constantslayer.createFinAdminApi(hashchecksumNdata)
        comparedResults=constantslayer.convinptodict(comparedResults)
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
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Failed")
        return responses.standardErrorResponseToBE("INSERTING","Wrong!!")

# ADD POOJA
def createPooja(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST CREATE POOJA ",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed","CREATEPOOJA","SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.createPoojaApi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123457")
        maasslogger(request, str(exCompareUser), "LOGIN", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")

# LIST POOJA
def listPooja(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    req = json.dumps(req)
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    maasslogger(req,"hashing passes","LISTPOOJA","SUCCESS")

    try:

        comparedResults = blconstants.listTemplePoojaApi(hashchecksumNdata)
        comparedResult = constantslayer.convinptodict(comparedResults)
        if(len(comparedResults) >= 1):
            comparedResults['result'] = "Success"
    except Exception as exCompareUser:
        maasslogger(request, str(exCompareUser),"LISTPOOJA", "FAILURE")
        return str(exCompareUser)
    errresp = "Error-Response"
    reqs = json.loads(req)
    if(errresp in comparedResults):
        print("COMPARERESULT>>>>>>>",comparedResults)
        failureResults = {}
        failureResults['em_reqid'] = reqs['em_reqid']
        failureResults['em_custid'] = reqs['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LISTED": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",failureResults)
        return staticfunctions.coretobe_response(failureResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults = {}
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully listed"
        comparedResults['em_reqid'] = reqs['em_reqid']
        comparedResults['em_custid'] = reqs['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResult
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(req, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LISTED","Wrong Credentials")
    
    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")

# CREATE OFFERING
def createOfferings(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("CREAOFFERINGS",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed","CREAOFFERINGS","SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.createOfferingApi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123458")
        maasslogger(request, str(exCompareUser), "CREAOFFERINGS", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully inserted"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("INSERTED","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")
# LIST OFFERINGS
def listOfferings(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(request,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    maasslogger(request,"hashing passes","LISTOFFERINGS","SUCCESS")

    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    # if(valHash == "true"):
    #     maasslogger(request, "Hashing Passed")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
    #     if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.listTempleOfferingApi(hashchecksumNdata)
        comparedResult = constantslayer.convinptodict(comparedResults)
        if(len(comparedResults) >= 1):
            comparedResults['result'] = "Success"
    except Exception as exCompareUser:
        maasslogger(request, str(exCompareUser),"CREAOFFERINGS", "FAILURE")
        return str(exCompareUser)
    errresp = "Error-Response"
    if(errresp in comparedResult):
        failureResults = {}
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LISTED": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResult)
        return staticfunctions.coretobe_response(comparedResult)

    elif(comparedResult['result'] == "Success"):
        comparedResultz = {}

        comparedResultz['resp_code'] = 800
        comparedResultz['resp_type'] = "SUCCESS"
        comparedResultz['message'] = "Successfully listed"
        comparedResultz['em_reqid'] = request['em_reqid']
        comparedResultz['em_custid'] = request['em_custid']
        comparedResultz['resp_frm_bank'] = ""
        comparedResultz['resp_frm_ewire'] = comparedResult
        comparedResultz['resp_frm_cbs'] = ""
        comparedResultz['resp_frm_ext'] = ['resp_frm_ext']
        comparedResultz['resp_frm_maass'] = ['resp_frm_maass']
        comparedResultz['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResultz['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResultz['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResultz)
        return staticfunctions.coretobe_response(comparedResultz)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LISTED","Wrong Credentials")
    
    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")

# CREATE PRASDHAM
def createPrasadam(req):
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed",req['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.createPrasadamApi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123459")
        maasslogger(request, str(exCompareUser), "CREAPRASADAM", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully inserted"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("INSERTED","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")
# LIST PRASADAM
def listPrasadam(req):
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(request,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    maasslogger(request,"hashing passes",request['modulename'],"SUCCESS")

    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    # if(valHash == "true"):
    #     maasslogger(request, "Hashing Passed")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
    #     if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.listTemplePrasadamApi(hashchecksumNdata)
        comparedResult = constantslayer.convinptodict(comparedResults)
        if(len(comparedResults) >= 1):
            comparedResults['result'] = "Success"
    except Exception as exCompareUser:
        maasslogger(request, str(exCompareUser),"CREAPRASADAM", "FAILURE")
        return str(exCompareUser)
    errresp = "Error-Response"
    if(errresp in comparedResult):
        failureResults = {}
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LISTED": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResult)
        return staticfunctions.coretobe_response(comparedResult)

    elif(comparedResult['result'] == "Success"):
        comparedResultz = {}

        comparedResultz['resp_code'] = 800
        comparedResultz['resp_type'] = "SUCCESS"
        comparedResultz['message'] = "Successfully listed"
        comparedResultz['em_reqid'] = request['em_reqid']
        comparedResultz['em_custid'] = request['em_custid']
        comparedResultz['resp_frm_bank'] = ""
        comparedResultz['resp_frm_ewire'] = comparedResult
        comparedResultz['resp_frm_cbs'] = ""
        comparedResultz['resp_frm_ext'] = ['resp_frm_ext']
        comparedResultz['resp_frm_maass'] = ['resp_frm_maass']
        comparedResultz['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResultz['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResultz['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResultz)
        return staticfunctions.coretobe_response(comparedResultz)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LISTED","Wrong Credentials")
    
    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")

# CREATE DIETY
def createDiety(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("CREAOFFERINGS",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed","CREATEDIETY","SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.createDietyApi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123458")
        maasslogger(request, str(exCompareUser), "CREATEDIETY", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully inserted"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("INSERTED","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")

# LIST DIETY
def listDiety(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(request,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    maasslogger(request,"hashing passes",request['modulename'],"SUCCESS")

    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    # if(valHash == "true"):
    #     maasslogger(request, "Hashing Passed")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
    #     if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.listTempleDietyApi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)

    except Exception as exCompareUser:
        maasslogger(request, str(exCompareUser))
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")

    
# CREATE HISTORY
def createHistory(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed","CREHISTORY","SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.createHistoryApi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123450")
        maasslogger(request, str(exCompareUser), "CREHISTORY", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")
# LIST HISTORY
def listHistory(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(request,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    maasslogger(request,"hashing passes",request['modulename'],"SUCCESS")

    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    # if(valHash == "true"):
    #     maasslogger(request, "Hashing Passed")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
    #     if(checksumcompare == "true"):
    try:
        comparedResults = blconstants.listTempleHistoryApi(hashchecksumNdata)
    except Exception as exCompareUser:
        maasslogger(request, str(exCompareUser))
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = request['em_reqid']
        failureResults['em_custid'] = request['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",failureResults)
        return staticfunctions.coretobe_response(failureResults)
    elif(comparedResults['result'] == "Success"):
        compareResults = {}
        compareResults['resp_code'] = 800
        compareResults['resp_type'] = "SUCCESS"
        compareResults['message'] = "Successfully login"
        compareResults['em_reqid'] = request['em_reqid']
        compareResults['em_custid'] = request['em_custid']
        compareResults['resp_frm_bank'] = ""
        compareResults['resp_frm_ewire'] = comparedResults
        compareResults['resp_frm_cbs'] = ""
        compareResults['resp_frm_ext'] = ['resp_frm_ext']
        compareResults['resp_frm_maass'] = ['resp_frm_maass']
        compareResults['resp_frm_blockc'] = ['resp_frm_blockc']
        compareResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        compareResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",compareResults)
        return staticfunctions.coretobe_response(compareResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")
# DROPDOWN DIETY
def dropdownDietyApi(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("DROPDOWN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(request,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    maasslogger(request,"hashing passes",request['modulename'],"SUCCESS")

    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    # if(valHash == "true"):
    #     maasslogger(request, "Hashing Passed")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
    #     if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.drpdwnTempdietyApi(hashchecksumNdata)
        comparedResult = constantslayer.convinptodict(comparedResults)
        if(len(comparedResults) >= 1):
            comparedResults['result'] = "Success"
    except Exception as exCompareUser:
        maasslogger(request, str(exCompareUser),"DROPDOWNDIETY", "FAILURE")
        return str(exCompareUser)
    errresp = "Error-Response"
    if(errresp in comparedResult):
        failureResults = {}
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LISTED": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResult)
        return staticfunctions.coretobe_response(comparedResult)

    elif(comparedResult['result'] == "Success"):
        comparedResultz = {}

        comparedResultz['resp_code'] = 800
        comparedResultz['resp_type'] = "SUCCESS"
        comparedResultz['message'] = "Successfully listed"
        comparedResultz['em_reqid'] = request['em_reqid']
        comparedResultz['em_custid'] = request['em_custid']
        comparedResultz['resp_frm_bank'] = ""
        comparedResultz['resp_frm_ewire'] = comparedResult
        comparedResultz['resp_frm_cbs'] = ""
        comparedResultz['resp_frm_ext'] = ['resp_frm_ext']
        comparedResultz['resp_frm_maass'] = ['resp_frm_maass']
        comparedResultz['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResultz['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResultz['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResultz)
        return staticfunctions.coretobe_response(comparedResultz)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LISTED","Wrong Credentials")
    
    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")



# DROPDOWN DIETY
def dropdownRateApi(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("DROPDOWN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(request,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    maasslogger(request,"hashing passes",request['modulename'],"SUCCESS")

    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    # if(valHash == "true"):
    #     maasslogger(request, "Hashing Passed")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
    #     if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.drpdwnTemprateApi(hashchecksumNdata)
        comparedResult = constantslayer.convinptodict(comparedResults)
        if(len(comparedResults) >= 1):
            comparedResults['result'] = "Success"
    except Exception as exCompareUser:
        maasslogger(request, str(exCompareUser),"DROPDOWNRATE", "FAILURE")
        return str(exCompareUser)
    errresp = "Error-Response"
    if(errresp in comparedResult):
        failureResults = {}
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LISTED": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResult)
        return staticfunctions.coretobe_response(comparedResult)

    elif(comparedResult['result'] == "Success"):
        comparedResultz = {}

        comparedResultz['resp_code'] = 800
        comparedResultz['resp_type'] = "SUCCESS"
        comparedResultz['message'] = "Successfully listed"
        comparedResultz['em_reqid'] = request['em_reqid']
        comparedResultz['em_custid'] = request['em_custid']
        comparedResultz['resp_frm_bank'] = ""
        comparedResultz['resp_frm_ewire'] = comparedResult
        comparedResultz['resp_frm_cbs'] = ""
        comparedResultz['resp_frm_ext'] = ['resp_frm_ext']
        comparedResultz['resp_frm_maass'] = ['resp_frm_maass']
        comparedResultz['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResultz['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResultz['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResultz)
        return staticfunctions.coretobe_response(comparedResultz)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LISTED","Wrong Credentials")
    
    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")

# DROPDOWN QUANTITY OF PRASADAM
def dropdownPrasadamQtyApi(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("DROPDOWN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(request,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    maasslogger(request,"hashing passes",request['modulename'],"SUCCESS")

    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    # if(valHash == "true"):
    #     maasslogger(request, "Hashing Passed")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
    #     if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.drpdwnPrasadamQtyApi(hashchecksumNdata)
        comparedResult = constantslayer.convinptodict(comparedResults)
        if(len(comparedResults) >= 1):
            comparedResults['result'] = "Success"
    except Exception as exCompareUser:
        maasslogger(request, str(exCompareUser),"DROPDOWNQTY", "FAILURE")
        return str(exCompareUser)
    errresp = "Error-Response"
    if(errresp in comparedResult):
        failureResults = {}
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LISTED": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResult)
        return staticfunctions.coretobe_response(comparedResult)

    elif(comparedResult['result'] == "Success"):
        comparedResultz = {}

        comparedResultz['resp_code'] = 800
        comparedResultz['resp_type'] = "SUCCESS"
        comparedResultz['message'] = "Successfully listed"
        comparedResultz['em_reqid'] = request['em_reqid']
        comparedResultz['em_custid'] = request['em_custid']
        comparedResultz['resp_frm_bank'] = ""
        comparedResultz['resp_frm_ewire'] = comparedResult
        comparedResultz['resp_frm_cbs'] = ""
        comparedResultz['resp_frm_ext'] = ['resp_frm_ext']
        comparedResultz['resp_frm_maass'] = ['resp_frm_maass']
        comparedResultz['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResultz['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResultz['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResultz)
        return staticfunctions.coretobe_response(comparedResultz)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LISTED","Wrong Credentials")
    
    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")
# CREATE KANIKKA
def createKanikkaApi(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed",req['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.createKanikkaApi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123450")
        maasslogger(request, str(exCompareUser), "LOGIN", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")
# ADD AIRPORT
def addAirportApi(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed",req['modulename'],"SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.createAirportApi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123450")
        maasslogger(request, str(exCompareUser), "CREHISTORY", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")

    # else:
    #     maasslogger(request, str("Hash Mismatch, Incorrect Request"))
    #     return responses.standardErrorResponseToBE("LOGIN","Hash Mismatch, Incorrect Request")


# ADD POOJA
def createStay(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed","CREATEPOOJA","SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.createStayApi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123457")
        maasslogger(request, str(exCompareUser), "LOGIN", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")


# LIST POOJA
def listStay(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    req = json.dumps(req)
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    maasslogger(req,"hashing passes","LISTPOOJA","SUCCESS")

    try:

        comparedResults = blconstants.listTempleStayApi(hashchecksumNdata)
        comparedResult = constantslayer.convinptodict(comparedResults)
        if(len(comparedResults) >= 1):
            comparedResults['result'] = "Success"
    except Exception as exCompareUser:
        maasslogger(request, str(exCompareUser),"LISTPOOJA", "FAILURE")
        return str(exCompareUser)
    errresp = "Error-Response"
    reqs = json.loads(req)
    if(errresp in comparedResults):
        print("COMPARERESULT>>>>>>>",comparedResults)
        failureResults = {}
        failureResults['em_reqid'] = reqs['em_reqid']
        failureResults['em_custid'] = reqs['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LISTED": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",failureResults)
        return staticfunctions.coretobe_response(failureResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults = {}
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully listed"
        comparedResults['em_reqid'] = reqs['em_reqid']
        comparedResults['em_custid'] = reqs['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResult
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(req, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LISTED","Wrong Credentials")
    
def addRateApi(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("CREAOFFERINGS",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed","CREAOFFERINGS","SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.createRateApi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123458")
        maasslogger(request, str(exCompareUser), "CREAOFFERINGS", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully inserted"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("INSERTED","Wrong Credentials")

# ADD QNTY
def addQntyApi(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("CREAOFFERINGS",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed","QUANTITYLIST","SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.createQntyApi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123458")
        maasslogger(request, str(exCompareUser), "QUANTITYLIST", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully inserted"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("INSERTED","Wrong Credentials")

#========================================================================================
# USER INDEX

def userIndexApi(req):
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("USERINDEX",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(request,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    maasslogger(request,"hashing passes",request['modulename'],"SUCCESS")

    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    # if(valHash == "true"):
    #     maasslogger(request, "Hashing Passed")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
    #     if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.userIndexApi(hashchecksumNdata)
        comparedResult = constantslayer.convinptodict(comparedResults)
        if(len(comparedResults) >= 1):
            comparedResults['result'] = "Success"
    except Exception as exCompareUser:
        maasslogger(request, str(exCompareUser),"USERINDEX", "FAILURE")
        return str(exCompareUser)
    errresp = "Error-Response"
    if(errresp in comparedResult):
        failureResults = {}
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LISTED": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResult)
        return staticfunctions.coretobe_response(comparedResult)

    elif(comparedResult['result'] == "Success"):
        comparedResultz = {}

        comparedResultz['resp_code'] = 800
        comparedResultz['resp_type'] = "SUCCESS"
        comparedResultz['message'] = "Successfully listed"
        comparedResultz['em_reqid'] = request['em_reqid']
        comparedResultz['em_custid'] = request['em_custid']
        comparedResultz['resp_frm_bank'] = ""
        comparedResultz['resp_frm_ewire'] = comparedResult
        comparedResultz['resp_frm_cbs'] = ""
        comparedResultz['resp_frm_ext'] = ['resp_frm_ext']
        comparedResultz['resp_frm_maass'] = ['resp_frm_maass']
        comparedResultz['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResultz['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResultz['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResultz)
        return staticfunctions.coretobe_response(comparedResultz)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LISTED","Wrong Credentials")


# GET KANIKKA BY DIETYID
def kanikkaByDietyidApi(req):
    req = json.dumps(req)
    print("REQUEST",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    maasslogger(req,"hashing passes","LISTPOOJA","SUCCESS")
    try:

        comparedResults = constant_dropdownsui.getKanikkabyDietyid(hashchecksumNdata)
        comparedResult = constantslayer.convinptodict(comparedResults)
        if(len(comparedResults) >= 1):
            comparedResults['result'] = "Success"
    except Exception as exCompareUser:
        maasslogger(request, str(exCompareUser),"GETKANIKKABYDIETYID", "FAILURE")
        return str(exCompareUser)
    errresp = "Error-Response"
    if(errresp in comparedResult):
        failureResults = {}
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LISTED": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResult)
        return staticfunctions.coretobe_response(comparedResult)

    elif(comparedResult['result'] == "Success"):
        comparedResultz = {}

        comparedResultz['resp_code'] = 800
        comparedResultz['resp_type'] = "SUCCESS"
        comparedResultz['message'] = "Successfully listed"
        comparedResultz['em_reqid'] = request['em_reqid']
        comparedResultz['em_custid'] = request['em_custid']
        comparedResultz['resp_frm_bank'] = ""
        comparedResultz['resp_frm_ewire'] = comparedResult
        comparedResultz['resp_frm_cbs'] = ""
        comparedResultz['resp_frm_ext'] = ['resp_frm_ext']
        comparedResultz['resp_frm_maass'] = ['resp_frm_maass']
        comparedResultz['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResultz['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResultz['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResultz)
        return staticfunctions.coretobe_response(comparedResultz)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LISTED","Wrong Credentials")


# GET OFFERING BY TEMPLEID
def offeringByTempleidApi(req):
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LISTED",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(request,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    maasslogger(request,"hashing passes",request['modulename'],"SUCCESS")
    try:
        comparedResults = constant_dropdownsui.getOfferingbyTempleid(hashchecksumNdata)
        comparedResult = constantslayer.convinptodict(comparedResults)
        if(len(comparedResults) >= 1):
            comparedResults['result'] = "Success"
    except Exception as exCompareUser:
        maasslogger(request, str(exCompareUser),"GETDIETYBYTEMPID", "FAILURE")
        return str(exCompareUser)
    errresp = "Error-Response"
    if(errresp in comparedResult):
        failureResults = {}
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LISTED": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        print("ComparedResultFail",comparedResult)
        return staticfunctions.coretobe_response(comparedResult)
    elif(comparedResult['result'] == "Success"):
        comparedResultz = {}
        comparedResultz['resp_code'] = 800
        comparedResultz['resp_type'] = "SUCCESS"
        comparedResultz['message'] = "Successfully listed"
        comparedResultz['em_reqid'] = request['em_reqid']
        comparedResultz['em_custid'] = request['em_custid']
        comparedResultz['resp_frm_bank'] = ""
        comparedResultz['resp_frm_ewire'] = comparedResult
        comparedResultz['resp_frm_cbs'] = ""
        comparedResultz['resp_frm_ext'] = ['resp_frm_ext']
        comparedResultz['resp_frm_maass'] = ['resp_frm_maass']
        comparedResultz['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResultz['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResultz['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResultz)
        return staticfunctions.coretobe_response(comparedResultz)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LISTED","Wrong Credentials")
    
    
# GET OFFERING BY DIETYID
def offeringByDietyidApi(req):
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LISTED",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(request,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    maasslogger(request,"hashing passes",request['modulename'],"SUCCESS")
   
    try:
        comparedResults = constant_dropdownsui.getOfferingbyDietyid(hashchecksumNdata)
        comparedResult = constantslayer.convinptodict(comparedResults)
        if(len(comparedResults) >= 1):
            comparedResults['result'] = "Success"
    except Exception as exCompareUser:
        maasslogger(request, str(exCompareUser),"GETOFFERINGBYDIETYID", "FAILURE")
        return str(exCompareUser)
    errresp = "Error-Response"
    if(errresp in comparedResult):
        failureResults = {}
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LISTED": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        print("ComparedResultFail",comparedResult)
        return staticfunctions.coretobe_response(comparedResult)
    elif(comparedResult['result'] == "Success"):
        comparedResultz = {}
        comparedResultz['resp_code'] = 800
        comparedResultz['resp_type'] = "SUCCESS"
        comparedResultz['message'] = "Successfully listed"
        comparedResultz['em_reqid'] = request['em_reqid']
        comparedResultz['em_custid'] = request['em_custid']
        comparedResultz['resp_frm_bank'] = ""
        comparedResultz['resp_frm_ewire'] = comparedResult
        comparedResultz['resp_frm_cbs'] = ""
        comparedResultz['resp_frm_ext'] = ['resp_frm_ext']
        comparedResultz['resp_frm_maass'] = ['resp_frm_maass']
        comparedResultz['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResultz['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResultz['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResultz)
        return staticfunctions.coretobe_response(comparedResultz)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LISTED","Wrong Credentials")
    
    
# GET PRASADAM BY TEMPLEID
def prasadamByTempleidApi(req):
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LISTED",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(request,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    maasslogger(request,"hashing passes",request['modulename'],"SUCCESS")
    try:
        comparedResults = constant_dropdownsui.getPrasadambyTempleid(hashchecksumNdata)
        comparedResult = constantslayer.convinptodict(comparedResults)
        if(len(comparedResults) >= 1):
            comparedResults['result'] = "Success"
    except Exception as exCompareUser:
        maasslogger(request, str(exCompareUser),"GETDIETYBYTEMPID", "FAILURE")
        return str(exCompareUser)
    errresp = "Error-Response"
    if(errresp in comparedResult):
        failureResults = {}
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LISTED": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        print("ComparedResultFail",comparedResult)
        return staticfunctions.coretobe_response(comparedResult)
    elif(comparedResult['result'] == "Success"):
        comparedResultz = {}
        comparedResultz['resp_code'] = 800
        comparedResultz['resp_type'] = "SUCCESS"
        comparedResultz['message'] = "Successfully listed"
        comparedResultz['em_reqid'] = request['em_reqid']
        comparedResultz['em_custid'] = request['em_custid']
        comparedResultz['resp_frm_bank'] = ""
        comparedResultz['resp_frm_ewire'] = comparedResult
        comparedResultz['resp_frm_cbs'] = ""
        comparedResultz['resp_frm_ext'] = ['resp_frm_ext']
        comparedResultz['resp_frm_maass'] = ['resp_frm_maass']
        comparedResultz['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResultz['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResultz['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResultz)
        return staticfunctions.coretobe_response(comparedResultz)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LISTED","Wrong Credentials")


# GET DIETY BY TEMPLEID
def dietyByTempleidApi(req):
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LISTED",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(request,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    maasslogger(request,"hashing passes",request['modulename'],"SUCCESS")
    try:
        comparedResults = constant_dropdownsui.getDietybyTempleid(hashchecksumNdata)
        comparedResult = constantslayer.convinptodict(comparedResults)
        print(type(comparedResult))
        if(len(comparedResults) >= 1):
            comparedResults['result'] = "Success"
    except Exception as exCompareUser:
        maasslogger(request, str(exCompareUser),"GETDIETYTEMPLEID", "FAILURE")
        return str(exCompareUser)
    errresp = "Error-Response"
    if(errresp in comparedResult):
        failureResults = {}
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LISTED": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        print("ComparedResultFail",comparedResult)
        return staticfunctions.coretobe_response(comparedResult)
    elif(comparedResult['result'] == "Success"):
        comparedResultz = {}
        comparedResultz['resp_code'] = 800
        comparedResultz['resp_type'] = "SUCCESS"
        comparedResultz['message'] = "Successfully listed"
        comparedResultz['em_reqid'] = request['em_reqid']
        comparedResultz['em_custid'] = request['em_custid']
        comparedResultz['resp_frm_bank'] = ""
        comparedResultz['resp_frm_ewire'] = comparedResult
        comparedResultz['resp_frm_cbs'] = ""
        comparedResultz['resp_frm_ext'] = ['resp_frm_ext']
        comparedResultz['resp_frm_maass'] = ['resp_frm_maass']
        comparedResultz['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResultz['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResultz['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResultz)
        return staticfunctions.coretobe_response(comparedResultz)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LISTED","Wrong Credentials")


# ADD CATEGORY
def createCategoryApi(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST CREATE POOJA ",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("CREATECATEGORY",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(req,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        print("EXCEPTION1234")
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    # if(valHash == "true"):
    maasslogger(req, "Hashing Passed","CREATEPOOJA","SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.createCategoryApi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123457")
        maasslogger(request, str(exCompareUser), "CREATECATEGORY", "FAILURE")
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = req['em_reqid']
        failureResults['em_custid'] = req['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    elif(comparedResults['result'] == "Success"):
        comparedResults['resp_code'] = 800
        comparedResults['resp_type'] = "SUCCESS"
        comparedResults['message'] = "Successfully login"
        comparedResults['em_reqid'] = req['em_reqid']
        comparedResults['em_custid'] = req['em_custid']
        comparedResults['resp_frm_bank'] = ""
        comparedResults['resp_frm_ewire'] = comparedResults['respfrmdb']
        comparedResults['resp_frm_cbs'] = ""
        comparedResults['resp_frm_ext'] = ['resp_frm_ext']
        comparedResults['resp_frm_maass'] = ['resp_frm_maass']
        comparedResults['resp_frm_blockc'] = ['resp_frm_blockc']
        comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        comparedResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",comparedResults)
        return staticfunctions.coretobe_response(comparedResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")

# LIST CATEGORY
def listCategoryApi(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LOGIN",str(e))
    #Create hash from data
    try:
        createdhash = constantslayer.createHashfromData(request,"HASH_MO")
        print("HASH@@@",createdhash)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    maasslogger(request,"hashing passes",request['modulename'],"SUCCESS")

    #Decode hash obtained from input and from created hash and compare
    # valHash = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    # if(valHash == "true"):
    #     maasslogger(request, "Hashing Passed")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hash'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
    #     if(checksumcompare == "true"):
    try:
        comparedResults = blconstants.listTempleCategoryApi(hashchecksumNdata)
    except Exception as exCompareUser:
        maasslogger(request, str(exCompareUser))
        return str(exCompareUser)
    print(">>>>>>>",comparedResults)
    errresp = "Error-Response"
    if(errresp in comparedResults):
        failureResults = {}
        failureResults['resp_code'] = 810
        failureResults['resp_type'] = "FAIL"
        failureResults['message'] = "Login Fail"
        failureResults['em_reqid'] = request['em_reqid']
        failureResults['em_custid'] = request['em_custid']
        failureResults['resp_frm_bank'] = ""
        failureResults['resp_frm_ewire'] = {"LOGIN": "Wrong Credentials"}
        failureResults['resp_frm_cbs'] = ""
        failureResults['resp_frm_ext'] = ['resp_frm_ext']
        failureResults['resp_frm_maass'] = ['resp_frm_maass']
        failureResults['resp_frm_blockc'] = ['resp_frm_blockc']
        failureResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        failureResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResultFail",failureResults)
        return staticfunctions.coretobe_response(failureResults)
    elif(comparedResults['result'] == "Success"):
        compareResults = {}
        compareResults['resp_code'] = 800
        compareResults['resp_type'] = "SUCCESS"
        compareResults['message'] = "Successfully login"
        compareResults['em_reqid'] = request['em_reqid']
        compareResults['em_custid'] = request['em_custid']
        compareResults['resp_frm_bank'] = ""
        compareResults['resp_frm_ewire'] = comparedResults
        compareResults['resp_frm_cbs'] = ""
        compareResults['resp_frm_ext'] = ['resp_frm_ext']
        compareResults['resp_frm_maass'] = ['resp_frm_maass']
        compareResults['resp_frm_blockc'] = ['resp_frm_blockc']
        compareResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        compareResults['resp_frm_rulengn'] = ['resp_frm_rulengn']
        # comparedResults['resp_frm_mojaloop'] = ['resp_frm_mojaloop']
        print("ComparedResult",compareResults)
        return staticfunctions.coretobe_response(compareResults)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LOGIN","Wrong Credentials")