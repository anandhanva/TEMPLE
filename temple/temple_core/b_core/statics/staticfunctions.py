import datetime
from re import A
import re
from flask import request,Response
from jsonschema.validators import validate
import requests,json
import logging
import hashlib
from b_core.platformlayers import constantslayer,standardresponses
from b_core.statics import staticfunctions,dbconstants
from b_core.responsemaster import responses
from base64 import b64decode
from base64 import b64encode
from b_core.statics import apiconstants,staticconstants
from Crypto.Cipher import AES
from hashlib import md5
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from b_core.statics.urlconstants import ENDPOINT, IP_DEV




# COMMON RESPONSE CLASS
class CommonReq2be:
    req_type : str
    req_code : datetime
    apiname : str
    em_reqid : str
    partner_reqid : str
    req_timestamp : str
    requestdata : dict
    authtoken : dict
    em_endpoint : str
    em_custid:str
    txntype=str
    hashstr=str
    checksum=str
    def __init__(self, rqstdata):
        print("DATAAA",rqstdata)
        self.resp_code = rqstdata["req_code"]
        self.resp_type = rqstdata["req_type"]
        self.message = rqstdata["message"]
        try:
            if rqstdata["em_reqid"] is None or rqstdata["em_custid"] is None:
                raise Exception("Attribute error,request param null")
            self.req_type=rqstdata["req_type"]
            self.req_code=rqstdata["req_code"]
            self.apiname=rqstdata["apiname"]
            self.em_reqid=rqstdata["em_reqid"]
            self.partner_reqid=rqstdata["partner_reqid"]
            self.requestdata=rqstdata["requestdata"]
            self.authtoken=rqstdata["authtoken"]
            self.em_endpoint=rqstdata["em_endpoint"]
            self.em_custid=rqstdata["em_custid"]
            self.txntype=rqstdata["txntype"]
            self.hashstr=rqstdata['hashstr']
            self.checksum=rqstdata['checksum']
            self.timestamp = str(datetime.datetime.now())
        except ValueError :
            raise Exception("ValueError exception  while assigning timeStamp")
        except TypeError:
            raise Exception("TypeError exception while assigning timeStamp")
        except Exception as e:
            print(e)
            raise Exception("exception while assigning timeStamp")

class CommonResponse:
    em_reqid : str
    timestamp : datetime
    em_custid : str
    resp_code : str
    message : str
    resp_type : str
    resp_frm_yesb : dict

    resp_frm_ewire : dict    
    def __init__(self, respdata):       
        print("DATARESp",respdata)
        print("DATAAA",type(respdata))        
        self.resp_code = respdata["resp_code"]
        self.resp_type = respdata["resp_type"]
        self.message = respdata["message"]        
        try:

            if respdata["em_reqid"] is None or respdata["em_reqid"] is None:
                 raise Exception("Attribute error,request param null")
            else:
                self.em_reqid = respdata["em_reqid"]
                self.em_custid = respdata["em_custid"]
                self.resp_frm_bank = respdata["resp_frm_bank"]
                self.resp_frm_ewire = respdata["resp_frm_ewire"]
                self.resp_frm_cbs = respdata["resp_frm_cbs"]
                self.resp_frm_ext = respdata["resp_frm_ext"]
                self.resp_frm_maass = respdata["resp_frm_maass"]
                self.resp_frm_blockc = respdata["resp_frm_blockc"]
                self.resp_frm_mojaloop = respdata["resp_frm_mojaloop"]
                self.resp_frm_rulengn = respdata["resp_frm_rulengn"]
                self.timestamp = str(datetime.datetime.now())        

        except ValueError :
            raise Exception("ValueError exception  while assigning timeStamp")
        except TypeError:
            raise Exception("TypeError exception while assigning timeStamp")
        except Exception as e:
            print(e)
            raise Exception("exception while assigning timeStamp")

def checkrequest(request):
    data = request
    if data is None or data == {}:
        return {"response" : json.dumps({"Error": "Please provide connection information"}),
                        "status" : 500,
                        "mimetype" : 'application/json'}
    else:
        return {"response" : json.dumps({"Success": "It Works"}),
                        "status" : 200,
                        "mimetype" : 'application/json'}

def coretobe_response(resptype):
    
    if(resptype['resp_type'] == "SUCCESS"):
        resptype['message'] = {"request_status": "SUCCESS", "Status":" Login Successfull"}
        return CommonResponse(resptype).__dict__
    else:
        respdata = {"request_status": "FAIL", "Status":" Login failed with errors"}

        return CommonResponse(respdata).__dict__

def logger_srv(logData):
    
    if(logData['reqtype'] == "SUCCESS"):


        logData['apiname'] =  apiconstants.userLogin
        logData['level'] = "SUCCESS"
        logData['logtype'] = "SUCCESS LOG"
        logData['logdata'] = json.dumps(logData)
        logData['reqtype'] = logData['req_type']
        logData['timestamp'] = str(datetime.datetime.now())
        #logData['collection'] = config.LOG_TABLE
        logData['database'] = staticconstants.DB_NAME
        
        resp = successlogreq(logData)
    else:
       
        if(logData['reqtype'] == "FAIL"):
            resp = faillogreq(logData)
            print("")
        else:
            print("FAIL")
    print("Response: " + str(resp))
    return resp




def successlogreq(reqdata):
    # REQUEST LOGGING
    try:
        
        loggr = dbconstants.MongoAPI(reqdata).write(reqdata)

        
        if(loggr['Status'] == "Successfully Inserted"):
            return 
        else:
            return responses.standardErrorResponseToBE


      
    except ValueError as e:
        return str(e)
    except Exception as e:
        return str(e)
    
    

def faillogreq(reqdata):
    reqst = "" + reqdata + ""
    return reqst

