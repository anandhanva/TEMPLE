from flask.globals import request
from b_core.maass import maasslogger
import json
from b_core.statics import staticfunctions,staticconstants,dbconstants
from b_core.platformlayers import standardresponses
import re
from b_core.statics import dbconstants
import json,jsonschema
from jsonschema import validate


def parseRequestHCRD(request):
    try:
        #Convert Request to dictionary
        reqdata = convinptodict(request)
    except Exception as e:
        #Log exception
        maasslogger(request, str(e))
        return str(e)

    #parse by pre defined request data
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
        #convert int to dictionary
        return json.loads(input)

def createHashfromData(request, modulename):
    #Extract Data
    hashabledata = convinptodict(request)
    print("HASHABLEDATA",hashabledata)
    rethashableonly = hashabledata
    print("RETHASHABLEONLY",rethashableonly)
    #Prepare Data
    hashinput = preparehash(rethashableonly)
    print("HASHINPUT",hashinput)
    hashinput = json.dumps(hashinput)
    #Convert to Hash
    hashh = callmaass4hashing(hashinput, modulename)
    print("HASSHH***",hashh)
    #Return Hash
    return hashh

def preparehash(dataset):
    # print("request",request)
    hashstr = re.sub("{","||||",str(dataset)) # replace open brackets
    hashstr = re.sub("}","||||",hashstr) # replace close brackets
    hashstr = re.sub(":","|",hashstr) # replace semicolons
    hashstr = re.sub(" ","",hashstr) # replace spaces
    hashifyrequestdata = re.sub(",","||",hashstr) # replace commasz
    return hashifyrequestdata


def callmaass4hashing(hashinput, modulename):
    # requestDataJson=json.dumps(hashinput)
    # print("REQUESTDATA",requestDataJson)
    configparams = staticfunctions.getUrlsbyModule(modulename)
    
    # configparams = json.dumps(configparams)
    print("CONFIG",configparams)
    logdata = {}
    logdata['parameters'] = configparams
   
    logdata['data'] = hashinput
    print("LOGDATA",logdata)
    print("LOGDATA",type(logdata))
    respfrmmasshash = staticfunctions.performRequest(logdata)
    # checkUserServers,standardresponses.checkUserHeaders,requestDataJson,standardresponses.checkUserReqType,standardresponses.checkUserMethodType,standardresponses.checkUserEndpoint)
    return respfrmmasshash
    print("RESPFROMMAASS",respfrmmasshash)

def checkuserfrmdb(request):
    try:
        print("        REQUEST IVIDE ETHI    ",request)
        #Perform username and password validation with database if hashes and checksum are valid
        dbQuery = {"username":request['datafrm']['username'],"password":request['datafrm']['password']}
        print("           ividethi           ",dbQuery)
        request['database'] = "temple"
        request['collection'] = "login"
        usrSelect = dbconstants.MongoAPI(request).readOne(dbQuery)
        print("     ividethi 2   ",usrSelect)
        print("     ividethi 2   ",type(usrSelect))
        print("request********",request)
        if (request['datafrm']['username'] == usrSelect['username']) & (request['datafrm']['password'] == usrSelect['password']):
            print(">>>>>>>>>>>>>>>>.")
            print(usrSelect['username'])
            print(usrSelect['userpic'])
            print(usrSelect['userRole'])
            print(usrSelect['userstatus'])
            datadict = {"username":usrSelect['username'],
                        "user_prof_pic":usrSelect['userpic'],
                        "user_role":usrSelect['userRole'],
                        "user_status":usrSelect['userstatus']}


            respdict = {}
            respdict['respfrmdb']=datadict
            respdict['result'] = "Success"
           
            
            print("DTA DICT",datadict)

            return respdict
        else:
            return staticconstants.INVALID_USER_PASS
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        return str(e)


def addTempleApi(request):
    try:
        print("request>>>>>>>>>>>>>>>>>>.",request)
        request['database'] = "temple"
        request['collection'] = "temple_list"
        datadict={}
        datadict['d_templename'] = request['datafrm']['d_templename'],
        datadict['d_address1'] = request['datafrm']['d_address1'],
        datadict['d_address2'] = request['datafrm']['d_address2'],
        datadict['d_address3'] = request['datafrm']['d_address3'],
        datadict['d_lattitude'] = request['datafrm']['d_lattitude'],
        datadict['d_longitude'] = request['datafrm']['d_longitude'],
        datadict['d_vintage'] = request['datafrm']['d_vintage'],
        datadict['d_found'] = request['datafrm']['d_found'],
        datadict['temp_desc'] = request['datafrm']['temp_desc'],
        print("Datadict*************",datadict)
        datavalue = dbconstants.MongoAPI(request).write(datadict)
        print("insert",datavalue)
        respdict={}
        respdict['respfrmdb'] = datadict
        respdict['result']="Success"
        del datadict['_id']
        print("type------",type(datadict))
        print("respdict!!!!!!!!!",datadict)
        return respdict
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        return str(e)

def listTempleApi(request):
    try:
        print("REQUEST##########",request)
        request['database'] = "temple"
        request['collection'] = "temple_list"
        datavalue = dbconstants.MongoAPI(request).read()
        print("listed",datavalue)

    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        return str(e)

def createTempleAdminApi(request):
    try:
        request['database'] = "temple"
        request['collection'] = "temple_admin"
        datadict={}
        datadict['tmp_name'] = request['datafrm']['tmp_name'],
        datadict['ad_name'] = request['datafrm']['ad_name'],
        datadict['contact'] = request['datafrm']['contact'],
        datadict['d_email'] = request['datafrm']['d_email'],
        datadict['d_add1'] = request['datafrm']['d_add1'],
        datadict['d_add2'] = request['datafrm']['d_add2'],
        datadict['d_state'] = request['datafrm']['d_state'],
        print("Datadict*************",datadict)
        datavalue = dbconstants.MongoAPI(request).write(datadict)
        print("insert",datavalue)
        respdict={}
        respdict['respfrmdb'] = datadict
        respdict['result']="Success"
        del datadict['_id']
        print("type------",type(datadict))
        print("respdict!!!!!!!!!",datadict)
        return respdict
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        return str(e)


def listTempleAdminApi(request):
    try:
        request['database'] = "temple"
        request['collection'] = "temple_admin"
        datavalue = dbconstants.MongoAPI(request).read()
        print("listed",datavalue)
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        return str(e)


def createAccountApi(request):
    try:
        request['database'] = "temple"
        request['collection'] = "temp_account"
        datadict={}
        datadict['tmp_name'] = request['datafrm']['tmp_name'],
        datadict['bank_name'] = request['datafrm']['bank_name'],
        datadict['acc_no'] = request['datafrm']['acc_no'],
        datadict['ifsc'] = request['datafrm']['ifsc'],
        datadict['d_add1'] = request['datafrm']['d_add1'],
        print("Datadict*************",datadict)
        datavalue = dbconstants.MongoAPI(request).write(datadict)
        print("insert",datavalue)
        respdict={}
        respdict['respfrmdb'] = datadict
        respdict['result']="Success"
        del datadict['_id']
        print("type------",type(datadict))
        print("respdict!!!!!!!!!",datadict)
        return respdict
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        return str(e)

def listAccountApi(request):
    try:
        request['database'] = "temple"
        request['collection'] = "temp_account"
        datavalue = dbconstants.MongoAPI(request).read()
        print("listed",datavalue)
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        return str(e)
