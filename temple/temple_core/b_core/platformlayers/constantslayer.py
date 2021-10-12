from flask.globals import request
from b_core.maass import maasslogger
import json
from b_core.statics import staticfunctions,staticconstants
from b_core.platformlayers import standardresponses
import re





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
    rethashableonly = hashabledata['username']
    print("RETHASHABLEONLY",rethashableonly)
    #Prepare Data
    hashinput = preparehash(rethashableonly)
    #Convert to Hash
    hashh = callmaass4hashing(hashinput, modulename)
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
    requestDataJson=json.dumps(hashinput)
    urls = staticfunctions.getUrlsbyModule(modulename)
    configparams = standardresponses.commonValues
    respfrmmasshash = staticfunctions.performRequest(standardresponses.checkUserServers,standardresponses.checkUserHeaders,requestDataJson,standardresponses.checkUserReqType,standardresponses.checkUserMethodType,standardresponses.checkUserEndpoint)

def checkuserfrmdb(request):
    try:
        #Perform username and password validation with database if hashes and checksum are valid
        dbQuery = {"username":request['requestdata']['username'],"password":request['requestdata']['password']}
        request['database'] = "buildd"
        request['collection'] = "users"
        usrSelect = staticfunctions.MongoAPI(request).readOne(dbQuery)
        if (request['requestdata']['username'] == usrSelect['username']) & (request['requestdata']['password'] == usrSelect['password']):
            datadict = {"username":usrSelect['username'],
                        # "user_id": usrSelect['userid'],
                        "user_prof_pic":usrSelect['userpic'],
                        "user_role":usrSelect['userRole'],
                        "user_status":usrSelect['userStatus']["SUCCESS"]}
            return datadict
        else:
            return staticconstants.INVALID_USER_PASS
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        return str(e)
