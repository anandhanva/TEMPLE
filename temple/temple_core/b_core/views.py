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
    
    # Check User credentials and perform login operation
    return bllayer.processLoginRequest(request)


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

