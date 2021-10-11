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
