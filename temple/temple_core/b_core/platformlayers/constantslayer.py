from flask.globals import request
from b_core.maass import maasslogger
import json
from b_core.statics import staticfunctions,staticconstants,dbconstants
from b_core.platformlayers import standardresponses
import re
from b_core.statics import dbconstants







def parseRequestHCRD(request):
    try:
        #Convert Request to dictionary
        reqdata = convinptodict(request)
    except Exception as e:
        #Log exception
        maasslogger(request, str(e))
        return str(e)

    #parse by pre defined request data
    hashfrmInput = reqdata['hash']
    checksumfrmInput = reqdata['checksum']
    datafrmInput = reqdata['requestdata']
    #prepare a return dictionary
    retaftrParsed = {}
    retaftrParsed['hash'] = hashfrmInput
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
                        # "user_id": usrSelect['userid'],
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
        request['database'] = "buildd"
        request['collection'] = "users"
        datadict = {"d_templename":request['d_templename'],
                        "d_address1": request['d_address1'],
                        "d_address2":request['d_address2'],
                        "d_address3":request['d_address3'],
                        "d_lattitude":request['d_lattitude'],
                        "d_longitude":request['d_longitude'],
                        "d_vintage":request['d_vintage'],
                        "d_found":request['d_found'],
                        "prasadham_desc":request['prasadham_desc']}
        datavalue = dbconstants.MongoAPI(request).write(datadict)
        print("insert",datavalue)
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        return str(e)

def listTempleApi(request):
    try:
        request['database'] = "buildd"
        request['collection'] = "users"
        # datadict = {"d_templename":request['d_templename'],
        #                 "d_address1": request['d_address1'],
        #                 "d_address2":request['d_address2'],
        #                 "d_address3":request['d_address3'],
        #                 "d_lattitude":request['d_lattitude'],
        #                 "d_longitude":request['d_longitude'],
        #                 "d_vintage":request['d_vintage'],
        #                 "d_found":request['d_found'],
        #                 "prasadham_desc":request['prasadham_desc']}
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
        request['database'] = "buildd"
        request['collection'] = "users"
        datadict = {"tmp_name":request['tmp_name'],
                        "ad_name": request['ad_name'],
                        "contact":request['contact'],
                        "d_email":request['d_email'],
                        "d_add1":request['d_add1'],
                        "d_add2":request['d_add2'],
                        "d_state":request['d_state'],
                        }
        datavalue = dbconstants.MongoAPI(request).write(datadict)
        print("insert",datavalue)
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        return str(e)


def listTempleAdminApi(request):
    try:
        request['database'] = "buildd"
        request['collection'] = "users"
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
        request['database'] = "buildd"
        request['collection'] = "users"
        datadict = {"tmp_name":request['tmp_name'],
                        "bank_name": request['bank_name'],
                        "acc_no":request['acc_no'],
                        "ifsc":request['ifsc'],
                        "d_add1":request['d_add1'],
                        }
        datavalue = dbconstants.MongoAPI(request).write(datadict)
        print("insert",datavalue)
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        return str(e)

def listAccountApi(request):
    try:
        request['database'] = "buildd"
        request['collection'] = "users"
        datavalue = dbconstants.MongoAPI(request).read()
        print("listed",datavalue)
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        return str(e)