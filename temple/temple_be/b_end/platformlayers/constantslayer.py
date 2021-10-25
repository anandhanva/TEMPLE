from b_end.maass import maasslogger
import json,jsonschema
import re
from b_end.statics import staticfunctions
from b_end.platformlayers import standardresponses
from b_end.statics import urlconstants
from jsonschema import validate
import traceback, sys
def parseRequestHCRD(request):
    
    try:
        #convert Request to dictionary
        reqdata = convinptodict(request)
    except Exception as e:
        #Log exception
        maasslogger(request,str(e))
        return str(e)
    #parse by predefined requestdata
    hashfrmInput = reqdata['hashstr']
    checksumfrmInput = reqdata['checksum']
    datafrmInput = reqdata['requestdata']
    #prepare a return dictionary
    retaftrParsed = {}
    retaftrParsed['hashstr'] = hashfrmInput
    retaftrParsed['checksum'] = checksumfrmInput
    retaftrParsed['datafrm'] = datafrmInput
    return retaftrParsed
def convinptodict(input):
    #check input data type
    if(isinstance(input, dict)):
        #it is already dict
        return input
    elif(isinstance(input, str)):
        print("here")
        #convert string to dictionary
        v = json.loads(input)
        print("reaaaaa",v)
        print("reaaaaa",type(v))

        if type(v) is dict:
            print("VVVVV",v)
            return v
        else:

            return json.loads(json.dumps(input)) # json
    elif(isinstance(input, int)):
        #convert iny to dictionary
        return json.loads(input)


