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
    #     # request['database'] = "temple"
    #     # request['collection'] = "offering"
    #     modulename='CREATETEMPLE'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.temple({},datadict,"c","temple")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.temple("",datadict,"i","temple")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "templename":"temple1",
            "templedesc":"fagdfgdfg"
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
def listTempleApi(request):
    try:
        dbQuery = {"templeid":request['datafrm']['templeid']}
        # request['database'] = "temple"
        # request['collection'] = "offering"
        # modulename='LISTOFFERINGS'
        # request['modulename'] = modulename
        datavalue =dbmodules.temple(dbQuery,"","l","temple")
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
   

def createTempleAdminApi(request):
    try:
    #     # request['database'] = "temple"
    #     # request['collection'] = "offering"
    #     modulename='CREATETEMPLE'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.temple({},datadict,"c","temple")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.temple("",datadict,"i","temple")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "templeadminname":"templeadmin",
            "templedadminid":"10"
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
    #     # request['database'] = "temple"
    #     # request['collection'] = "offering"
    #     modulename='CREATETEMPLE'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.temple({},datadict,"c","temple")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.temple("",datadict,"i","temple")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "accountnumber":"SBI009",
            "accountdesc":"djvhjfsgfdg"
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
    #     # request['database'] = "temple"
    #     # request['collection'] = "offering"
    #     modulename='CREATETEMPLE'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.temple({},datadict,"c","temple")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.temple("",datadict,"i","temple")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "finadminname":"fin1",
            "finadminid":"12"
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
        datavalue =dbmodules.prasadam("",datadict,"i","prasadam")
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

       #     # request['database'] = "temple"
    #     # request['collection'] = "offering"
    #     modulename='CREATETEMPLE'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.temple({},datadict,"c","temple")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.temple("",datadict,"i","temple")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "accountnumber":"CrStmt",
            "accountdesc":"jhgyhgfg"
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

# LIST STATEMENT

def listStatementsApi(request):
    try:
        dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # modulename='LISTHISTORY'
        # request['modulename'] = modulename
        datavalue =dbmodules.category(dbQuery, "","l","statement")
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

#DROPDOWN ACTIVITY
def drpdwnFinActivityApi(request):
    try:
        dbQuery = {"templeid":request['datafrm']['templeid']}
        # request['database'] = "temple"
        # request['collection'] = "prasadam"
        datavalue =dbmodules.activity({},dbQuery,"l","activity")

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

# CREATE DEVASOM
def createDevasomsApi(request):
    try:

       #     # request['database'] = "temple"
    #     # request['collection'] = "offering"
    #     modulename='CREATETEMPLE'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.temple({},datadict,"c","temple")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.temple("",datadict,"i","temple")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "devasomname":"Devasom1",
            "devasomdesc":"ncjhhdfh"
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

# LIST DEVASOM

def listDevasomsApi(request):
    try:
        dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # modulename='LISTHISTORY'
        # request['modulename'] = modulename
        datavalue =dbmodules.devaswom(dbQuery, "","l","devaswom")
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

#Create Devasom Admin
def createDevasomAdminApi(request):
    try:

       #     # request['database'] = "temple"
    #     # request['collection'] = "offering"
    #     modulename='CREATETEMPLE'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.temple({},datadict,"c","temple")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.temple("",datadict,"i","temple")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "devasomadmin":"DevasomAdmin",
            "devasomlog":"jahsas"
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

#List Devasom Admin
def listDevasomAdminApi(request):
    try:
        dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # modulename='LISTHISTORY'
        # request['modulename'] = modulename
        datavalue =dbmodules.devasomadmin(dbQuery, "","l","devasomadmin")
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


#Create Pool
def createPoolApi(request):
    try:

       #     # request['database'] = "temple"
    #     # request['collection'] = "offering"
    #     modulename='CREATETEMPLE'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.temple({},datadict,"c","temple")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.temple("",datadict,"i","temple")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "createpool":"pool1",
            "poolpass":"hasj"
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


