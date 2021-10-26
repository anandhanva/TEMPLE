from flask.globals import request, session
from flask.wrappers import Request
from flask import Response
import requests
from b_core import app
import json
from b_core.statics import urlconstants,staticfunctions
from b_core.platformlayers import bllayer, constantslayer,qrmanage
from b_core.responsemaster import responses
# from temple.temple_core.b_core.statics.staticfunctions import coretobe_response
from flask.json import jsonify




baseUrl="/api/v1/temple/"

@app.route('/', methods=['POST','GET'])
def base():
    return responses.upGetResponse()

# USER APIS
# USER LOGIN
@app.route(urlconstants.ENDPOINT+'/user', methods = ['POST'])
def user():
    
    return bllayer.processLoginRequest(request.json)

@app.route(urlconstants.ENDPOINT+'/ac', methods = ['POST'])
def ac():
    
    # Check User credentials and perform login operation
    return bllayer.accstmtfrmdb(request)



# ADD TEMPLE
@app.route(urlconstants.ENDPOINT+'/add_temple', methods = ['POST'])
def addtemple():
    
    return bllayer.addTemple(request)
# LIST TEMPLE
@app.route(urlconstants.ENDPOINT+'/list_temple', methods = ['POST'])
def listtemple():
    
    return bllayer.listTempleApi(request)

# CREATE TEMPLE ADMIN
@app.route(urlconstants.ENDPOINT+'/createtemple_admin', methods = ['POST'])
def createtempleadmin():
    
    return bllayer.createTempleAdmin(request)

# LIST TEMPLE ADMIN
@app.route(urlconstants.ENDPOINT+'/listtemple_admin', methods = ['POST'])
def listtempleadmin():
    
    return bllayer.listTempleAdminApi(request)

# CREATE ACCOUNT
@app.route(urlconstants.ENDPOINT+'/create_account', methods = ['POST'])
def addaccount():
    
    return bllayer.createAccount(request)


# LIST ACCOUNT
@app.route(urlconstants.ENDPOINT+'/list_account', methods = ['POST'])
def listaccount():
    
    return bllayer.listAccountApi(request)



# CREATE FIN ADMIN
@app.route(urlconstants.ENDPOINT+'/add_finadmin', methods = ['POST'])
def createfinadmins():
    
    return bllayer.createFinAdmin(request)
#TEMPLE ADMIN
#CREATE POOJA
@app.route(urlconstants.ENDPOINT+'/create_pooja', methods = ['POST'])
def addpooja():
    
    return bllayer.createPooja(request.json)

#LIST POOJA
@app.route(urlconstants.ENDPOINT+'/list_pooja', methods = ['POST'])
def listpooja():
    
    return bllayer.listPooja(request.json)

#CREATE PRASADAM
@app.route(urlconstants.ENDPOINT+'/create_prasadam', methods = ['POST'])
def addprasadam():
    
    return bllayer.createPrasadam(request.json)

#LIST PRASADAM
@app.route(urlconstants.ENDPOINT+'/list_prasadam', methods = ['POST'])
def listprasadam():
    
    return bllayer.listPrasadam(request)

#CREATE OFFERINGS
@app.route(urlconstants.ENDPOINT+'/create_offerings', methods = ['POST'])
def addofferings():
    
    return bllayer.createOfferings(request.json)

#LIST OFFERINGS
@app.route(urlconstants.ENDPOINT+'/list_offerings', methods = ['POST'])
def listofferings():
    
    return bllayer.listOfferings(request)

#CREATE DIETY
@app.route(urlconstants.ENDPOINT+'/create_diety', methods = ['POST'])
def adddiety():
    
    return bllayer.createDiety(request.json)

#LIST DIETY
@app.route(urlconstants.ENDPOINT+'/list_diety', methods = ['POST'])
def listdiety():
    
    return bllayer.listDiety(request)

#CREATE HISTORY
@app.route(urlconstants.ENDPOINT+'/create_history', methods = ['POST'])
def addhistory():
    
    return bllayer.createHistory(request.json)

#LIST HISTORY
@app.route(urlconstants.ENDPOINT+'/list_history', methods = ['POST'])
def listhistory():
    
    return bllayer.listHistory(request)

