from flask.globals import request
from b_core.maass import maasslogger
import json
from b_core.statics import staticfunctions,staticconstants,dbconstants
from b_core.platformlayers import standardresponses
import re



#=======================================================================
#LOGIN DB

def checkuserfrmdb(request):
    try:
        # print("        REQUEST IVIDE ETHI    ",request)
        #Perform username and password validation with database if hashes and checksum are valid
        dbQuery = {"username":request['datafrm']['username'],"password":request['datafrm']['password']}
        # print("           ividethi           ",dbQuery)
        request['database'] = "temple"
        request['collection'] = "login"
        usrSelect = dbconstants.MongoAPI(request).readOne(dbQuery)
        # print("     ividethi 2   ",usrSelect)
        # print("     ividethi 2   ",type(usrSelect))
        # print("request********",request)
        if (request['datafrm']['username'] == usrSelect['username']) & (request['datafrm']['password'] == usrSelect['password']):
            # print(">>>>>>>>>>>>>>>>.")
            # print(usrSelect['username'])
            # print(usrSelect['userpic'])
            # print(usrSelect['userRole'])
            # print(usrSelect['userstatus'])
            datadict = {"username":usrSelect['username'],
                        # "user_id": usrSelect['userid'],
                        "user_prof_pic":usrSelect['userpic'],
                        "user_role":usrSelect['userRole'],
                        "user_status":usrSelect['userstatus']}


            respdict = {}
            respdict['respfrmdb']=datadict
            respdict['result'] = "Success"
           
            
            # print("DTA DICT",datadict)

            return respdict
        else:
            return staticconstants.INVALID_USER_PASS
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        return str(e)
#=======================================================================
#ACCOUNT STATEMENT DB

def accstmtfrmdb(request):
    try:
        #Perform username and password validation with database if hashes and checksum are valid
        request['database'] = "temple"
        request['collection'] = "login"
        datadict = {"username":request['username'],
                        # "user_id": usrSelect['userid'],
                        "user_prof_pic":request['userpic'],
                        "user_role":request['userRole'],
                        "user_status":request['userstatus']}
        dataval = dbconstants.MongoAPI(request).readOne(datadict)
            
        respdict = {}
        respdict['respfrmdb']=datadict
        respdict['result'] = "Success"
        return respdict

    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        return str(e)