#List Pool
def listPoolApi(request):
    try:
        dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # modulename='LISTHISTORY'
        # request['modulename'] = modulename
        datavalue =dbmodules.pool(dbQuery, "","l","bpool")
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

#Create Pool
def createFundTransferApi(request):
    try:

       #     # request['database'] = "temple"
    #     # request['collection'] = "offering"
    #     modulename='CREATETEMPLE'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.temple({},datadict,"c","temple")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.temple("",datadict,"i","temple")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "createfundtransfer":"fund1",
            "fundpass":"ahgsh"
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

#List Fund Transfer
def listFundTransferApi(request):
    try:
        dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # modulename='LISTHISTORY'
        # request['modulename'] = modulename
        datavalue =dbmodules.fund(dbQuery, "","l","bfund")
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

#Create Bank Details
def createBankApi(request):
    try:

       #     # request['database'] = "temple"
    #     # request['collection'] = "offering"
    #     modulename='CREATETEMPLE'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.temple({},datadict,"c","temple")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.temple("",datadict,"i","temple")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "createbankdetails":"bank1",
            "bankpass":"anbsahg"
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


#List Bank Details
def listBankDetailsApi(request):
    try:
        dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # modulename='LISTHISTORY'
        # request['modulename'] = modulename
        datavalue =dbmodules.bank(dbQuery, "","l","bank")
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

#Create Bank Admin
def createBankAdminApi(request):
    try:

       #     # request['database'] = "temple"
    #     # request['collection'] = "offering"
    #     modulename='CREATETEMPLE'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.temple({},datadict,"c","temple")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.temple("",datadict,"i","temple")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "createbankadmin":"admin1",
            "adminpass":"admin"
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

#List Bank Admin
def listBankAdminApi(request):
    try:
        dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # modulename='LISTHISTORY'
        # request['modulename'] = modulename
        datavalue =dbmodules.bankadmin(dbQuery, "","l","bankadmin")
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

def createCardApi(request):
    try:

       #     # request['database'] = "temple"
    #     # request['collection'] = "offering"
    #     modulename='CREATETEMPLE'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.temple({},datadict,"c","temple")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.temple("",datadict,"i","temple")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "cardnumber":"980",
            "name":"rfyrgh"
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




#LIST CARD APPLICATION
def listCardApplicationsApi(request):
    try:
        dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # modulename='LISTHISTORY'
        # request['modulename'] = modulename
        datavalue =dbmodules.card(dbQuery, "","l","card")
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


def createTransactionDevaswomsApi(request):
    try:

       #     # request['database'] = "temple"
    #     # request['collection'] = "offering"
    #     modulename='CREATETEMPLE'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.temple({},datadict,"c","temple")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.temple("",datadict,"i","temple")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "transactionname":"transactio1",
            "name":"ncsjnj"
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



#LIST TRANSACTION DEVASWOM
def listTransactionsDevaswomsApi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # # modulename='LISTHISTORY'
        # # request['modulename'] = modulename
        # datavalue =dbmodules.transactionDevaswom(dbQuery, "","l","card")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "transactionname":"transactio1",
            "name":"ncsjnj"
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
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)

# DROPDOWN BANK    
def drpdwnBankApi(request):
    try:
        dbQuery = {"bank_templeid":request['datafrm']['templeid']}
        # request['database'] = "temple"
        # request['collection'] = "diety"
        # modulename="DROPDOWNDIETY"
        # request['modulename']=modulename
        datavalue =dbmodules.bank({},dbQuery,"l","bank")
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

# DROPDOWN TEMPLE    
def drpdwnTempleApi(request):
    try:
        dbQuery = {"bank_templeid":request['datafrm']['templeid']}
        # request['database'] = "temple"
        # request['collection'] = "diety"
        # modulename="DROPDOWNDIETY"
        # request['modulename']=modulename
        datavalue =dbmodules.bank({},dbQuery,"l","bank")
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