def checklogin(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    try:
        modulename = 'LOGIN'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['requestdata'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
                    "em_custid":request['em_custid'],"txntype":request["txntype"],"hashstr":request['hashstr'],"checksum":request['checksum']}
        obj = standardresponses.commonValues
        otherdata = {}
        # 
        otherdata['parameters'] = obj
        otherdata['data'] = datadict
        # print('otherdata', otherdata)
        TempleBeResp = staticfunctions.performRequest(otherdata,modulename)
        # print("Build Resp Type", type(TempleBeResp))
        # print("Temple Resp ", TempleBeResp)
        TempleBeResp =convinptodict(TempleBeResp)
        print("ivide ethi 1",TempleBeResp)
        erresp="ERROR Response"
        if(erresp in TempleBeResp):
            failureRespToui={}
            failureRespToui['resp_type']="FAIL"
            failureRespToui['resp_code']=800
            failureRespToui['message']="couldn't connect to servers"
            failureRespToui['em_reqid']=request["em_reqid"]
            failureRespToui['timestamp']=request["timestamp"]
            failureRespToui['em_custid']=request["em_custid"]
            failureRespToui['resp_frm_yesb']=""
            failureRespToui['resp_frm_ewire']=""
            return staticfunctions.betoui_response(failureRespToui)
        else:
            return TempleBeResp 
    except ValueError as e:
        print("EXCEPTION1",str(e))
        
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

   
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#USER API

#home page

def index(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'INDEX'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['requestdata'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
                    "em_custid":request['em_custid'],"txntype":request["txntype"],"hashstr":request['hashstr'],"checksum":request['checksum']}
        obj = standardresponses.commonValues
        otherdata = {}
        # 
        otherdata['parameters'] = obj
        otherdata['data'] = datadict
        print('otherdata', otherdata)
        TempleBeResp = staticfunctions.performRequest(otherdata,modulename)
        print("Temple Resp Type", type(TempleBeResp))
        # print('otherdata', otherdata)
       
        erresp="ERROR Response"
        if(erresp in TempleBeResp):
            failureRespToui={}
            failureRespToui['resp_type']="FAIL"
            failureRespToui['resp_code']=800
            failureRespToui['message']="couldn't connect to servers"
            failureRespToui['em_reqid']=request["em_reqid"]
            failureRespToui['timestamp']=request["timestamp"]
            failureRespToui['em_custid']=request["em_custid"]
            failureRespToui['resp_frm_yesb']=""
            failureRespToui['resp_frm_ewire']=""
            return staticfunctions.betoui_response(failureRespToui)
        else:
            if("HTTPConnectionPool" in TempleBeResp):
                return {"resp":"ERROR"}
            else:
                return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return {"resp":"ERROR"}
    except Exception as e:
        print("EXCEPTION2",str(e))
        return {"resp":"ERROR"}

#user kanikka

def userkanikka(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'USERKANIKKA'
        datadict = {"req_type":request['type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['requestdata'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
                    "em_custid":request['em_custid'],"txntype":request["txntype"],"hashstr":request['hashstr'],"checksum":request['checksum']}
        obj = standardresponses.commonValues
        otherdata = {}
        # 
        otherdata['parameters'] = obj
        otherdata['data'] = datadict
        print('otherdata', otherdata)
        TempleBeResp = staticfunctions.performRequest(otherdata,modulename)
        print("Temple Resp Type", type(TempleBeResp))
       
        print("Temple Resp ", TempleBeResp)
        erresp="ERROR Response"
        if(erresp in TempleBeResp):
            failureRespToui={}
            failureRespToui['resp_type']="FAIL"
            failureRespToui['resp_code']=800
            failureRespToui['message']="couldn't connect to servers"
            failureRespToui['em_reqid']=request["em_reqid"]
            failureRespToui['timestamp']=request["timestamp"]
            failureRespToui['em_custid']=request["em_custid"]
            failureRespToui['resp_frm_yesb']=""
            failureRespToui['resp_frm_ewire']=""
            return staticfunctions.betoui_response(failureRespToui)
        else:
            if("HTTPConnectionPool" in TempleBeResp):
                return {"resp":"ERROR"}
            else:
                return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return {"resp":"ERROR"}
    except Exception as e:
        print("EXCEPTION2",str(e))
        return {"resp":"ERROR"}

#get star drop

def getstar(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'GETSTARDROP'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['requestdata'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
                    "em_custid":request['em_custid'],"txntype":request["txntype"],"hashstr":request['hashstr'],"checksum":request['checksum']}
        obj = standardresponses.commonValues
        otherdata = {}
        # 
        otherdata['parameters'] = obj
        otherdata['data'] = datadict
        print('otherdata', otherdata)
        TempleBeResp = staticfunctions.performRequest(otherdata,modulename)
        print("Temple Resp Type", type(TempleBeResp))
        print("Temple Resp ", TempleBeResp)
        # print('otherdata', otherdata)
        
        erresp="ERROR Response"
        if(erresp in TempleBeResp):
            failureRespToui={}
            failureRespToui['resp_type']="FAIL"
            failureRespToui['resp_code']=800
            failureRespToui['message']="couldn't connect to servers"
            failureRespToui['em_reqid']=request["em_reqid"]
            failureRespToui['timestamp']=request["timestamp"]
            failureRespToui['em_custid']=request["em_custid"]
            failureRespToui['resp_frm_yesb']=""
            failureRespToui['resp_frm_ewire']=""
            return staticfunctions.betoui_response(failureRespToui)
        else:
            if("HTTPConnectionPool" in TempleBeResp):
                return {"resp":"ERROR"}
            else:
                return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return {"resp":"ERROR"}
    except Exception as e:
        print("EXCEPTION2",str(e))
        return {"resp":"ERROR"}

#get_prasadam_bill_list

def getprsdmbilllst(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'GETPRASADAMBILL'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['requestdata'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
                    "em_custid":request['em_custid'],"txntype":request["txntype"],"hashstr":request['hashstr'],"checksum":request['checksum']}
        obj = standardresponses.commonValues
        otherdata = {}
        # 
        otherdata['parameters'] = obj
        otherdata['data'] = datadict
        print('otherdata', otherdata)
        TempleBeResp = staticfunctions.performRequest(otherdata,modulename)
        
        print("Temple Resp ", TempleBeResp)
        erresp="ERROR Response"
        if(erresp in TempleBeResp):
            failureRespToui={}
            failureRespToui['resp_type']="FAIL"
            failureRespToui['resp_code']=800
            failureRespToui['message']="couldn't connect to servers"
            failureRespToui['em_reqid']=request["em_reqid"]
            failureRespToui['timestamp']=request["timestamp"]
            failureRespToui['em_custid']=request["em_custid"]
            failureRespToui['resp_frm_yesb']=""
            failureRespToui['resp_frm_ewire']=""
            return staticfunctions.betoui_response(failureRespToui)
        else:
            if("HTTPConnectionPool" in TempleBeResp):
                return {"resp":"ERROR"}
            else:
                return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return {"resp":"ERROR"}
    except Exception as e:
        print("EXCEPTION2",str(e))
        return {"resp":"ERROR"}

#user_list_kanikka


def userlistkanikka(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'USERLISTKANIKKA'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['requestdata'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
                    "em_custid":request['em_custid'],"txntype":request["txntype"],"hashstr":request['hashstr'],"checksum":request['checksum']}
        obj = standardresponses.commonValues
        otherdata = {}
        # 
        otherdata['parameters'] = obj
        otherdata['data'] = datadict
        print('otherdata', otherdata)
        TempleBeResp = staticfunctions.performRequest(otherdata,modulename)
        print("Temple Resp Type", type(TempleBeResp))
       
       
        print("Temple Resp ", TempleBeResp)
        erresp="ERROR Response"
        if(erresp in TempleBeResp):
            failureRespToui={}
            failureRespToui['resp_type']="FAIL"
            failureRespToui['resp_code']=800
            failureRespToui['message']="couldn't connect to servers"
            failureRespToui['em_reqid']=request["em_reqid"]
            failureRespToui['timestamp']=request["timestamp"]
            failureRespToui['em_custid']=request["em_custid"]
            failureRespToui['resp_frm_yesb']=""
            failureRespToui['resp_frm_ewire']=""
            return staticfunctions.betoui_response(failureRespToui)
        else:
            if("HTTPConnectionPool" in TempleBeResp):
                return {"resp":"ERROR"}
            else:
                return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return {"resp":"ERROR"}
    except Exception as e:
        print("EXCEPTION2",str(e))
        return {"resp":"ERROR"}

def userhistory(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'HISTORY'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['requestdata'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
                    "em_custid":request['em_custid'],"txntype":request["txntype"],"hashstr":request['hashstr'],"checksum":request['checksum']}
        obj = standardresponses.commonValues
        otherdata = {}
        # 
        otherdata['parameters'] = obj
        otherdata['data'] = datadict
        print('otherdata', otherdata)
        TempleBeResp = staticfunctions.performRequest(otherdata,modulename)
       
       
        # print("Build Resp Type", type(TempleBeResp))
        print("Temple Resp ", TempleBeResp)
        erresp="ERROR Response"
        if(erresp in TempleBeResp):
            failureRespToui={}
            failureRespToui['resp_type']="FAIL"
            failureRespToui['resp_code']=800
            failureRespToui['message']="couldn't connect to servers"
            failureRespToui['em_reqid']=request["em_reqid"]
            failureRespToui['timestamp']=request["timestamp"]
            failureRespToui['em_custid']=request["em_custid"]
            failureRespToui['resp_frm_yesb']=""
            failureRespToui['resp_frm_ewire']=""
            return staticfunctions.betoui_response(failureRespToui)
        else:
            if("HTTPConnectionPool" in TempleBeResp):
                return {"resp":"ERROR"}
            else:
                return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return {"resp":"ERROR"}
    except Exception as e:
        print("EXCEPTION2",str(e))
        return {"resp":"ERROR"}


def poojabill(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'POOJABILL'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['requestdata'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
                    "em_custid":request['em_custid'],"txntype":request["txntype"],"hashstr":request['hashstr'],"checksum":request['checksum']}
        obj = standardresponses.commonValues
        otherdata = {}
        # 
        otherdata['parameters'] = obj
        otherdata['data'] = datadict
        print('otherdata', otherdata)
        TempleBeResp = staticfunctions.performRequest(otherdata,modulename)
        print("Temple Resp Type", type(TempleBeResp))
        
        
        print("Temple Resp ", TempleBeResp)
        erresp="ERROR Response"
        if(erresp in TempleBeResp):
            failureRespToui={}
            failureRespToui['resp_type']="FAIL"
            failureRespToui['resp_code']=800
            failureRespToui['message']="couldn't connect to servers"
            failureRespToui['em_reqid']=request["em_reqid"]
            failureRespToui['timestamp']=request["timestamp"]
            failureRespToui['em_custid']=request["em_custid"]
            failureRespToui['resp_frm_yesb']=""
            failureRespToui['resp_frm_ewire']=""
            return staticfunctions.betoui_response(failureRespToui)
        else:
            if("HTTPConnectionPool" in TempleBeResp):
                return {"resp":"ERROR"}
            else:
                return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return {"resp":"ERROR"}
    except Exception as e:
        print("EXCEPTION2",str(e))
        return {"resp":"ERROR"}

def kanikkapay(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'KANIKKAPAY'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['requestdata'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
                    "em_custid":request['em_custid'],"txntype":request["txntype"],"hashstr":request['hashstr'],"checksum":request['checksum']}
        obj = standardresponses.commonValues
        otherdata = {}
        # 
        otherdata['parameters'] = obj
        otherdata['data'] = datadict
        print('otherdata', otherdata)
        TempleBeResp = staticfunctions.performRequest(otherdata,modulename)
        print("Temple Resp Type", type(TempleBeResp))
        # print('otherdata', otherdata)
        
        
        print("Temple Resp ", TempleBeResp)
        erresp="ERROR Response"
        if(erresp in TempleBeResp):
            failureRespToui={}
            failureRespToui['resp_type']="FAIL"
            failureRespToui['resp_code']=800
            failureRespToui['message']="couldn't connect to servers"
            failureRespToui['em_reqid']=request["em_reqid"]
            failureRespToui['timestamp']=request["timestamp"]
            failureRespToui['em_custid']=request["em_custid"]
            failureRespToui['resp_frm_yesb']=""
            failureRespToui['resp_frm_ewire']=""
            return staticfunctions.betoui_response(failureRespToui)
        else:
            if("HTTPConnectionPool" in TempleBeResp):
                return {"resp":"ERROR"}
            else:
                return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return {"resp":"ERROR"}
    except Exception as e:
        print("EXCEPTION2",str(e))
        return {"resp":"ERROR"}

#offering bill
def offeringBill(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'OFFERINGBILL'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['requestdata'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
                    "em_custid":request['em_custid'],"txntype":request["txntype"],"hashstr":request['hashstr'],"checksum":request['checksum']}
        obj = standardresponses.commonValues
        otherdata = {}
        # 
        otherdata['parameters'] = obj
        otherdata['data'] = datadict
        print('otherdata', otherdata)
        TempleBeResp = staticfunctions.performRequest(otherdata,modulename)
        print("Temple Resp Type", type(TempleBeResp))
        
        
        print("Temple Resp ", TempleBeResp)
        erresp="ERROR Response"
        if(erresp in TempleBeResp):
            failureRespToui={}
            failureRespToui['resp_type']="FAIL"
            failureRespToui['resp_code']=800
            failureRespToui['message']="couldn't connect to servers"
            failureRespToui['em_reqid']=request["em_reqid"]
            failureRespToui['timestamp']=request["timestamp"]
            failureRespToui['em_custid']=request["em_custid"]
            failureRespToui['resp_frm_yesb']=""
            failureRespToui['resp_frm_ewire']=""
            return staticfunctions.betoui_response(failureRespToui)
        else:
            if("HTTPConnectionPool" in TempleBeResp):
                return {"resp":"ERROR"}
            else:
                return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return {"resp":"ERROR"}
    except Exception as e:
        print("EXCEPTION2",str(e))
        return {"resp":"ERROR"}
#nearby attractin
def nearbyattraction(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'NEARBYATRCTIN'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['requestdata'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
                    "em_custid":request['em_custid'],"txntype":request["txntype"],"hashstr":request['hashstr'],"checksum":request['checksum']}
        obj = standardresponses.commonValues
        otherdata = {}
        # 
        otherdata['parameters'] = obj
        otherdata['data'] = datadict
        print('otherdata', otherdata)
        TempleBeResp = staticfunctions.performRequest(otherdata,modulename)
       
       
        print("Temple Resp ", TempleBeResp)
        erresp="ERROR Response"
        if(erresp in TempleBeResp):
            failureRespToui={}
            failureRespToui['resp_type']="FAIL"
            failureRespToui['resp_code']=800
            failureRespToui['message']="couldn't connect to servers"
            failureRespToui['em_reqid']=request["em_reqid"]
            failureRespToui['timestamp']=request["timestamp"]
            failureRespToui['em_custid']=request["em_custid"]
            failureRespToui['resp_frm_yesb']=""
            failureRespToui['resp_frm_ewire']=""
            return staticfunctions.betoui_response(failureRespToui)
        else:
            if("HTTPConnectionPool" in TempleBeResp):
                return {"resp":"ERROR"}
            else:
                return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return {"resp":"ERROR"}
    except Exception as e:
        print("EXCEPTION2",str(e))
        return {"resp":"ERROR"}

#nearest stay
def neareststay(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'NEARESTSTAY'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['requestdata'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
                    "em_custid":request['em_custid'],"txntype":request["txntype"],"hashstr":request['hashstr'],"checksum":request['checksum']}
        obj = standardresponses.commonValues
        otherdata = {}
        # 
        otherdata['parameters'] = obj
        otherdata['data'] = datadict
        print('otherdata', otherdata)
        TempleBeResp = staticfunctions.performRequest(otherdata,modulename)
        print("Temple Resp Type", type(TempleBeResp))
        
        
        print("Temple Resp ", TempleBeResp)
        erresp="ERROR Response"
        if(erresp in TempleBeResp):
            failureRespToui={}
            failureRespToui['resp_type']="FAIL"
            failureRespToui['resp_code']=800
            failureRespToui['message']="couldn't connect to servers"
            failureRespToui['em_reqid']=request["em_reqid"]
            failureRespToui['timestamp']=request["timestamp"]
            failureRespToui['em_custid']=request["em_custid"]
            failureRespToui['resp_frm_yesb']=""
            failureRespToui['resp_frm_ewire']=""
            return staticfunctions.betoui_response(failureRespToui)
        else:
            if("HTTPConnectionPool" in TempleBeResp):
                return {"resp":"ERROR"}
            else:
                return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return {"resp":"ERROR"}
    except Exception as e:
        print("EXCEPTION2",str(e))
        return {"resp":"ERROR"}


def validateJSON(jsonData, schemaname):
    str1 = {}
    try:
        validated = validate(instance=jsonData, schema=schemaname)
        return {"respType": "success"}
    except jsonschema.exceptions.ValidationError as err:
        return {"respType": "failure"}
        
#lord
def listdiety(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'USERDIETY'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['requestdata'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
                    "em_custid":request['em_custid'],"txntype":request["txntype"],"hashstr":request['hashstr'],"checksum":request['checksum']}
        obj = standardresponses.commonValues
        otherdata = {}
        # 
        otherdata['parameters'] = obj
        otherdata['data'] = datadict
        print('otherdata', otherdata)
        TempleBeResp = staticfunctions.performRequest(otherdata,modulename)
        print("Temple Resp Type", type(TempleBeResp))
       
       
        print("Temple Resp ", TempleBeResp)
        erresp="ERROR Response"
        if(erresp in TempleBeResp):
            failureRespToui={}
            failureRespToui['resp_type']="FAIL"
            failureRespToui['resp_code']=800
            failureRespToui['message']="couldn't connect to servers"
            failureRespToui['em_reqid']=request["em_reqid"]
            failureRespToui['timestamp']=request["timestamp"]
            failureRespToui['em_custid']=request["em_custid"]
            failureRespToui['resp_frm_yesb']=""
            failureRespToui['resp_frm_ewire']=""
            return staticfunctions.betoui_response(failureRespToui)
        else:
            if("HTTPConnectionPool" in TempleBeResp):
                return {"resp":"ERROR"}
            else:
                return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return {"resp":"ERROR"}
    except Exception as e:
        print("EXCEPTION2",str(e))
        return {"resp":"ERROR"}
#location
def location(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'LOCATION'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['requestdata'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
                    "em_custid":request['em_custid'],"txntype":request["txntype"],"hashstr":request['hashstr'],"checksum":request['checksum']}
        obj = standardresponses.commonValues
        otherdata = {}
        # 
        otherdata['parameters'] = obj
        otherdata['data'] = datadict
        print('otherdata', otherdata)
        TempleBeResp = staticfunctions.performRequest(otherdata,modulename)
        print("Temple Resp Type", type(TempleBeResp))
        
        
        print("Temple Resp ", TempleBeResp)
        erresp="ERROR Response"
        if(erresp in TempleBeResp):
            failureRespToui={}
            failureRespToui['resp_type']="FAIL"
            failureRespToui['resp_code']=800
            failureRespToui['message']="couldn't connect to servers"
            failureRespToui['em_reqid']=request["em_reqid"]
            failureRespToui['timestamp']=request["timestamp"]
            failureRespToui['em_custid']=request["em_custid"]
            failureRespToui['resp_frm_yesb']=""
            failureRespToui['resp_frm_ewire']=""
            return staticfunctions.betoui_response(failureRespToui)
        else:
            if("HTTPConnectionPool" in TempleBeResp):
                return {"resp":"ERROR"}
            else:
                return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return {"resp":"ERROR"}
    except Exception as e:
        print("EXCEPTION2",str(e))
        return {"resp":"ERROR"}



#map
def map(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'MAP'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['requestdata'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
                    "em_custid":request['em_custid'],"txntype":request["txntype"],"hashstr":request['hashstr'],"checksum":request['checksum']}
        obj = standardresponses.commonValues
        otherdata = {}
        # 
        otherdata['parameters'] = obj
        otherdata['data'] = datadict
        print('otherdata', otherdata)
        TempleBeResp = staticfunctions.performRequest(otherdata,modulename)
        print("Temple Resp Type", type(TempleBeResp))
        
        
        print("Temple Resp ", TempleBeResp)
        erresp="ERROR Response"
        if(erresp in TempleBeResp):
            failureRespToui={}
            failureRespToui['resp_type']="FAIL"
            failureRespToui['resp_code']=800
            failureRespToui['message']="couldn't connect to servers"
            failureRespToui['em_reqid']=request["em_reqid"]
            failureRespToui['timestamp']=request["timestamp"]
            failureRespToui['em_custid']=request["em_custid"]
            failureRespToui['resp_frm_yesb']=""
            failureRespToui['resp_frm_ewire']=""
            return staticfunctions.betoui_response(failureRespToui)
        else:
            if("HTTPConnectionPool" in TempleBeResp):
                return {"resp":"ERROR"}
            else:
                return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return {"resp":"ERROR"}
    except Exception as e:
        print("EXCEPTION2",str(e))
        return {"resp":"ERROR"}


def validateJSON(jsonData, schemaname):
    str1 = {}
    try:
        validated = validate(instance=jsonData, schema=schemaname)
        return {"respType": "success"}
    except jsonschema.exceptions.ValidationError as err:
        return {"respType": "failure"}