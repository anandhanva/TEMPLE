
from flask.globals import session
from flask.json import jsonify
from flask.wrappers import Request
from flask import Response,request
from b_end import app
import json
from b_end.platformlayers import constantslayer
from b_end.responsemaster import responses
from b_end.statics.staticfunctions import uitobe_response, validateReq
from flask_cors import CORS
baseUrl = '/api/v1/temple'
@app.route('/', methods=['POST','GET'])
def base():
    return responses.upGetResponse(request)
# USER APIS
# USER LOGIN
@app.route(baseUrl+'/login', methods = ['POST'])
def user():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(uitobe_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(uitobe_response())