# DROPDOWN IFSC   
def drpdwnIFSCApi(request):
    try:
        dbQuery = {"bank_templeid":request['datafrm']['templeid']}
        # request['database'] = "temple"
        # request['collection'] = "diety"
        # modulename="DROPDOWNDIETY"
        # request['modulename']=modulename
        datavalue =dbmodules.bank({},dbQuery,"l","bank")
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

#LIST FINANCE ACTIVITY
def listFinActivityApi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # # modulename='LISTHISTORY'
        # # request['modulename'] = modulename
        # datavalue =dbmodules.activity(dbQuery, "","l","activity")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "financetype":"goldloan",
            "name":"Hlk"
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
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)

#CREATE RECONCILIATION
def createReconciliationApi(request):
    try:

       #     # request['database'] = "temple"
    #     # request['collection'] = "reconciliation"
    #     modulename='CREATETEMPLE'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.temple({},datadict,"c","temple")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.temple("",datadict,"i","temple")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "reconciliationtype":"reconcilaition2",
            "rename":"type2"
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

#LIST RECONCILIATION ACTIVITY
def listReconciliationApi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # # modulename='LISTHISTORY'
        # # request['modulename'] = modulename
        # datavalue =dbmodules.reconsiliation(dbQuery, "","l","recon")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "reconciliationtype":"re1",
            "rename":"standard"
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
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)

#CREATE REQUEST MONEY
def createRequestMoneyApi(request):
    try:

       #     # request['database'] = "temple"
    #     # request['collection'] = "reqmoney"
    #     modulename='CREATETEMPLE'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.temple({},datadict,"c","temple")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.temple("",datadict,"i","temple")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "getreqmoneytype":"reconcilaition2",
            "getrmoney":"money1"
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

# DROPDOWN DEVASWOM
def dropdownDevaswomApi(request):
    try:
        dbQuery = {"bank_templeid":request['datafrm']['templeid']}
        # request['database'] = "temple"
        # request['collection'] = "devaswom"
        # modulename="DROPDOWNDEVASWOM"
        # request['modulename']=modulename
        datavalue =dbmodules.devaswom({},dbQuery,"l","bank")
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

# SUPER ADMIN
#CREATE REQUEST MONEY
def createLordsApi(request):
    try:

       #     # request['database'] = "temple"
    #     # request['collection'] = "lords"
    #     modulename='CREATELORDS'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.temple({},datadict,"c","temple")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.temple("",datadict,"i","temple")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "lordname":"shiva",
            "lordtype":"jags"
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

#LIST LORDS
def listLordsApi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # # modulename='LISTLORD'
        # # request['modulename'] = modulename
        # datavalue =dbmodules.lords(dbQuery, "","l","lords")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "lordname":"shiva",
            "lordtlist":"5"
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
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)

def createForgotPinApi(request):
    try:

       #     # request['database'] = "temple"
    #     # request['collection'] = "forgotpin"
    #     modulename='CREATETEMPLE'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.temple({},datadict,"c","temple")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.temple("",datadict,"i","temple")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "pinumber":"980",
            "acholdername":"jason"
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

def getTransactionDevaswomApi(request):
    try:

       #     # request['database'] = "temple"
    #     # request['collection'] = "devaswom"
    #     modulename='CREATETEMPLE'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.temple({},datadict,"c","temple")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.temple("",datadict,"i","temple")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "date":"6/9/21",
            "transaction":"5"
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

def getTransactionBankApi(request):
    try:

       #     # request['database'] = "temple"
    #     # request['collection'] = "bank"
    #     modulename='CREATETEMPLE'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.temple({},datadict,"c","temple")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.temple("",datadict,"i","temple")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "date":"10/10/2021",
            "transaction":"10"
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

#LIST BANK
def listTransactionBankApi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # # modulename='LISTLORD'
        # # request['modulename'] = modulename
        # datavalue =dbmodules.bank(dbQuery, "","l","bank")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "list":"banklist",
            "banklist":"20"
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
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)

