import datetime
from re import A
from flask import request,Response
from jsonschema.validators import validate
import requests,json
import logging

from b_end.platformlayers import constantslayer
from b_end.statics import staticfunctions
from b_end.responsemaster import responses
from b_end.statics import apiconstants,staticconstants
from b_end.statics.urlconstants import ENDPOINT, IP_DEV
# COMMON RESPONSE CLASS
class CommonReq2be:
    req_type : str
    req_code : datetime
    api_name : str
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
            self.api_name=rqstdata["api_name"]
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
def betoui_response(resptype):
    if(resptype['resp_type'] == "SUCCESS"):
        resptype['Response'] = {"request_status": "SUCCESS", "Status":" Login Successfully"}
    return CommonResponse(resptype).__dict__
   

def validateReq(req):
    # VALIDATE REQUEST
    try:
        valdata = json.loads(json.dumps(req))
        # valdata=json.dumps(valdata)
        print("val Data ", valdata)
        SchemaConst=valdata['api_name']+"Schema"
        print(">>>>>>>>>>>>>>>>>>>>>>>>",SchemaConst)

        Schema=staticconstants.schemas[SchemaConst]
        print(">>>>>>>>>>>>>>>>>>>>>>>>",Schema)
        validatereq=constantslayer.validateJSON(validate,Schema)
        # responses.standardErrorResponseToUI["sourceoflog"] = "bcore-checklogin"
        if(validatereq['respType'] == 'success'):
            valResp = {}
            valResp['response'] = responses.upGetResponse()
            valResp['status'] = 200
        else:
            responses.standardErrorResponseToUI["sourceoflog"] = "fail"
            valResp = responses.standardErrorResponseToUI()
        logging.info(" :::VALIDATION SUCCESSFULL::: ",valResp)
        return valResp        
    except ValueError as e:
        return str(e)
    except Exception as e:
        return str(e)


def performRequest(request, modulename):
    

    server = request['parameters'][modulename]['server']
    headerz = request['parameters'][modulename]['headerz']
    endpoint = request['parameters'][modulename]['endpoint']
    reqdata = request['data']
    reqType = request['parameters'][modulename]['reqtype']
    methodType = request['parameters'][modulename]['methodtype']
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
                return responses.standardErrorResponseToUI
            responseofreq = r
            
    return responseofreq
