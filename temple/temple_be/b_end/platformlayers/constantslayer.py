from b_end.maass import maasslogger
import json,jsonschema
import re
from b_end.statics import staticfunctions
from b_end.platformlayers import standardresponses
from b_end.statics import urlconstants
from jsonschema import validate
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
        #convert string to dictionary
        return json.loads(input)
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
        print("Temple Resp ", TempleBeResp)
        TempleBeResp =convinptodict(TempleBeResp)
        # print("ivide ethi 1",TempleBeResp)
        return TempleBeResp 
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

def accountstatement(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    try:
        modulename = 'ACCSTATEMENT'
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
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)



def Createpooja(req):
    print('Req Type', type(req))
    request = convinptodict(req)
    print("**********************************",request)
    try:
        modulename = 'CREATEPOOJA'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
                    "em_custid":request['em_custid'],"txntype":request["txntype"],"hashstr":request['hashstr'],"checksum":request['checksum']}
        obj = standardresponses.commonValues
        otherdata = {}
        # 
        otherdata['parameters'] = obj
        otherdata['data'] = datadict
        # print('otherdata', otherdata)
        TempleBeResp = staticfunctions.performRequest(otherdata,modulename)
        # print("Build Resp Type", type(TempleBeResp))
        print("Temple Resp ", TempleBeResp)
        TempleBeResp =convinptodict(TempleBeResp)
        # print("ivide ethi 1",TempleBeResp)
        return TempleBeResp 
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

    
def Listpooja(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    try:
        modulename = 'LISTPOOJA'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
                    "em_custid":request['em_custid'],"txntype":request["txntype"],"hashstr":request['hashstr'],"checksum":request['checksum']}
        obj = standardresponses.commonValues
        otherdata = {}
        # 
        otherdata['parameters'] = obj
        otherdata['data'] = datadict
        # print('otherdata', otherdata)
        TempleBeResp = staticfunctions.performRequest(otherdata,modulename)
        # print("Build Resp Type", type(TempleBeResp))
        print("Temple Resp ", TempleBeResp)
        TempleBeResp =convinptodict(TempleBeResp)
        # print("ivide ethi 1",TempleBeResp)
        return TempleBeResp 
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)
    
def Createprasadam(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    try:
        modulename = 'CREAPRASADAM'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
                    "em_custid":request['em_custid'],"txntype":request["txntype"],"hashstr":request['hashstr'],"checksum":request['checksum']}
        obj = standardresponses.commonValues
        otherdata = {}
        # 
        otherdata['parameters'] = obj
        otherdata['data'] = datadict
        # print('otherdata', otherdata)
        TempleBeResp = staticfunctions.performRequest(otherdata,modulename)
        # print("Build Resp Type", type(TempleBeResp))
        print("Temple Resp ", TempleBeResp)
        TempleBeResp =convinptodict(TempleBeResp)
        # print("ivide ethi 1",TempleBeResp)
        return TempleBeResp 
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)
def Listprasadam(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    try:
        modulename = 'LISTPRASADAM'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
                    "em_custid":request['em_custid'],"txntype":request["txntype"],"hashstr":request['hashstr'],"checksum":request['checksum']}
        obj = standardresponses.commonValues
        otherdata = {}
        # 
        otherdata['parameters'] = obj
        otherdata['data'] = datadict
        # print('otherdata', otherdata)
        TempleBeResp = staticfunctions.performRequest(otherdata,modulename)
        # print("Build Resp Type", type(TempleBeResp))
        print("Temple Resp ", TempleBeResp)
        TempleBeResp =convinptodict(TempleBeResp)
        # print("ivide ethi 1",TempleBeResp)
        return TempleBeResp 
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

def crediety(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'CREDIETY'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
            return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)




def Createofferings(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    try:
        modulename = 'CREAOFFERINGS'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
        TempleBeResp = staticfunctions.performRequest(otherdata,modulename)
        # print("Build Resp Type", type(TempleBeResp))
        print("Temple Resp ", TempleBeResp)
        TempleBeResp =convinptodict(TempleBeResp)
        # print("ivide ethi 1",TempleBeResp)
        return TempleBeResp 
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

def listdiety(req):
    request = convinptodict(req)
    try:
        modulename = 'LISTDIETY'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
            return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)
   
def Listofferings(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    try:
        modulename = 'LISTOFFERINGS'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
        TempleBeResp =convinptodict(TempleBeResp)
        # print("ivide ethi 1",TempleBeResp)
        return TempleBeResp 
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

def crehistory(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'CREDIETY'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
            return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

def listtotal(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'LISTTOTAL'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
            return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

def creaccsuper(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'CREATECCOUNT'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
            return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

def listaccsuper(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'LISTACCOUNT'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
            return TempleBeResp 
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

#create trans temp superadmin

def cretranstemp(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'CREATETRANSTEMP'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
            return TempleBeResp 
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

def listtranstemp(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'LISTTRANSTEMP'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
            return TempleBeResp 
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

def credevaswomsuper(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'CREATEDEVASWOM'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
            return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

def listdevaswomsuper(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'LISTDEVASWOM'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
            return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

def crebankadminsuper(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'CREATEBANKADMIN'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
            return TempleBeResp 
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

def listmaangebankadminsuper(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'LISTMNGBANKADMIN'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
            return TempleBeResp 
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

def cardallocate(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'CARDALLOCATE'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
            return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

def listcardallocate(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'LISTCARDALLOCATE'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
            return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

def creblocktemple(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'CREATEBLOCKTEMPLE'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
            return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

def listblocktemple(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'LISTBLOCKTEMPLE'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
            return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

def repbydiety(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'REPDIETY'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
            return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

def repbydate(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'REPDATE'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
            return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

def repbycustcity(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'REPCUSTCITY'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
            return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

def invoiceview(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'INVOICEVIEW'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
            return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

def invoicelist(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'INVOICELIST'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
            return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

def invoicesearch(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'INVOICESEARCH'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
            return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

def createparking(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'CREPARKING'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
            return TempleBeResp 
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

def listparking(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'LISTPARKING'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
            return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

def createsightseeing(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'CRESIGHTSEEING'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
            return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

def listsightseeing(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'LISTSIGHTSEEING'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
            return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

def dropdiety(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'DROPDOWNDIETY'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
            return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)

def droprate(req):
    # print('Req Type', type(req))
    request = convinptodict(req)
    print(">>>>>>>>>>>>>>>request",request)
    try:
        modulename = 'DROPDOWNDRATE'
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['api_name'],"modulename":modulename,"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['req_data'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
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
            return TempleBeResp
    except ValueError as e:
        print("EXCEPTION1",str(e))
        return str(e)
    except Exception as e:
        print("EXCEPTION2",str(e))
        return str(e)




def validateJSON(jsonData, schemaname):
    str1 = {}
    try:
        validated = validate(instance=jsonData, schema=schemaname)
        return {"respType": "success"}
    except jsonschema.exceptions.ValidationError as err:
        return {"respType": "failure"}
   