def getTransactionTempleApi(request):
    try:

       #     # request['database'] = "temple"
    #     # request['collection'] = "templetra"
    #     modulename='CREATETEMPLE'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.temple({},datadict,"c","temple")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.temple("",datadict,"i","temple")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "date":"15/10/2021",
            "templtrans":"20"
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

#LIST TRANSACTION TEMPLE
def listTransactionTempleApi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # # modulename='LISTLORD'
        # # request['modulename'] = modulename
        # datavalue =dbmodules.templetra(dbQuery, "","l","templetra")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "templtra":"listtrans",
            "templelist":"05"
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
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)

def createBlockTempleApi(request):
    try:

       #     # request['database'] = "temple"
    #     # request['collection'] = "block"
    #     modulename='CREATETEMPLE'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.temple({},datadict,"c","temple")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.block("",datadict,"i","block")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "blocktemp":"tempname",
            "reason":"reason"
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

#LIST BLOCK TEMPLE
def listBlockTempleApi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # # modulename='LISTLORD'
        # # request['modulename'] = modulename
        # datavalue =dbmodules.block(dbQuery, "","l","block")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "blocklist":"blocklist1",
            "blocktype":"blocktype"
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
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)

def createBlockDevaswomApi(request):
    try:

       #     # request['database'] = "temple"
    #     # request['collection'] = "block"
    #     modulename='CREATETEMPLE'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.temple({},datadict,"c","temple")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.block("",datadict,"i","block")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "blockdevaswom":"devaswomname",
            "reason":"reason"
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

#LIST BLOCK DEVASWOM
def listBlockDevaswomApi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # # modulename='LISTLORD'
        # # request['modulename'] = modulename
        # datavalue =dbmodules.block(dbQuery, "","l","block")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "blocklist":"blocklist2",
            "blocktype":"blocktype"
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
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)

def createBlockCustomerApi(request):
    try:

       #     # request['database'] = "temple"
    #     # request['collection'] = "block"
    #     modulename='CREATETEMPLE'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.temple({},datadict,"c","temple")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.block("",datadict,"i","block")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "blockcustomer":"customername",
            "reason":"reason"
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

#LIST BLOCK CUSTOMER
def listBlockCustomerApi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # # modulename='LISTLORD'
        # # request['modulename'] = modulename
        # datavalue =dbmodules.block(dbQuery, "","l","block")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "blocklist":"blocklist3",
            "blocktype":"customer"
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
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)

def createBlockCardApi(request):
    try:

       #     # request['database'] = "temple"
    #     # request['collection'] = "block"
    #     modulename='CREATETEMPLE'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.temple({},datadict,"c","temple")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.block("",datadict,"i","block")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "blockcard":"cardname",
            "type":"card"
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

#LIST BLOCK CARD
def listBlockCardApi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # # modulename='LISTLORD'
        # # request['modulename'] = modulename
        # datavalue =dbmodules.block(dbQuery, "","l","block")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "blocklist":"blocklist3",
            "blocktype":"card"
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
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)

def createBlockBankApi(request):
    try:

       #     # request['database'] = "temple"
    #     # request['collection'] = "block"
    #     modulename='CREATETEMPLE'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.temple({},datadict,"c","temple")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.block("",datadict,"i","block")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "blockbank":"bankname",
            "type":"bank1"
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

#LIST BLOCK BANK
def listBlockBankApi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # # modulename='LISTLORD'
        # # request['modulename'] = modulename
        # datavalue =dbmodules.block(dbQuery, "","l","block")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "blocklist":"blocklist4",
            "blocktype":"bank"
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
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)

#LIST TRANSACTION DEVASWOM
def superListTransDevaApi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # # modulename='LISTLORD'
        # # request['modulename'] = modulename
        # datavalue =dbmodules.devaswom(dbQuery, "","l","devaswom")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "translist":"list3",
            "transtype":"bank"
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
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)

