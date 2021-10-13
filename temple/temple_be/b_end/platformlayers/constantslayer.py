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
    if(isinstance(input,dict)):
        #it is already dict
        return input
    elif(isinstance(input,str)):
        #convert string to dictionary
        return json.loads(input)
    elif(isinstance(input,int)):
        #convert iny to dictionary
        return json.loads(input)


def checklogin(req):
    request = req.get_json()
    try:
        datadict = {"req_type":request['req_type'],"req_code":request['req_code'],
                    "apiname":request['apiname'],"modulename":request['modulename'],"em_reqid":request['em_reqid'],
                    "partner_reqid":request['partner_reqid'],"requestdata":request['requestdata'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
                    "em_custid":request['em_custid'],"txntype":request["txntype"],"hashstr":request['hashstr'],"checksum":request['checksum']}
        obj = standardresponses.commonValues
        otherdata = {}
        # modulename = 'LOGIN'
        otherdata['parameters'] = obj
        otherdata['data'] = datadict
        print('otherdata', otherdata)
        BuildBeResp = staticfunctions.performRequest(otherdata,request['modulename'])
        print("ivide ethi 1",BuildBeResp)
        return BuildBeResp
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
    except jsonschema.exceptions.ValidationError as err:
        return {"respType": "failure"}
    return {"respType": "success"}