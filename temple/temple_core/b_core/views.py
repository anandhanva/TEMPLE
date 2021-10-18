from flask.globals import request, session
from flask.wrappers import Request
from flask import Response
import requests
from b_core import app
import json
from b_core.statics import urlconstants
from b_core.platformlayers import bllayer, constantslayer
from b_core.responsemaster import responses



baseUrl="/api/v1/temple/"

@app.route('/', methods=['POST','GET'])
def base():
    return responses.upGetResponse()

# USER APIS
# USER LOGIN
@app.route(urlconstants.ENDPOINT+'/user', methods = ['POST'])
def user():
    print("Request from UI: ", request.json)
    # Check User credentials and perform login operation
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

#TEMPLE ADMIN
#CREATE POOJA
@app.route(urlconstants.ENDPOINT+'/create_pooja', methods = ['POST'])
def addpooja():
    
    return bllayer.createPooja(request)

#LIST POOJA
@app.route(urlconstants.ENDPOINT+'/list_pooja', methods = ['POST'])
def listpooja():
    
    return bllayer.listPooja(request)

#CREATE PRASADAM
@app.route(urlconstants.ENDPOINT+'/create_prasadam', methods = ['POST'])
def addprasadam():
    
    return bllayer.createPrasadam(request)

#LIST PRASADAM
@app.route(urlconstants.ENDPOINT+'/list_prasadam', methods = ['POST'])
def listprasadam():
    
    return bllayer.listPrasadam(request)

#CREATE OFFERINGS
@app.route(urlconstants.ENDPOINT+'/create_offerings', methods = ['POST'])
def addofferings():
    
    return bllayer.createOfferings(request)

#LIST OFFERINGS
@app.route(urlconstants.ENDPOINT+'/list_offerings', methods = ['POST'])
def listofferings():
    
    return bllayer.listOfferings(request)

#CREATE DIETY
@app.route(urlconstants.ENDPOINT+'/create_diety', methods = ['POST'])
def adddiety():
    
    return bllayer.createDiety(request)

#LIST DIETY
@app.route(urlconstants.ENDPOINT+'/list_diety', methods = ['POST'])
def listdiety():
    
    return bllayer.listDiety(request)

#CREATE HISTORY
@app.route(urlconstants.ENDPOINT+'/create_history', methods = ['POST'])
def addhistory():
    
    return bllayer.createHistory(request)

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

