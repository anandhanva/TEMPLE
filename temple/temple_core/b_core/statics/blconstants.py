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
            # print("@!@!@!", successurl)
            # print(usrSelect['username'])
            # print(usrSelect['userpic'])
            # print(usrSelect['userRole'])
            # print(usrSelect['userstatus'])
            datadict = {"username":usrSelect['username'],
                        "user_prof_pic":usrSelect['userpic'],
                        "user_role":usrSelect['userRole'],
                        "success_url":successurl['success_url'],
                        "user_status":usrSelect['userstatus'],
                        "templeid":usrSelect['templeid']
                        }


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
        datadict['createdat'] = str(datetime.now()) 
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


#=========================================================================
#CREATE POOJA
def createPoojaApi(request):
    try:
    
        # request['database'] = "temple"
        # request['collection'] = "pooja"
        modulename='CREATEPOOJA'
        request['modulename'] = modulename
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print(request['datafrm']['pooja_name'])
        datadict={}
        datadict['pooja_name'] = request['datafrm']['pooja_name']
        datadict['pooja_rateid'] = request['datafrm']['pooja_rateid']
        datadict['pooja_descr'] = request['datafrm']['pooja_descr']
        datadict['pooja_templeid'] = request['datafrm']['templeid']
        datadict['pooja_dietyid'] = request['datafrm']['deity']
        datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
        datadict['amount'] = getAmoutName(request['datafrm']['pooja_rateid'])
        datadict['createdat'] = str(datetime.now())
        countdocs = dbmodules.pooja({},datadict,"c","pooja")
        print("Count of returned docs: ",countdocs)
        datadict['pooja_id'] = int(countdocs) + 1
        datadict['status'] = 1
       
        print("Datadict*************",datadict)
        datavalue =dbmodules.pooja("",datadict,"i","pooja")
        print("insert",datavalue)
        respdict={}
        respdict['respfrmdb'] = {"response":"Success"}
        respdict['result']="Success"
        # print("type------",type(datadict))
        # print("respdict!!!!!!!!!",datadict)
        return respdict
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)
        return str(e)



def getAmoutName(id):
    request2 = {}
    dbQuery2 = {"rate_id":int(id)}
    request2['database'] = "temple"
    request2['collection'] = "rate"
    amount = dbconstants.MongoAPI(request2).readOne(dbQuery2)
    return amount['rate_amount']

def getDietyName(id):
    request3 = {}
    dbQuery3 = {"diety_id":int(id)}
    request3['database'] = "temple"
    request3['collection'] = "diety"
    diety_name = dbconstants.MongoAPI(request3).readOne(dbQuery3)
    return diety_name['diety_name']
    
#=========================================================================
#LISTPOOJA
def listTemplePoojaApi(request):
    try:
        dbQuery = {"pooja_templeid":request['datafrm']['templeid']}
        modulename='LISTPOOJA'
        request['modulename'] = modulename
        print("DALIDAJSDLASIJDLAISJDLASIJDLAISJDILASJDLASDJALSIDJALSDIASILDJASLDJ => ",dbQuery)
        datavalue =dbmodules.pooja(dbQuery, "","l","pooja")
        print("listed",datavalue)
        return datavalue        
    except ValueError as e:
        print("EXCEPTION1")
        print(str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)
        return str(e)

#=========================================================================
#CREATE OFFERINGS
def  createOfferingApi(request):
    try:
        # request['database'] = "temple"
        # request['collection'] = "offering"
        modulename='CREAOFFERINGS'
        request['modulename'] = modulename
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        # print(request['datafrm']['offering_name'])
        datadict={}
        datadict['offering_name'] = request['datafrm']['offering_name']
        print("OFFERINGID",datadict)
        datadict['offering_rateid'] = request['datafrm']['offering_rateid']
        print("OFFERINGrateid",datadict)
        datadict['offering_descr'] = request['datafrm']['offering_description']
        print("OFFERINGrateid",datadict)
        datadict['offering_templeid'] = request['datafrm']['templeid']
        print("OFFERINGrateid",datadict)
        datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
        datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
        datadict['createdat'] = str(datetime.now())
        countdocs = dbmodules.offering({},datadict,"c","offering")
        datadict['offering_id'] = int(countdocs) + 1
        datadict['status'] = 1
        print("Datadict*************",datadict)
        datavalue =dbmodules.offering("",datadict,"i","offering")
        print("insert",datavalue)
        respdict={}
        respdict['respfrmdb'] = {"response":"Success"}
        respdict['result']="Success"
        # del datadict['_id']
        # print("type------",type(datadict))
        # print("respdict!!!!!!!!!",datadict)
        return respdict
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)
        return str(e)