def getUrlsbyModule(modulename):
   return standardresponses.commonValues[modulename]



def validateReq(req):

    # VALIDATE REQUEST
    try:
        valdata = json.loads(req.data.decode('utf-8'))
        

        if valdata['apiname'] == apiconstants.userLogin:
            validatereq = constantslayer.validateJSON(valdata, staticconstants.userSchema)   
        if valdata['apiname']== apiconstants.userLogin:
            validatereq = constantslayer.validateJSON(valdata, staticconstants.userSchema)
        elif valdata['apiname'] == apiconstants.accStatement:
            validatereq = constantslayer.validateJSON(valdata, staticconstants.accStatementSchema)
            
            # responses.standardErrorResponseToUI["sourceoflog"] = "bcore-checklogin"
        elif valdata['apiname'] == apiconstants.addTempleapi:
            validatereq = constantslayer.validateJSON(valdata,staticconstants.addTempleSchema)
        elif valdata['apiname'] == apiconstants.listTempleapi:
            validatereq = constantslayer.validateJSON(valdata,staticconstants.listTempleSchema)
        elif valdata['apiname'] == apiconstants.createTempleAdminapi:
            validatereq = constantslayer.validateJSON(valdata,staticconstants.addTempleAdminSchema)
        elif valdata['apiname'] == apiconstants.listTempleAdminapi:
            validatereq = constantslayer.validateJSON(valdata,staticconstants.listTempleAdminSchema)
        elif valdata['apiname'] == apiconstants.createAccountapi:
            validatereq = constantslayer.validateJSON(valdata,staticconstants.createAccountSchema)
        elif valdata['apiname'] == apiconstants.listAccountapi:
            validatereq = constantslayer.validateJSON(valdata,staticconstants.listAccountSchema)


                
        if(validatereq['respType'] == 'success'):
            valResp = {}
            valResp['response'] = responses.upGetResponse()
            valResp['status'] = 200
            
        else:
            responses.standardErrorResponseToBE["sourceoflog"] = "fail"
            valResp = responses.standardErrorResponseToBE()

        
        logging.info(" :::VALIDATION SUCCESSFULL::: ",valResp)

        return valResp

    
    except ValueError as e:
        return str(e)
    except Exception as e:
        return str(e)

class AESCipher:
    def __init__(self, key):
        self.key = md5(key.encode('utf8')).digest()

    def encrypt(self, data):
        iv = get_random_bytes(AES.block_size)
        print(iv)
        self.cipher = AES.new(self.key, AES.MODE_CBC,iv)
        return b64encode(self.cipher.encrypt(pad(data.encode('utf-8'),AES.block_size))).decode('utf-8')

    def decrypt(self, data):
        raw = b64decode(data)
        self.cipher = AES.new(self.key, AES.MODE_CBC, raw[:AES.block_size])
        return unpad(self.cipher.decrypt(raw[AES.block_size:]), AES.block_size).decode('utf-8')    




def performRequest(request):


    try:

        # print("Request>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",request)

        server = request['parameters']['server']
        # print("server",server)

        headerz = request['parameters']['headerz']
        # print("headerz",headerz)

        endpoint = request['parameters']['endpoint']
        # print("endpoint",endpoint)

        reqdata = request['data']
        # print("reqdata",reqdata)

        reqType = request['parameters']['reqtype']
        # print("reqType",reqType)

        methodType = request['parameters']['methodtype']
        # print("methodType",methodType)


        
        
        if(reqType == "SSL"):
            url = "https://" + server + endpoint

        else:
            url = "http://" + server + endpoint

        responseofreq = ""

        if(methodType == "POST"):
            
            print("DATA",str(reqdata))
            print("URL",str(url))
            print("HEADER",str(headerz))
            payload = json.dumps(reqdata)

            print("PL = ",payload)

            try:
                r = requests.post(url, data = payload, headers=headerz)
            
                if(r.status_code == 200):
                    return r.text
                else:
                    print(r.text)
                    return {"Error":"Api Failed"}
                responseofreq = r
            except Exception as e:
                return  str(e)
        else:
            if(methodType == "GET"):
                r = requests.get(url, data=reqdata, headers=headerz)
                if(r.status_code == 200):
                    return responses.upGetResponse
                else:
                    return responses.standardErrorResponseToBE
                responseofreq = r
        return responseofreq

    except Exception as e:
        print("EXCEPTION",str(e))
        return str(e)

    except ValueError as e:
        print("EXCEPTION VALUE ERROR",str(e))
        return str(e)

def checkSum(value):
        # if  type(value)!= "Dict":
        #     value = json.dumps(value)
    hashvalue = hashlib.md5(str(value).encode('utf-8')).hexdigest()
    # hashValue = hashlib.sha512(value.encode('utf-8')).hexdigest().lower()
    return hashvalue

def validateHash(requesthash,createdhash):
    # requesthash = json.loads(requesthash['hashstr'])
    decodehash2 = AESCipher(staticconstants.ENCRYPTION_KEY).decrypt(requesthash['hashstr'])

    #Decode hash from created hash
    checksum1 = request['checksum']

    checksum2 = checkSum(request['hashstr'])
    decodehash1 = AESCipher(staticconstants.ENCRYPTION_KEY).decrypt(createdhash['hashstr'])

    reqChecksum = checkSum(createdhash['hashstr'])

    #Compare Checksum and HASHES
    if decodehash1 == decodehash2:

        return "true"
    else:
        return "false"


def validatechecksum(requestchecksum,createdchecksum):
    checksum1 = checkSum(requestchecksum)
    checksum2 = checkSum(createdchecksum)
    if checksum1 == checksum2:
        return "true"
    else:
        return "false"






