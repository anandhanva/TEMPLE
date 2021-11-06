from collections import UserString
from flask.globals import request
from pymongo.message import query
from b_core.maass import maasslogger
import json
from b_core.statics import staticfunctions,staticconstants,dbconstants
from b_core.platformlayers import standardresponses
import re
import traceback, sys
# from temple.temple_core import b_core
from b_core.statics import dbmodules
from datetime import datetime



# LOGIN USER
def checkuserfrmdb(request):
    try:
    #     print("        REQUEST IVIDE ETHI    ",request)
    #     #Perform username and password validation with database if hashes and checksum are valid
    #     dbQuery = {"username":request['datafrm']['username'],"password":request['datafrm']['password']}
    #     print("           ividethi           ",dbQuery)
    #     request['database'] = "templeapp"
    #     request['collection'] = "login"
    #     usrSelect = dbconstants.MongoAPI(request).readOne(dbQuery)
    #     print("     ividethi 2   ",usrSelect)
    #     print("     ividethi 2   ",type(usrSelect))
    #     print("request********",request)
    #     if (request['datafrm']['username'] == usrSelect['username']) & (request['datafrm']['password'] == usrSelect['password']):
    #         print(">>>>>>>>>>>>>>>>.")
    #         request2 = {}
    #         dbQuery2 = {"role_id":int(usrSelect['userRole'])}
    #         request2['database'] = "templeapp"
    #         request2['collection'] = "roles"
    #         successurl = dbconstants.MongoAPI(request2).readOne(dbQuery2)
    #         # print("@!@!@!", successurl)
    #         # print(usrSelect['username'])
    #         # print(usrSelect['userpic'])
    #         # print(usrSelect['userRole'])
    #         # print(usrSelect['userstatus'])
    #         datadict = {"username":usrSelect['username'],
    #                     "user_prof_pic":usrSelect['userpic'],
    #                     "user_role":usrSelect['userRole'],
    #                     "success_url":successurl['success_url'],
    #                     "user_status":usrSelect['userstatus'],
    #                     "templeid":usrSelect['templeid']
    #                     }


    #         respdict = {}
    #         respdict['respfrmdb']=datadict
    #         respdict['result'] = "Success"
           
            
    #         print("DTA DICT",datadict)

    #         return respdict
    #     else:
    #         return staticconstants.INVALID_USER_PASS
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "login":"userlogin",
            "logintype":"user1"
        }
        print("dict***",dict)
        respdict={}
        respdict["respfrmdb"]=dict
        respdict["result"]="Success"
        return respdict
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        # for frame in traceback.extract_tb(sys.exc_info()[2]):
        #     fname,lineno,fn,text = frame
        #     print( "Error in %s on line %d", fname, lineno)
        return str(e)



# LOGIN OTPVERIFICATION
def processOtpVerificationtapi(request):
    try:
    #     print("        REQUEST IVIDE ETHI    ",request)
    #     #Perform username and password validation with database if hashes and checksum are valid
    #     dbQuery = {"username":request['datafrm']['username'],"password":request['datafrm']['password']}
    #     print("           ividethi           ",dbQuery)
    #     request['database'] = "templeapp"
    #     request['collection'] = "login"
    #     usrSelect = dbconstants.MongoAPI(request).readOne(dbQuery)
    #     print("     ividethi 2   ",usrSelect)
    #     print("     ividethi 2   ",type(usrSelect))
    #     print("request********",request)
    #     if (request['datafrm']['username'] == usrSelect['username']) & (request['datafrm']['password'] == usrSelect['password']):
    #         print(">>>>>>>>>>>>>>>>.")
    #         request2 = {}
    #         dbQuery2 = {"role_id":int(usrSelect['userRole'])}
    #         request2['database'] = "templeapp"
    #         request2['collection'] = "roles"
    #         successurl = dbconstants.MongoAPI(request2).readOne(dbQuery2)
    #         # print("@!@!@!", successurl)
    #         # print(usrSelect['username'])
    #         # print(usrSelect['userpic'])
    #         # print(usrSelect['userRole'])
    #         # print(usrSelect['userstatus'])
    #         datadict = {"username":usrSelect['username'],
    #                     "user_prof_pic":usrSelect['userpic'],
    #                     "user_role":usrSelect['userRole'],
    #                     "success_url":successurl['success_url'],
    #                     "user_status":usrSelect['userstatus'],
    #                     "templeid":usrSelect['templeid']
    #                     }


    #         respdict = {}
    #         respdict['respfrmdb']=datadict
    #         respdict['result'] = "Success"
           
            
    #         print("DTA DICT",datadict)

    #         return respdict
    #     else:
    #         return staticconstants.INVALID_USER_PASS
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "otp":"otpsend",
            "number":"1234"
        }
        print("dict***",dict)
        respdict={}
        respdict["respfrmdb"]=dict
        respdict["result"]="Success"
        return respdict
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        # for frame in traceback.extract_tb(sys.exc_info()[2]):
        #     fname,lineno,fn,text = frame
        #     print( "Error in %s on line %d", fname, lineno)
        return str(e)