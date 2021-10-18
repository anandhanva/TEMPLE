
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
    # print("UI REQUEST",str(request))
    # print("UI REQUESTtype",type(request))
    # print("UI REQUESTjson",str(request.json))
    # print("UI REQUESTdata",str(request.get_data))
    valdata=validateReq(request)
    #valdata=json.dumps(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(uitobe_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(uitobe_response())

@app.route(baseUrl+'/acc_statement', methods = ['POST'])
def AccStatement():
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


@app.route(baseUrl+'/activity_type', methods = ['POST'])
def Activitytype():
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

@app.route(baseUrl+'/pooldetails', methods = ['POST'])
def Pool_Details():
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


@app.route(baseUrl+'/fundtransfer', methods = ['POST'])
def Fundtransfer():
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

@app.route(baseUrl+'/select_devaswom', methods = ['POST'])
def Select_Devaswom():
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

@app.route(baseUrl+'/select_temple', methods = ['POST'])
def SelectTemple():
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


@app.route(baseUrl+'/requestmoney', methods = ['POST'])
def Requestmoney():
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