#=========================================================================
#LIST OFFERINGS
def listTempleOfferingApi(request):
    try:
        dbQuery = {"offering_templeid":request['datafrm']['templeid']}
        # request['database'] = "temple"
        # request['collection'] = "offering"
        # modulename='LISTOFFERINGS'
        # request['modulename'] = modulename
        datavalue =dbmodules.offering(dbQuery,"","l","offering")
        print("listed",datavalue)
        return datavalue  
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)
        return str(e)

#=========================================================================
#CREATE PRASADAM
def createPrasadamApi(request):
    try:
        # request['database'] = "temple"
        # request['collection'] = "prasadam"
        modulename='CREAPRASADAM'

        request['modulename'] = modulename
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print(request['datafrm']['prasadam_name'])
        datadict={}
        datadict['prasadam_name'] = request['datafrm']['prasadam_name']
        datadict['prasadam_rateid'] = request['datafrm']['prasadam_rateid']
        datadict['prasadam_measure'] = request['datafrm']['prasadam_measure']
        datadict['prasadam_descr'] = request['datafrm']['prasadam_descr']
        datadict['prasadam_templeid'] = request['datafrm']['templeid']
        datadict['prasadam_count'] = request['datafrm']['prasadam_count']
        datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
        datadict['amount'] = getAmoutName(request['datafrm']['prasadam_rateid'])
        datadict['createdat'] = str(datetime.now())
        countdocs = dbmodules.prasadam({},datadict,"c","prasadam")
        datadict['prasadam_id'] = int(countdocs) + 1
        datadict['status'] = 1
        print("Datadict*************",datadict)
        datavalue =dbmodules.prasadam({},datadict,"i","prasadam")
        print("insert",datavalue)
        respdict={}
        respdict['respfrmdb'] = {"response":"Success"}
        respdict['result']="Success"
        # del datadict['_id']
        # print("type------",type(datadict))
        # print("respdict!!!!!!!!!",datadict)
        return respdict
    except ValueError as e:
        print("EXCEPTION1")
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)
        return str(e)
    except Exception as e:
        print("FAILED")
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)
        return str(e)

#=========================================================================
#LIST PRASADAM
def listTemplePrasadamApi(request):
    try:
        dbQuery = {"prasadam_templeid":request['datafrm']['templeid']}
        # request['database'] = "temple"
        # request['collection'] = "prasadam"
        # modulename="LISTPRASADAM"
        # request['modulename']=modulename
        datavalue =dbmodules.prasadam(dbQuery,"","l","prasadam")
        print("listed",datavalue)
        return datavalue        
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)
        return str(e)

#=========================================================================
#CREATE DIETY
def createDietyApi(request):
    try:
    
        # request['database'] = "temple"
        # request['collection'] = "diety"
        modulename='CREATEDIETY'
        request['modulename'] = modulename
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print(request['datafrm']['diety_name'])
        datadict={}
        datadict['diety_name'] = request['datafrm']['diety_name']
        datadict['diety_oftemp'] = request['datafrm']['diety_oftemp']
        datadict['diety_photo'] = request['datafrm']['diety_photo']
        datadict['diety_descr'] = request['datafrm']['diety_desc']
        datadict['diety_templeid'] = request['datafrm']['templeid']
        datadict['createdat'] = str(datetime.now())
        countdocs = dbmodules.diety({},datadict,"c","diety")
        datadict['diety_id'] = int(countdocs) + 1
        datadict['status'] = 1
        print("Datadict*************",datadict)
        datavalue =dbmodules.diety({},datadict,"i","diety")
        print("insert",datavalue)
        respdict={}
        respdict['respfrmdb'] = {"response":"Success"}
        respdict['result']="Success"
        # del datadict['_id']
        # print("type------",type(datadict))
        # print("respdict!!!!!!!!!",datadict)
        return respdict
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)
        return str(e)

#=========================================================================
#LIST DIETY
def listTempleDietyApi(request):
    try:
        dbQuery = {"diety_templeid":request['datafrm']['templeid']}
        # request['database'] = "temple"
        # request['collection'] = "diety"
        # modulename="LISTDIETY"
        # request['modulename']=modulename
        datavalue =dbmodules.diety(dbQuery,"","l","diety")
        print("listed",datavalue)
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)
        return str(e)

