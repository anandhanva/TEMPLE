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

baseUrl="/android"

@app.route('/', methods=['POST','GET'])
def base():
    return responses.upGetResponse()

#USER APIS

#USER LOGIN
@app.route(urlconstants.ENDPOINT+'/login', methods = ['POST'])
def login():
    
    return bllayer.processLoginRequest(request.json)

#USER OTPVERIFICATION
@app.route(urlconstants.ENDPOINT+'/otpverification', methods = ['POST'])
def otpverification():
    
    return bllayer.processOtpVerificationt(request.json)