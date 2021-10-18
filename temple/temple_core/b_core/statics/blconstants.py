from collections import UserString
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

        dbQuery = {"username":request['datafrm']['username'],"password":request['datafrm']['password']}
        print("DBQUERY",dbQuery)
        dbconn = {}
        dbconn['database'] = "temple"
        dbconn['collection'] = "login"
        try:
            print(dbconn)
            print(dbQuery)
            usrSelect = dbconstants.MongoAPI(dbconn).readOne(dbQuery)
            
        except Exception as e:
            print("Exceptionnnnn",str(e))
            return str(e)
        print("USERSELECT",usrSelect)
        username = "username"
        if(username in usrSelect):
            if (request['datafrm']['username'] == usrSelect['username']) & (request['datafrm']['password'] == usrSelect['password']):
                print("REQUESTTT",request)
                dbQueryy = {"role_id": int(usrSelect['userRole'])}
                dbcon={}
                dbcon['database'] = "temple"
                dbcon['collection'] = "roles"
                userrole = dbconstants.MongoAPI(dbcon).readOne(dbQueryy)
                print("DBQuerryy",dbQueryy)
                print("USERROLE",userrole)
                datadict = {"username":usrSelect['username'],
                            "success_url": userrole['success_url'],
                            "user_prof_pic":usrSelect['userpic'],
                            "user_role":usrSelect['userRole'],
                            "user_status":usrSelect['userstatus']}
                print("DATADICTT",datadict)
                respdict = {}
                respdict['respfrmdb']=datadict
                respdict['result'] = "Success"
                print("DTA DICT",datadict)
                return respdict
            elif (request['datafrm']['username']==usrSelect['username']):
                return staticconstants.USER_NOT_EXIST
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

def accstmtfrmdbApi(request):
    try:
        #Perform username and password validation with database if hashes and checksum are valid
        request['database'] = "temple"
        request['collection'] = "login"
        # datadict = {"username":request['username'],
        #                 # "user_id": usrSelect['userid'],
        #                 "user_prof_pic":request['userpic'],
        #                 "user_role":request['userRole'],
        #                 "user_status":request['userstatus']}
        dataval = dbconstants.MongoAPI(request).readAll()
            
        # respdict = {}
        # respdict['respfrmdb']=
        # respdict['result'] = "Success"
        # return respdict

    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        return str(e)