#=========================================================================
#CREATE HISTORY
def createHistoryApi(request):
    try:
        # request['database'] = "temple"
        # request['collection'] = "history"
        modulename='CREHISTORY'
        request['modulename'] = modulename
        datadict={}
        datadict['history_templeid'] = request['datafrm']['templeid'],
        datadict['history_title'] = request['datafrm']['temp_name'],
        datadict['history_image1'] = request['datafrm']['diety_photo1']
        datadict['history_image2'] = request['datafrm']['diety_photo2']
        datadict['history_image3'] = request['datafrm']['diety_photo3']
        datadict['history_descr'] = request['datafrm']['t_history']
        datadict['createdat'] = str(datetime.now())
        countdocs = dbmodules.history({},datadict,"c","history")
        print("Count of returned docs: ",countdocs)
        datadict['history_id'] = int(countdocs) + 1
        datadict['status'] = 1
        print("Datadict*************",datadict)
        datavalue =dbmodules.history("",datadict,"i","history")
        print("insert",datavalue)
        respdict={}
        respdict['respfrmdb'] = {"response":"Success"}
        respdict['result']="Success"
        # print("type------",type(datadict))
        # print("respdict!!!!!!!!!",datadict)
        return respdict
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)
        return "err"

#=========================================================================
#LIST HISTORY        
def listTempleHistoryApi(request):
    try:
        dbQuery = {"history_templeid":request['datafrm']['templeid']}
        # modulename='LISTHISTORY'
        # request['modulename'] = modulename
        datavalue =dbmodules.history(dbQuery, "","l","history")
        print("listed",datavalue)
        datavalue['result'] = "Success"
        return datavalue        
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)
        return str(e)

#=========================================================================
#CREATE CATEGORY
def createCategoryApi(request):
    try:
    
        # request['database'] = "temple"
        # request['collection'] = "pooja"
        modulename='CREATECATEGORY'
        request['modulename'] = modulename
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print(request['datafrm']['category_name'])
        datadict={}
        datadict['category_name'] = request['datafrm']['title_text']
        datadict['category_photo'] = request['datafrm']['cat_image']
        datadict['category_desc'] = request['datafrm']['sel_cat']
        # datadict['stay_amount'] = request['datafrm']['title_text']
        datadict['category_templeid'] = request['datafrm']['templeid']
        datadict['createdat'] = str(datetime.now())
        countdocs = dbmodules.category({},datadict,"c","category")
        print("Count of returned docs: ",countdocs)
        datadict['category_id'] = int(countdocs) + 1
        datadict['status'] = 1
        print("Datadict*************",datadict)
        datavalue =dbmodules.category("",datadict,"i","category")
        print("insert",datavalue)
        respdict={}
        respdict['respfrmdb'] = {"response":"Success"}
        respdict['result']="Success"
        # print("type------",type(datadict))
        # print("respdict!!!!!!!!!",datadict)
        return respdict
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)
        return str(e)
        
 #=========================================================================
 # DROPDOWN DIETY       
def drpdwnTempdietyApi(request):
    try:
        dbQuery = {"diety_templeid":request['datafrm']['templeid']}
        # request['database'] = "temple"
        # request['collection'] = "diety"
        # modulename="DROPDOWNDIETY"
        # request['modulename']=modulename
        datavalue =dbmodules.diety({},dbQuery,"l","diety")
        print("listed",datavalue)
        return datavalue  
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)
        return str(e)

 # DROPDOWN RATE      
def drpdwnTemprateApi(request):
    try:
        dbQuery = {"rate_templeid":request['datafrm']['templeid']}
        # modulename='DROPDOWNRATE'
        # request['modulename'] = modulename
        datavalue =dbmodules.rate({},dbQuery,"l","rate")
        print("listed",datavalue)
        return datavalue        
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)
        return str(e)
        
#=========================================================================
#DROPDOWN QUANTITY OF PRASADAM
def drpdwnPrasadamQtyApi(request):
    try:
        dbQuery = {"templeid":request['datafrm']['templeid']}
        # request['database'] = "temple"
        # request['collection'] = "prasadam"
        datavalue =dbmodules.qnty({},dbQuery,"l","qnty")

        print("listed",datavalue)
        return datavalue
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)
        return str(e)

