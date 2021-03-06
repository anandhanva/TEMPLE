import json
from flask.globals import request
from b_core.platformlayers import constantslayer,constant_dropdownsui,qrmanage
from b_core.platformlayers import constantslayer,constant_dropdownsui
from b_core.responsemaster import responses
from b_core.maass.maasslogger import maasslogger
from b_core.statics import staticfunctions,blconstants
import traceback, sys


# USER LOGIN
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


# USER OTPVERIFICATION
def processOtpVerificationt(req):
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

        comparedResults = blconstants. processOtpVerificationtapi(hashchecksumNdata)
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


