from collections import UserString
from flask.globals import request
from pymongo.message import query
from b_core.maass import maasslogger
import json
from b_core.statics import staticfunctions,staticconstants,dbconstants
from b_core.platformlayers import standardresponses
import re



#=======================================================================
#LOGIN DB

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
            request2 = {}
            dbQuery2 = {"role_id":int(usrSelect['userRole'])}
            request2['database'] = "temple"
            request2['collection'] = "roles"
            successurl = dbconstants.MongoAPI(request2).readOne(dbQuery2)
            print("@!@!@!", successurl)
            print(usrSelect['username'])
            print(usrSelect['userpic'])
            print(usrSelect['userRole'])
            print(usrSelect['userstatus'])
            datadict = {"username":usrSelect['username'],
                        "user_prof_pic":usrSelect['userpic'],
                        "user_role":usrSelect['userRole'],
                        "success_url":successurl['success_url'],
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


def createFinAdminApi(request):
    try:
        request['database'] = "temple"
        request['collection'] = "finance_admin"
        datadict={}
        datadict['tmp_name'] = request['datafrm']['tmp_name'],
        datadict['ad_name'] = request['datafrm']['ad_name'],
        datadict['d_email'] = request['datafrm']['d_email'],
        datadict['d_add1'] = request['datafrm']['d_add1'],
        datadict['d_add2'] = request['datafrm']['d_add2'],
        datadict['d_state'] = request['datafrm']['d_state'],
        datadict['bank_name'] = request['datafrm']['bank_name'],
        datadict['d_accno'] = request['datafrm']['d_accno'],
        datadict['ifsc'] = request['datafrm']['ifsc'],

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


def createPoojaApi(request):
    try:
    
        request['database'] = "temple"
        request['collection'] = "pooja"
        modulename='CREATEPOOJA'
        request['modulename'] = modulename
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print(request['datafrm']['pooja_name'])
        datadict={}
        datadict['pooja_name'] = request['datafrm']['pooja_name']
        datadict['pooja_rateid'] = request['datafrm']['pooja_rateid']
        datadict['pooja_descr'] = request['datafrm']['pooja_descr']
        datadict['pooja_templeid'] = request['datafrm']['templeid']
        countdocs = dbconstants.MongoAPI(request).count({})
        datadict['pooja_id'] = int(countdocs) + 1
        datadict['status'] = 1
         

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
def listTemplePoojaApi(request):
    try:
        dbQuery = {"pooja_templeid":request['datafrm']['temple_id']}
        request['database'] = "temple"
        request['collection'] = "pooja"
        datavalue = dbconstants.MongoAPI(request).read(dbQuery)
        print("listed",datavalue)
        return datavalue        
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        return str(e)


def createOfferingApi(request):
    try:
        request['database'] = "temple"
        request['collection'] = "offering"
        modulename='CREAOFFERINGS'

        request['modulename'] = modulename
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print(request['datafrm']['offering_name'])
        datadict={}
        datadict['offering_name'] = request['datafrm']['offering_name']
        datadict['offering_rateid'] = request['datafrm']['offering_rateid']
        datadict['offering_descr'] = request['datafrm']['offering_descr']
        datadict['offering_templeid'] = request['datafrm']['templeid']
        countdocs = dbconstants.MongoAPI(request).count({})
        datadict['offering_id'] = int(countdocs) + 1
        datadict['status'] = 1
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


def listTempleOfferingApi(request):
    try:
        dbQuery = {"offering_templeid":request['datafrm']['temple_id']}
        request['database'] = "temple"
        request['collection'] = "offering"
        datavalue = dbconstants.MongoAPI(request).read(dbQuery)
        print("listed",datavalue)
        return datavalue  
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        return str(e)
def createPrasadamApi(request):
    try:
        request['database'] = "temple"
        request['collection'] = "prasadam"
        datadict={}
        datadict['templeid'] = request['datafrm']['templeid'],
        datadict['prasadam_name'] = request['datafrm']['prasadam_name'],
        datadict['prasadam_amount'] = request['datafrm']['prasadam_amount'],
        datadict['prasadam_description'] = request['datafrm']['prasadam_description']
        datadict['prasadam_count'] = request['datafrm']['prasadam_count']
        datadict['prasadam_measure'] = request['datafrm']['prasadam_measure']

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


def listTemplePrasadamApi(request):
    try:
        request['database'] = "temple"
        request['collection'] = "prasadam"
        datavalue = dbconstants.MongoAPI(request).readAll()
        print("listed",datavalue)
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        return str(e)

def createDietyApi(request):
    try:
        request['database'] = "temple"
        request['collection'] = "diety"
        datadict={}
        datadict['templeid'] = request['datafrm']['templeid'],
        datadict['diety_name'] = request['datafrm']['diety_name'],
        datadict['diety_desc'] = request['datafrm']['diety_desc'],
        datadict['diety_photo'] = request['datafrm']['diety_photo']
        datadict['diety_oftemp'] = request['datafrm']['diety_oftemp']

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
def listTempleDietyApi(request):
    try:
        request['database'] = "temple"
        request['collection'] = "diety"
        datavalue = dbconstants.MongoAPI(request).readAll()
        print("listed",datavalue)
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        return str(e)

def createHistoryApi(request):
    try:
        request['database'] = "temple"
        request['collection'] = "diety"
        datadict={}
        datadict['templeid'] = request['datafrm']['templeid'],
        datadict['diety_name'] = request['datafrm']['diety_name'],
        datadict['diety_desc'] = request['datafrm']['diety_desc'],
        datadict['diety_photo'] = request['datafrm']['diety_photo']
        datadict['diety_oftemp'] = request['datafrm']['diety_oftemp']

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