#LIST ACCOUNT STATEMENT
def listAcctStatmeentApi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # # modulename=''
        # # request['modulename'] = modulename
        # datavalue =dbmodules.bank(dbQuery, "","l","bank")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "acctstatement":"statement1",
            "statementtype":"daily"
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
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)

# DROPDOWN ACTVITIES   
def dropdownActivityTypeApi(request):
    try:
        #dbQuery = {"diety_templeid":request['datafrm']['templeid']}
        # request['database'] = "temple"
        # request['collection'] = "diety"
        # modulename="DROPDOWNDIETY"
        # request['modulename']=modulename
        #datavalue =dbmodules.diety({},dbQuery,"l","diety")
        # print("listed",datavalue)
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "activity":"activity1",
            "activitytype":"daily"
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
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)
        return str(e)

# DROPDOWN ACTVITIES   
def superDropDownDevaswomApi(request):
    try:
        #dbQuery = {"diety_templeid":request['datafrm']['templeid']}
        # request['database'] = "temple"
        # request['collection'] = "diety"
        # modulename="DROPDOWNDIETY"
        # request['modulename']=modulename
        #datavalue =dbmodules.diety({},dbQuery,"l","diety")
        # print("listed",datavalue)
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "devaswomdrop":"drop1",
            "devaswomtype":"set1"
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
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)
        return str(e)

# DROPDOWN ACTVITIES   
def superDropDownTempleApi(request):
    try:
        #dbQuery = {"diety_templeid":request['datafrm']['templeid']}
        # request['database'] = "temple"
        # request['collection'] = "diety"
        # modulename="DROPDOWNDIETY"
        # request['modulename']=modulename
        #datavalue =dbmodules.diety({},dbQuery,"l","diety")
        # print("listed",datavalue)
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "templedrop":"drop2",
            "templetype":"set1"
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
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)
        return str(e)

def createSuperPoojaApi(request):
    try:

       #     # request['database'] = "temple"
    #     # request['collection'] = "pooja"
    #     modulename='CREATESUPERPOOJA'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.temple({},datadict,"c","temple")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.block("",datadict,"i","block")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "pooja":"poojaname",
            "type":"pooja1"
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