#=========================================================================
# CREATE KANIKKA
def createKanikkaApi(request):
    try:
    
        # request['database'] = "temple"
        # request['collection'] = "pooja"
        modulename='CREATEPOOJA'
        request['modulename'] = modulename
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print(request['datafrm']['pooja_name'])
        datadict={}
        datadict['pooja_name'] = request['datafrm']['pooja_name']
        datadict['pooja_rateid'] = request['datafrm']['pooja_rateid']
        datadict['pooja_descr'] = request['datafrm']['pooja_descr']
        datadict['pooja_templeid'] = request['datafrm']['templeid']
        datadict['createdat'] = str(datetime.now())
        countdocs = dbmodules.pooja({},datadict,"c","pooja")
        print("Count of returned docs: ",countdocs)
        # countdocs = dbconstants.MongoAPI(request).count({})
        datadict['pooja_id'] = int(countdocs) + 1
        datadict['status'] = 1
         

        print("Datadict*************",datadict)
        datavalue =dbmodules.pooja({},datadict,"i","pooja")
        print("insert",datavalue)
        respdict={}
        respdict['respfrmdb'] = datadict
        respdict['result']="Success"
        # del datadict['_id']
        print("type------",type(datadict))
        print("respdict!!!!!!!!!",datadict)
        return respdict
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        return str(e)
# def listTemplePoojaApi(request):
#     try:
#         dbQuery = {"pooja_templeid":request['datafrm']['templeid']}
#         modulename='LISTPOOJA'
#         request['modulename'] = modulename
#         datavalue =dbmodules.pooja({},dbQuery,"l","pooja")
#         print("listed",datavalue)
#         return datavalue        
#     except ValueError as e:
#         print("EXCEPTION1")
#         return str(e)
#     except Exception as e:
#         print("FAILED",str(e))
#         return str(e)

def createAirportApi(request):
    try:
        # request['database'] = "temple"
        # request['collection'] = "history"
        modulename='AIRPORT'
        request['modulename'] = modulename
        print(request['datafrm']['history_name'])
        datadict={}
        datadict['history_templeid'] = request['datafrm']['templeid'],
        datadict['history_title'] = request['datafrm']['t_name'],
        datadict['history_image1'] = request['datafrm']['t_photo1']
        datadict['history_image2'] = request['datafrm']['t_photo2']
        datadict['history_image3'] = request['datafrm']['t_photo3']
        datadict['history_descr'] = request['datafrm']['t_history']
        countdocs = dbmodules.airport({},datadict,"c","airport")
        print("Count of returned docs: ",countdocs)
        datadict['pooja_id'] = int(countdocs) + 1
        datadict['status'] = 1
        print("Datadict*************",datadict)
        datavalue =dbmodules.history("",datadict,"i","airport")
        print("insert",datavalue)
        respdict={}
        respdict['respfrmdb'] = {"response":"Success"}
        respdict['result']="Success"
        # print("type------",type(datadict))
        # print("respdict!!!!!!!!!",datadict)
        return respdict
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)
        return str(e)

#LIST STAY
def listTempleStayApi(request):
    try:
        dbQuery = {"stay_templeid":request['datafrm']['templeid']}
        # request['database'] = "temple"
        # request['collection'] = "prasadam"
        # modulename="LISTPRASADAM"
        # request['modulename']=modulename
        datavalue =dbmodules.stay(dbQuery,"","l","stay")
        print("listed",datavalue)
        return datavalue        
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)
        return str(e)

def  createRateApi(request):
    try:
        # request['database'] = "temple"
        # request['collection'] = "offering"
        modulename='ADDRATE'
        request['modulename'] = modulename
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        # print(request['datafrm']['rate_name'])
        datadict={}
        # datadict['rate_name'] = request['datafrm']['rate_name']
        datadict['rate_amount'] = request['datafrm']['rate']
        datadict['rate_templeid'] = request['datafrm']['templeid']
        # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
        # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
        datadict['createdat'] = str(datetime.now())
        countdocs = dbmodules.rate({},datadict,"c","rate")
        datadict['rate_id'] = int(countdocs) + 1
        datadict['status'] = 1
        print("Datadict*************",datadict)
        datavalue =dbmodules.rate("",datadict,"i","rate")
        print("insert",datavalue)
        respdict={}
        respdict['respfrmdb'] = {"response":"Success"}
        respdict['result']="Success"
        # del datadict['_id']
        # print("type------",type(datadict))
        # print("respdict!!!!!!!!!",datadict)
        return respdict
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)
        return str(e)