#CREATE STAY
@app.route(urlconstants.ENDPOINT+'/create_stay', methods = ['POST'])
def addstay():
    
    return bllayer.createstay(request)

#LIST STAY
@app.route(urlconstants.ENDPOINT+'/list_stay', methods = ['POST'])
def liststay():
    
    return bllayer.listStay(request)

#CREATE FESTIVAL
@app.route(urlconstants.ENDPOINT+'/create_festival', methods = ['POST'])
def addfestival():
    
    return bllayer.createFestival(request)

#LIST FESTIVAL
@app.route(urlconstants.ENDPOINT+'/list_festival', methods = ['POST'])
def listfestival():
    
    return bllayer.listFestival(request)

# DROPDOWN - -DIETY

@app.route(urlconstants.ENDPOINT+'/dropdown_diety', methods = ['POST'])
def dropDiety():
    
    return bllayer.dropdownDietyApi(request)


# DROPDOWN - -RATE

@app.route(urlconstants.ENDPOINT+'/dropdown_rate', methods = ['POST'])
def dropRate():
    
    return bllayer.dropdownRateApi(request)

#DROPDOWN - - QTY
@app.route(urlconstants.ENDPOINT+'/dropdown_qty', methods = ['POST'])
def dropQty():
    
    return bllayer.dropdownPrasadamQtyApi(request)

#CREATE KANIKKA
@app.route(urlconstants.ENDPOINT+'/create_kanikka', methods = ['POST'])
def createKanikka():
    
    return bllayer.createKanikkaApi(request.json)
#CREATE AIRPORT
@app.route(urlconstants.ENDPOINT+'/add_airport', methods = ['POST'])
def addAirport():
    
    return bllayer.addAirportApi(request.json)

#CREATE RATE
@app.route(urlconstants.ENDPOINT+'/add_rate', methods = ['POST'])
def addRate():
    
    return bllayer.addRateApi(request.json)

#CREATE QUANTITY
@app.route(urlconstants.ENDPOINT+'/add_quantity', methods = ['POST'])
def addQnty():
    
    return bllayer.addQntyApi(request.json)


#USER
#=============================================================================
#INDEX
@app.route(urlconstants.ENDPOINT+'/user_index', methods = ['POST'])
def userIndex():
    
    return bllayer.userIndexApi(request.json)


#GET KANIKKA BY DIETYID
@app.route(urlconstants.ENDPOINT+'/kanikka_bydietyid', methods = ['POST'])
def kanikkaByDietyid():
    
    return bllayer.kanikkaByDietyidApi(request.json)



#GET OFFERING BY TEMPLEID
@app.route(urlconstants.ENDPOINT+'/offering_bytempleid', methods = ['POST'])
def offeringByTempleid():
    
    return bllayer.offeringByTempleidApi(request)

#GET OFFERING BY DIETYID
@app.route(urlconstants.ENDPOINT+'/offering_bydietyid', methods = ['POST'])
def offeringByDietyid():
    
    return bllayer.offeringByDietyidApi(request)


#GET PRASADAM BY TEMPLEID
@app.route(urlconstants.ENDPOINT+'/prasadam_bytempleid', methods = ['POST'])
def prasadamByTempleid():
    
    return bllayer.prasadamByTempleidApi(request)

#GET POOJA BY TEMPLEID
@app.route(urlconstants.ENDPOINT+'/diety_bytempleid', methods = ['POST'])
def dietyjaByTempleid():
    
    return bllayer.dietyByTempleidApi(request)



#CREATE CATEGORY
@app.route(urlconstants.ENDPOINT+'/create_category', methods = ['POST'])
def createCategory():
    
    return bllayer.createCategoryApi(request)

#LIST CATEGORY
@app.route(urlconstants.ENDPOINT+'/list_category', methods = ['POST'])
def listCategory():
    
    return bllayer.listCategoryApi(request)



#=====================================================================
#QR

#CREATE QR
@app.route(urlconstants.ENDPOINT+'/createqr', methods = ['POST'])
def qrGen():
    return bllayer.createQR(request)


#READ QR
@app.route(urlconstants.ENDPOINT+'/rdqrdata', methods = ['POST'])
def rdQr():
    return bllayer.rdQRdata(request)

