import json
from flask.globals import request
from b_core.platformlayers import constantslayer,constant_dropdownsui,qrmanage
from b_core.platformlayers import constantslayer,constant_dropdownsui
from b_core.responsemaster import responses
from b_core.maass.maasslogger import maasslogger
from b_core.statics import staticfunctions,blconstants
import traceback, sys



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

def addTemple(requset):
    req= request.get_json()

    print("REQUEST CREATE TEMPLE ",req)
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
    maasslogger(req, "Hashing Passed","ADD_TEMPLE","SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.addTempleApi(hashchecksumNdata)
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
    
# LIST TEMPLE
def listTempleApi(req):
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

        comparedResults = blconstants.listTempleApi(hashchecksumNdata)
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
    
    
# CREATE TEMPLE ADMIN
def createTempleAdmin(req):
    req= request.get_json()

    print("REQUEST CREATE TEMPLE ",req)
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
    maasslogger(req, "Hashing Passed","CREATETEMPLE_ADMIN","SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.createTempleAdminApi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123457")
        maasslogger(request, str(exCompareUser), "CREATETEMPLE_ADMIN", "FAILURE")
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

# # ADD ACCOUNT
def createAccount(req):
    req= request.get_json()

    print("REQUEST CREATE TEMPLE ",req)
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
    maasslogger(req, "Hashing Passed","CREATETEMPLE_ADMIN","SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.createAccountApi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123457")
        maasslogger(request, str(exCompareUser), "CREATE_ACCOUNT", "FAILURE")
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
    req= request.get_json()

    print("REQUEST CREATE TEMPLE ",req)
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
    maasslogger(req, "Hashing Passed","CREATETEMPLE_ADMIN","SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.createTempleAdminApi(hashchecksumNdata)
        comparedResults = constantslayer.convinptodict(comparedResults)
        # if(isinstance(comparedResults) == str):compared
        #     comparedResults = json.loads(comparedResults)
        # elif isinstance(comparedResults) != dict:
        #     comparedResults = json.loads(comparedResults)
        # print(">>>>>>>",comparedResults)
        # print(">>>>>>>",type(comparedResults))
    except Exception as exCompareUser:
        print("EXCEPTION123457")
        maasslogger(request, str(exCompareUser), "ADD_FINADMIN", "FAILURE")
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


# =======================================================================================
#CREATE QR
def createQR(req):
    request = req.get_json()
    try:
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
    except Exception as e:
        return responses.standardErrorResponseToBE("CREATEQR",str(e))
    try:
        createdhash = constantslayer.createHashfromData(request,"HASH_MO")
    except Exception as e:
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    maasslogger(request,"hashing passes",request['modulename'],"SUCCESS")
    try:
        comparedResults = qrmanage.qrhandler(hashchecksumNdata)
        comparedResult = constantslayer.convinptodict(comparedResults)
        if(len(comparedResults) >= 1):
            comparedResults['result'] = "Success"
    except Exception as exCompareUser:
        maasslogger(request, str(exCompareUser),"QRGENERATION", "FAILURE")
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print(fname, lineno)
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
        print("ComparedResultFail",failureResults)
        return staticfunctions.coretobe_response(failureResults)
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
        print("ComparedResult",comparedResultz)
        return staticfunctions.coretobe_response(comparedResultz)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LISTED","Wrong Credentials")


#READ QR
def rdQRdata(req):
    request = req.get_json()
    try:
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
    except Exception as e:
        return responses.standardErrorResponseToBE("CREATEQR",str(e))
    try:
        createdhash = constantslayer.createHashfromData(request,"HASH_MO")
    except Exception as e:
        return responses.standardErrorResponseToBE("CREATELOGINHASH",str(e))
    maasslogger(request,"hashing passes",request['modulename'],"SUCCESS")
    try:
        comparedResults = qrmanage.readQRdata(hashchecksumNdata)
        comparedResult = constantslayer.convinptodict(comparedResults)
        if(len(comparedResults) >= 1):
            comparedResults['result'] = "Success"
    except Exception as exCompareUser:
        maasslogger(request, str(exCompareUser),"QRGENERATION", "FAILURE")
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
        print("ComparedResult",comparedResultz)
        return staticfunctions.coretobe_response(comparedResultz)
    else:
        maasslogger(request, "Wrong Credentials")
        return responses.standardErrorResponseToBE("LISTED","Wrong Credentials")

#====================================================================================================      
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


# DROPDOWN CATEGORY
def dropdownCategoryApi(req):
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

        comparedResults = blconstants.drpdwnTempCategoryApi(hashchecksumNdata)
        comparedResult = constantslayer.convinptodict(comparedResults)
        if(len(comparedResults) >= 1):
            comparedResults['result'] = "Success"
    except Exception as exCompareUser:
        maasslogger(request, str(exCompareUser),"DROPDOWNCATEGORY", "FAILURE")
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
    
# ADD FESTIVAL
def createFestivalApi(req):
    #Parse Request and  extract hash, checksum and data
    # request = req.get_json()
    print("REQUEST CREATE FESTIVAL ",req)
    try:
        print("REQQUEST",req)
        hashchecksumNdata = constantslayer.parseRequestHCRD(req)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        print("EXCEPTION123")
        # maasslogger(req, "Failed",req['modulename'],"SUCCESS")
        return responses.standardErrorResponseToBE("CREATEFESTIVAL",str(e))
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
    maasslogger(req, "Hashing Passed","CREATEFESTIVAL","SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.createFestivalApi(hashchecksumNdata)
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


# LIST FESTIVAL
def listFestivalApi(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LISTFESTIVAL",str(e))
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
        comparedResults = blconstants.listFestivalApi(hashchecksumNdata)
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



def createStatementApi(req):
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

        comparedResults = blconstants.createStatementApi(hashchecksumNdata)
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

# LIST ACSTATEMENT
def listStatementApi(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LISTSTATEMENT",str(e))
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
        comparedResults = blconstants.listStatementsApi(hashchecksumNdata)
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


# DROPDOWN FINACE ACTIVITY
def dropdownActivityApi(req):
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

        comparedResults = blconstants.drpdwnFinActivityApi(hashchecksumNdata)
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


# GET OFFERING BY DIETYID
def dataByAcnumberApi(req):
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
        comparedResults = constant_dropdownsui.getDatabyAcnumid(hashchecksumNdata)
        comparedResult = constantslayer.convinptodict(comparedResults)
        if(len(comparedResults) >= 1):
            comparedResults['result'] = "Success"
    except Exception as exCompareUser:
        maasslogger(request, str(exCompareUser),"GETDATABYACNUMBER", "FAILURE")
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

def createDevasamApi(request):
    req= request.get_json()

    print("REQUEST CREATE TEMPLE ",req)
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
    maasslogger(req, "Hashing Passed","ADD_TEMPLE","SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.createDevasomsApi(hashchecksumNdata)
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

# LIST DEVASOM
def listDevasomApi(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LISTSTATEMENT",str(e))
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
        comparedResults = blconstants.listDevasomsApi(hashchecksumNdata)
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

#Create Devasom Admin

def createDevasomAdminApi(request):
    req= request.get_json()

    print("REQUEST CREATE TEMPLE ",req)
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
    maasslogger(req, "Hashing Passed","ADD_TEMPLE","SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.createDevasomAdminApi(hashchecksumNdata)
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


# LIST DEVASOM
def listDevasomAdminApi(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LISTSTATEMENT",str(e))
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
        comparedResults = blconstants.listDevasomAdminApi(hashchecksumNdata)
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

#Create Devasom Admin

def createPoolApi(request):
    req= request.get_json()

    print("REQUEST CREATE TEMPLE ",req)
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
    maasslogger(req, "Hashing Passed","ADD_TEMPLE","SUCCESS")
    #     # checking checksum
    #     createdchecksum = staticfunctions.validateHash(hashchecksumNdata['hashstr'],createdhash)
    #     checksumcompare = staticfunctions.validatechecksum(hashchecksumNdata['checksum'], createdchecksum)
        # if(checksumcompare == "true"):
    try:

        comparedResults = blconstants.createPoolApi(hashchecksumNdata)
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


# LIST POOL
def listPoolsApi(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LISTSTATEMENT",str(e))
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
        comparedResults = blconstants.listPoolApi(hashchecksumNdata)
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




# Create fund Tranfer
def createFundsTransfer(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LISTSTATEMENT",str(e))
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
        comparedResults = blconstants.createFundTransferApi(hashchecksumNdata)
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


# List Fund Transfer
def listFundsTransfer(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LISTSTATEMENT",str(e))
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
        comparedResults = blconstants.listFundTransferApi(hashchecksumNdata)
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

# Create Bank Details
def createBank(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LISTSTATEMENT",str(e))
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
        comparedResults = blconstants.createBankApi(hashchecksumNdata)
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

# Create Bank Details
def listBankDetails(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LISTSTATEMENT",str(e))
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
        comparedResults = blconstants.listBankDetailsApi(hashchecksumNdata)
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

# Create Bank Admin
def createBankAdmin(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LISTSTATEMENT",str(e))
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
        comparedResults = blconstants.createBankAdminApi(hashchecksumNdata)
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


#list Bank Admin
def listBankAdmin(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LISTSTATEMENT",str(e))
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
        comparedResults = blconstants.listBankAdminApi(hashchecksumNdata)
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

# CREATE CARD ALLOCATION
def createCardAllocationApi(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LISTSTATEMENT",str(e))
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
        comparedResults = blconstants.createCardApi(hashchecksumNdata)
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

#LIST CARD ALLOCATION
def listCardAllocationApi(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LISTSTATEMENT",str(e))
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
        comparedResults = blconstants.listCardApplicationsApi(hashchecksumNdata)
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

# CREATE TRANSACTION DEVASWOM
def createTransactionDevaswomApi(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LISTSTATEMENT",str(e))
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
        comparedResults = blconstants.createTransactionDevaswomsApi(hashchecksumNdata)
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

#LIST TRANSACTION DEVASWOM
def listTransactionDevaswomApi(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LISTSTATEMENT",str(e))
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
        comparedResults = blconstants.listTransactionsDevaswomsApi(hashchecksumNdata)
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


#DROP DOWN BANK
def dropDownBankApi(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LISTSTATEMENT",str(e))
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
        comparedResults = blconstants.drpdwnBankApi(hashchecksumNdata)
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


#DROP DOWN TEMPLE
def dropDownTempleApi(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LISTSTATEMENT",str(e))
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
        comparedResults = blconstants.drpdwnTempleApi(hashchecksumNdata)
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

#DROP DOWN IFSC
def dropDownIFSCApi(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LISTSTATEMENT",str(e))
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
        comparedResults = blconstants.drpdwnIFSCApi(hashchecksumNdata)
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

#CREATE RECONCILIATION DETAILS
def createReconciliationApi(req):
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

        comparedResults = blconstants.createReconciliationApi(hashchecksumNdata)
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

# LIST RECONCILIATION DETAILS
def listReconciliationApi(req):
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

        comparedResults = blconstants.listReconciliationApi(hashchecksumNdata)
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

#CREATE REQUEST MONEY
def createReqMoneyApi(req):
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

        comparedResults = blconstants.createRequestMoneyApi(hashchecksumNdata)
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

#DROPDOWN DEVASWOM 
def dropdowndevaswomApi(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LISTSTATEMENT",str(e))
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
        comparedResults = blconstants.dropdownDevaswomApi(hashchecksumNdata)
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

# Create Lords 
def createlordsApi(req):
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

        comparedResults = blconstants.createLordsApi(hashchecksumNdata)
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

# LIST LORDS 
def listlordsApi(req):
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

        comparedResults = blconstants.listLordsApi(hashchecksumNdata)
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

# CREATE FORGOT PIN
def createforgotpinApi(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LISTSTATEMENT",str(e))
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
        comparedResults = blconstants.createForgotPinApi(hashchecksumNdata)
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

# GET TRANSACTION DEVASWOM
def gettransactiondevaswomApi(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LISTSTATEMENT",str(e))
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
        comparedResults = blconstants.getTransactionDevaswomApi(hashchecksumNdata)
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

# GET TRANSACTION BANK
def gettransactionbankApi(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LISTSTATEMENT",str(e))
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
        comparedResults = blconstants.getTransactionBankApi(hashchecksumNdata)
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


# LIST TRANSACTION BANK
def listtransactionbankApi(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LISTSTATEMENT",str(e))
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
        comparedResults = blconstants.listTransactionBankApi(hashchecksumNdata)
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

# GET TRANSACTION TEMPLE
def gettransactiontempleApi(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LISTSTATEMENT",str(e))
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
        comparedResults = blconstants.getTransactionTempleApi(hashchecksumNdata)
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

# LIST TRANSACTION BANK
def listtransactiontempleApi(req):
    #Parse Request and  extract hash, checksum and data
    request = req.get_json()
    print("REQUEST",request)
    try:
        print("REQQUEST",request)
        hashchecksumNdata = constantslayer.parseRequestHCRD(request)
        print("HASHHHH",hashchecksumNdata)
    except Exception as e:
        # maasslogger(req, str(e))
        return responses.standardErrorResponseToBE("LISTSTATEMENT",str(e))
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
        comparedResults = blconstants.listTransactionTempleApi(hashchecksumNdata)
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

# Create BLOCK TEMPLE
def createblocktempleApi(req):
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

        comparedResults = blconstants.createBlockTempleApi(hashchecksumNdata)
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
        return responses.standardErrorResponseToBE("LISTED","FAILURE")


# LIST BLOCK TEMPLE
def listblocktempleApi(req):
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

        comparedResults = blconstants.listBlockTempleApi(hashchecksumNdata)
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
        return responses.standardErrorResponseToBE("LISTED","FAILURE")

# CREATE BLOCK DEVASWOM
def createblockdevaswomApi(req):
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

        comparedResults = blconstants.createBlockDevaswomApi(hashchecksumNdata)
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
        return responses.standardErrorResponseToBE("LISTED","FAILURE")

# LIST BLOCK DEVASWOM
def listblockdevaswomApi(req):
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

        comparedResults = blconstants.listBlockDevaswomApi(hashchecksumNdata)
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
        return responses.standardErrorResponseToBE("LISTED","FAILURE")

# CREATE BLOCK CUSTOMER
def createblockcustomerApi(req):
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

        comparedResults = blconstants.createBlockCustomerApi(hashchecksumNdata)
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
        return responses.standardErrorResponseToBE("LISTED","FAILURE")


# LIST BLOCK CUSTOMER
def listblockcustomerApi(req):
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

        comparedResults = blconstants.listBlockCustomerApi(hashchecksumNdata)
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
        return responses.standardErrorResponseToBE("LISTED","FAILURE")

# CREATE BLOCK CARD
def createblockcardApi(req):
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

        comparedResults = blconstants.createBlockCardApi(hashchecksumNdata)
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
        return responses.standardErrorResponseToBE("LISTED","FAILURE")

# LIST BLOCK CARD
def listblockcardApi(req):
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

        comparedResults = blconstants.listBlockCardApi(hashchecksumNdata)
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
        return responses.standardErrorResponseToBE("LISTED","FAILURE")

# CREATE BLOCK BANK
def createblockbankApi(req):
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

        comparedResults = blconstants.createBlockBankApi(hashchecksumNdata)
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
        return responses.standardErrorResponseToBE("LISTED","FAILURE")

# LIST BLOCK BANK
def listblockbankApi(req):
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

        comparedResults = blconstants.listBlockBankApi(hashchecksumNdata)
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
        return responses.standardErrorResponseToBE("LISTED","FAILURE")

# LIST BLOCK BANK
def superlisttransdevaApi(req):
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

        comparedResults = blconstants.superListTransDevaApi(hashchecksumNdata)
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
        return responses.standardErrorResponseToBE("LISTED","FAILURE")


# LIST BLOCK BANK
def listacctstatmeentapi(req):
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

        comparedResults = blconstants.listAcctStatmeentApi(hashchecksumNdata)
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
        return responses.standardErrorResponseToBE("LISTED","FAILURE")

#DROPDOWN ACTIVITIES TYPE
def dropdownactivitytypeApi(req):
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

        comparedResults = blconstants.dropdownActivityTypeApi(hashchecksumNdata)
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
        return responses.standardErrorResponseToBE("LISTED","FAILURE")

#DROPDOWN DEVASWOM
def superdropdowndevaswomapi(req):
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

        comparedResults = blconstants.superDropDownDevaswomApi(hashchecksumNdata)
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
        return responses.standardErrorResponseToBE("LISTED","FAILURE")

#CREATE POOJA
def createsuperpoojaapi(req):
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

        comparedResults = blconstants.createSuperPoojaApi(hashchecksumNdata)
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
        return responses.standardErrorResponseToBE("LISTED","FAILURE")

#LIST POOJA
def listsuperpoojaapi(req):
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

        comparedResults = blconstants.listSuperPoojaApi(hashchecksumNdata)
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
        return responses.standardErrorResponseToBE("LISTED","FAILURE")

#CREATE DEVASWOM
def createsuperdevaswomapi(req):
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

        comparedResults = blconstants.createSuperDevaswomApi(hashchecksumNdata)
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
        return responses.standardErrorResponseToBE("LISTED","FAILURE")