def  createQntyApi(request):
    try:
        # request['database'] = "temple"
        # request['collection'] = "offering"
        modulename='QUANTITYLIST'
        request['modulename'] = modulename
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        # print(request['datafrm']['rate_name'])
        datadict={}
        # datadict['rate_name'] = request['datafrm']['rate_name']
        datadict['qnty_amount'] = request['datafrm']['qnty']
        datadict['qty_templeid'] = request['datafrm']['templeid']
        # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
        # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
        datadict['createdat'] = str(datetime.now())
        countdocs = dbmodules.qnty({},datadict,"c","qnty")
        datadict['qnty_id'] = int(countdocs) + 1
        datadict['status'] = 1
        print("Datadict*************",datadict)
        datavalue =dbmodules.qnty("",datadict,"i","qnty")
        print("insert",datavalue)
        respdict={}
        respdict['respfrmdb'] = {"response":"Success"}
        respdict['result']="Success"
        # del datadict['_id']
        # print("type------",type(datadict))
        # print("respdict!!!!!!!!!",datadict)
        return respdict
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)
        return str(e)


#USER
#=========================================================================
#INDEX
def listTempleCategoryApi(request):
    try:
        dbQuery = {"category_templeid":request['datafrm']['templeid']}
        # modulename='LISTHISTORY'
        # request['modulename'] = modulename
        datavalue =dbmodules.category(dbQuery, "","l","category")
        print("listed",datavalue)
        datavalue['result'] = "Success"
        return datavalue        
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)
        return str(e)
#CREATE FESTIVAL
def createFestivalApi(request):
    try:
    
        # request['database'] = "temple"
        # request['collection'] = "diety"
        modulename='CREATEFESTIVAL'
        request['modulename'] = modulename
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print(request['datafrm']['festival_name'])
        datadict={}
        datadict['festival_name'] = request['datafrm']['festival_name']
        datadict['festival_oftemp'] = request['datafrm']['festival_oftemp']
        datadict['festival_photo'] = request['datafrm']['festival_photo']
        datadict['festival_descr'] = request['datafrm']['festival_desc']
        datadict['diety_templeid'] = request['datafrm']['templeid']
        datadict['createdat'] = str(datetime.now())
        countdocs = dbmodules.festival({},datadict,"c","festival")
        datadict['diety_id'] = int(countdocs) + 1
        datadict['status'] = 1
        print("Datadict*************",datadict)
        datavalue =dbmodules.festival({},datadict,"i","festival")
        print("insert",datavalue)
        respdict={}
        respdict['respfrmdb'] = {"response":"Success"}
        respdict['result']="Success"
        # del datadict['_id']
        # print("type------",type(datadict))
        # print("respdict!!!!!!!!!",datadict)
        return respdict
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)
        return str(e)

# LIST FESTIVAL

def listFestivalApi(request):
    try:
        dbQuery = {"category_templeid":request['datafrm']['templeid']}
        # modulename='LISTHISTORY'
        # request['modulename'] = modulename
        datavalue =dbmodules.category(dbQuery, "","l","category")
        print("listed",datavalue)
        datavalue['result'] = "Success"
        return datavalue        
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)
        return str(e)



def createStatementApi(request):
    try:
    
        # request['database'] = "temple"
        # request['collection'] = "diety"
        modulename='CREATESTATEMENT'
        request['modulename'] = modulename
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print(request['datafrm']['statement_name'])
        datadict={}
        datadict['statement_name'] = request['datafrm']['festival_name']
        datadict['statement_oftemp'] = request['datafrm']['festival_oftemp']
        datadict['statement_photo'] = request['datafrm']['festival_photo']
        datadict['statement_descr'] = request['datafrm']['festival_desc']
        datadict['diety_templeid'] = request['datafrm']['templeid']
        datadict['createdat'] = str(datetime.now())
        countdocs = dbmodules.statement({},datadict,"c","statement")
        datadict['diety_id'] = int(countdocs) + 1
        datadict['status'] = 1
        print("Datadict*************",datadict)
        datavalue =dbmodules.statement({},datadict,"i","statement")
        print("insert",datavalue)
        respdict={}
        respdict['respfrmdb'] = {"response":"Success"}
        respdict['result']="Success"
        # del datadict['_id']
        # print("type------",type(datadict))
        # print("respdict!!!!!!!!!",datadict)
        return respdict
    except ValueError as e:
        print("EXCEPTION1")
        return str(e)
    except Exception as e:
        print("FAILED")
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)
        return str(e)