#LIST POOJA
def listSuperPoojaApi(request):
    try:
        # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
        # # modulename=''
        # # request['modulename'] = modulename
        # datavalue =dbmodules.pooja(dbQuery, "","l","pooja")
        # print("listed",datavalue)
        # datavalue['result'] = "Success"
        # return datavalue 
        print("REQUEST########",request)
        dict={
            "poojaname":"pooja1",
            "poojalist":"list"
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
        print("FAILED",str(e))
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            fname,lineno,fn,text = frame
            print( "Error in %s on line %d", fname, lineno)

# def createSuperAccountApi(request):
#     try:

#        #     # request['database'] = "temple"
#     #     # request['collection'] = "bank"
#     #     modulename='CREATESUPERPOOJA'
#     #     request['modulename'] = modulename
#     #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
#     #     # print(request['datafrm']['offering_name'])
#     #     datadict={}
#     #     datadict['temple_name'] = request['datafrm']['offering_name']
#     #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
#     #     datadict['offering_descr'] = request['datafrm']['offering_description']
#     #     datadict['offering_templeid'] = request['datafrm']['templeid']
#     #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
#     #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
#     #     datadict['createdat'] = str(datetime.now())
#     #     countdocs = dbmodules.temple({},datadict,"c","temple")
#     #     datadict['offering_id'] = int(countdocs) + 1
#     #     datadict['status'] = 1
#     #     print("Datadict*************",datadict)
#     #     datavalue =dbmodules.bank("",datadict,"i","bank")
#     #     print("insert",datavalue)
#     #     respdict={}
#     #     respdict['respfrmdb'] = {"response":"Success"}
#     #     respdict['result']="Success"
#     #     # del datadict['_id']
#     #     # print("type------",type(datadict))
#     #     # print("respdict!!!!!!!!!",datadict)
#     #     return respdict
#     # except ValueError as e:
#     #     print("EXCEPTION1")
#     #     return str(e)
#     # except Exception as e:
#     #     print("FAILED")
#     #     for frame in traceback.extract_tb(sys.exc_info()[2]):
#     #         fname,lineno,fn,text = frame
#     #         print( "Error in %s on line %d", fname, lineno)
#     #     return str(e)
#         print("REQUEST########",request)
#         dict={
#             "pooja":"poojaname",
#             "type":"pooja1"
#         }
#         print("dict***",dict)
#         respdict={}
#         respdict["respfrmdb"]=dict
#         respdict["result"]="Success"
#         return respdict
#     except ValueError as e:
#         print("EXCEPTION1")
#         return str(e)
#     except Exception as e:
#         print("FAILED")
#         # for frame in traceback.extract_tb(sys.exc_info()[2]):
#         #     fname,lineno,fn,text = frame
#         #     print( "Error in %s on line %d", fname, lineno)
#         return str(e)

# #LIST POOJA
# def listSuperPoojaApi(request):
#     try:
#         # dbQuery = {"statement_templeid":request['datafrm']['templeid']}
#         # # modulename=''
#         # # request['modulename'] = modulename
#         # datavalue =dbmodules.pooja(dbQuery, "","l","pooja")
#         # print("listed",datavalue)
#         # datavalue['result'] = "Success"
#         # return datavalue 
#         print("REQUEST########",request)
#         dict={
#             "poojaname":"pooja1",
#             "poojalist":"list"
#         }
#         print("dict***",dict)
#         respdict={}
#         respdict["respfrmdb"]=dict
#         respdict["result"]="Success"
#         return respdict       
#     except ValueError as e:
#         print("EXCEPTION1")
#         return str(e)
#     except Exception as e:
#         print("FAILED",str(e))
#         for frame in traceback.extract_tb(sys.exc_info()[2]):
#             fname,lineno,fn,text = frame
#             print( "Error in %s on line %d", fname, lineno)

def createSuperDevaswomApi(request):
    try:

       #     # request['database'] = "temple"
    #     # request['collection'] = "pooja"
    #     modulename='CREATESUPERPOOJA'
    #     request['modulename'] = modulename
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     # print(request['datafrm']['offering_name'])
    #     datadict={}
    #     datadict['temple_name'] = request['datafrm']['offering_name']
    #     datadict['offering_rateid'] = request['datafrm']['offering_rateid']
    #     datadict['offering_descr'] = request['datafrm']['offering_description']
    #     datadict['offering_templeid'] = request['datafrm']['templeid']
    #     # datadict['diety_name'] = getDietyName(request['datafrm']['deity'])
    #     # datadict['amount'] = getAmoutName(request['datafrm']['offering_rateid'])
    #     datadict['createdat'] = str(datetime.now())
    #     countdocs = dbmodules.temple({},datadict,"c","temple")
    #     datadict['offering_id'] = int(countdocs) + 1
    #     datadict['status'] = 1
    #     print("Datadict*************",datadict)
    #     datavalue =dbmodules.block("",datadict,"i","block")
    #     print("insert",datavalue)
    #     respdict={}
    #     respdict['respfrmdb'] = {"response":"Success"}
    #     respdict['result']="Success"
    #     # del datadict['_id']
    #     # print("type------",type(datadict))
    #     # print("respdict!!!!!!!!!",datadict)
    #     return respdict
    # except ValueError as e:
    #     print("EXCEPTION1")
    #     return str(e)
    # except Exception as e:
    #     print("FAILED")
    #     for frame in traceback.extract_tb(sys.exc_info()[2]):
    #         fname,lineno,fn,text = frame
    #         print( "Error in %s on line %d", fname, lineno)
    #     return str(e)
        print("REQUEST########",request)
        dict={
            "pooja":"poojaname",
            "type":"pooja1"
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
