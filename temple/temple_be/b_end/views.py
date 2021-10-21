import datetime
from logging import exception
from flask.globals import session
from flask.json import jsonify
from flask.wrappers import Request
from flask import Response,request
from b_end import app
import json
import ast
from b_end.platformlayers import constantslayer
from b_end.responsemaster import responses
from b_end.statics.staticfunctions import betoui_response, validateReq
from flask_cors import CORS

baseUrl = '/api/v1/temple'


@app.route('/', methods=['POST','GET'])
def base():
    return responses.upGetResponse(request)
# USER APIS
# USER LOGIN
@app.route(baseUrl+'/login', methods = ['POST'])
def user():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    print("UI REQUESTtype------------------------>",type(req))
    print("UI REQUEST ---",req )
    # print("UI REQUESTjson",str(request.json))
    # print("UI REQUESTdata",str(request.get_data))
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    print(">>>>>>>>>>>>>>>>>>>>>>",type(valdata))
    print(">>>>>>>>valdata",valdata)
    
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(req)
        print("checklog data is",checklog)
        if(isinstance(checklog, str)):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp'] = "SUCCESS"
        if(checklog['resp'] and checklog['resp']!='ERROR' or checklog['resp_type'] == "SUCCESS"):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp_type']=="SUCCESS"
            return jsonify(checklog)
        else:
            respn = {}
            respn['resp_type']="FAIL"
            respn['resp_code']="0"
            respn['message']="Request Failed Due to Unknown Error"
            respn['requestdata']="Error Captured during execution"
            respn['em_reqid']=req["em_reqid"]
            respn['timestamp']=str(datetime.datetime.now())
            respn['em_custid']=req["em_custid"]
            respn['resp_frm_yesb']=""
            respn['resp_frm_ewire']="Error Captured during execution"
            return jsonify(respn)    
    else:
        req['resp_type']="FAIL"
        req['resp_code']=0
        req['message']="Request Failed Due to Unknown Error"
        req['responsedata']="Error Captured during execution"
        return jsonify(req)




#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#USER API

#index

@app.route(baseUrl+'/index', methods = ['POST'])
def user_index():
    req = request.json
    print(">>>>>>>>>>>",req)
    rqJson = json.dumps(req)
    print("ASSSSasssdf",rqJson)
    req = ast.literal_eval(rqJson)
    print("ASSSSasssdf",req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    print("valdata>>>>>>>>>>>>>>>>>>>>>>>>>>>>//////////",valdata)
    
    
    if(valdata['status']==200):
        print("pppppppppppppppppppppppppppppppp>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        checklog=constantslayer.index(req)
        print("checklog data is???????????????????????????",checklog)
        if(isinstance(checklog, str)):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp'] = "SUCCESS"
        if(checklog['resp'] and checklog['resp']!='ERROR' or checklog['resp_type'] == "SUCCESS"):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp_type']=="SUCCESS"
            return jsonify(checklog)
        else:
            respn = {}
            respn['resp_type']="FAIL"
            respn['resp_code']="0"
            respn['message']="Request Failed Due to Unknown Error"
            respn['requestdata']="Error Captured during execution"
            respn['em_reqid']=req["em_reqid"]
            respn['timestamp']=str(datetime.datetime.now())
            respn['em_custid']=req["em_custid"]
            respn['resp_frm_yesb']=""
            respn['resp_frm_ewire']="Error Captured during execution"
            return jsonify(respn)
    else:
        req['resp_type']="FAIL"
        req['resp_code']=0
        req['message']="Request Failed Due to Unknown Error"
        req['responsedata']="Error Captured during execution"
        return jsonify(req)

#user kanikka
@app.route(baseUrl+'/user_kanikka', methods = ['POST'])
def user_kanikka():
    req = request.json
    rqJson = json.dumps(req)
    req = ast.literal_eval(rqJson)
    req = constantslayer.convinptodict(rqJson)
    valdata=validateReq(req)
    
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.userkanikka(req)
        print("checklog data is",checklog)
        if(isinstance(checklog, str)):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp'] = "SUCCESS"
        if(checklog['resp'] and checklog['resp']!='ERROR' or checklog['resp_type'] == "SUCCESS"):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp_type']=="SUCCESS"
            return jsonify(checklog)
        else:
            respn = {}
            respn['resp_type']="FAIL"
            respn['resp_code']="0"
            respn['message']="Request Failed Due to Unknown Error"
            respn['requestdata']="Error Captured during execution"
            respn['em_reqid']=req["em_reqid"]
            respn['timestamp']=str(datetime.datetime.now())
            respn['em_custid']=req["em_custid"]
            respn['resp_frm_yesb']=""
            respn['resp_frm_ewire']="Error Captured during execution"
            return jsonify(respn)
    else:
        req['resp_type']="FAIL"
        req['resp_code']=0
        req['message']="Request Failed Due to Unknown Error"
        req['responsedata']="Error Captured during execution"
        return jsonify(req)

#get_star drop
@app.route(baseUrl+'/get_stardrop', methods = ['POST'])
def getstardrop():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.getstar(req)
        print("checklog data is",checklog)
        if(isinstance(checklog, str)):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp'] = "SUCCESS"
        if(checklog['resp'] and checklog['resp']!='ERROR' or checklog['resp_type'] == "SUCCESS"):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp_type']=="SUCCESS"
            return jsonify(checklog)
        else:
            respn = {}
            respn['resp_type']="FAIL"
            respn['resp_code']="0"
            respn['message']="Request Failed Due to Unknown Error"
            respn['requestdata']="Error Captured during execution"
            respn['em_reqid']=req["em_reqid"]
            respn['timestamp']=str(datetime.datetime.now())
            respn['em_custid']=req["em_custid"]
            respn['resp_frm_yesb']=""
            respn['resp_frm_ewire']="Error Captured during execution"
            return jsonify(respn)
    else:
        req['resp_type']="FAIL"
        req['resp_code']=0
        req['message']="Request Failed Due to Unknown Error"
        req['responsedata']="Error Captured during execution"
        return jsonify(req)


#get_prasadam_bill_list
@app.route(baseUrl+'/get_prasadambill', methods = ['POST'])
def getprasadambill():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.getprsdmbilllst(req)
        print("checklog data is",checklog)
        if(isinstance(checklog, str)):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp'] = "SUCCESS"
        if(checklog['resp'] and checklog['resp']!='ERROR' or checklog['resp_type'] == "SUCCESS"):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp_type']=="SUCCESS"
            return jsonify(checklog)
        else:
            respn = {}
            respn['resp_type']="FAIL"
            respn['resp_code']="0"
            respn['message']="Request Failed Due to Unknown Error"
            respn['requestdata']="Error Captured during execution"
            respn['em_reqid']=req["em_reqid"]
            respn['timestamp']=str(datetime.datetime.now())
            respn['em_custid']=req["em_custid"]
            respn['resp_frm_yesb']=""
            respn['resp_frm_ewire']="Error Captured during execution"
            return jsonify(respn)
    else:
        req['resp_type']="FAIL"
        req['resp_code']=0
        req['message']="Request Failed Due to Unknown Error"
        req['responsedata']="Error Captured during execution"
        return jsonify(req)


#user_list_kanikka
@app.route(baseUrl+'/user_listkanikka', methods = ['POST'])
def userlistkanikka():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.userkanikka(req)
        print("checklog data is",checklog)
        if(isinstance(checklog, str)):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp'] = "SUCCESS"
        if(checklog['resp'] and checklog['resp']!='ERROR' or checklog['resp_type'] == "SUCCESS"):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp_type']=="SUCCESS"
            return jsonify(checklog)
        else:
            respn = {}
            respn['resp_type']="FAIL"
            respn['resp_code']="0"
            respn['message']="Request Failed Due to Unknown Error"
            respn['requestdata']="Error Captured during execution"
            respn['em_reqid']=req["em_reqid"]
            respn['timestamp']=str(datetime.datetime.now())
            respn['em_custid']=req["em_custid"]
            respn['resp_frm_yesb']=""
            respn['resp_frm_ewire']="Error Captured during execution"
            return jsonify(respn)
    else:
        req['resp_type']="FAIL"
        req['resp_code']=0
        req['message']="Request Failed Due to Unknown Error"
        req['responsedata']="Error Captured during execution"
        return jsonify(req)
#history
@app.route(baseUrl+'/history', methods = ['POST'])
def history():
    req = request.json
    print(">>>>>>>>>>>",req)
    rqJson = json.dumps(req)
    print("ASSSSasssdf",rqJson)
    req = ast.literal_eval(rqJson)
    print("ASSSSasssdf",req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.userhistory(req)
        print("checklog data is",checklog)
        if(isinstance(checklog, str)):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp'] = "SUCCESS"
        if(checklog['resp'] and checklog['resp']!='ERROR' or checklog['resp_type'] == "SUCCESS"):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp_type']=="SUCCESS"
            return jsonify(checklog)
        else:
            respn = {}
            respn['resp_type']="FAIL"
            respn['resp_code']="0"
            respn['message']="Request Failed Due to Unknown Error"
            respn['requestdata']="Error Captured during execution"
            respn['em_reqid']=req["em_reqid"]
            respn['timestamp']=str(datetime.datetime.now())
            respn['em_custid']=req["em_custid"]
            respn['resp_frm_yesb']=""
            respn['resp_frm_ewire']="Error Captured during execution"
            return jsonify(respn)
    else:
        req['resp_type']="FAIL"
        req['resp_code']=0
        req['message']="Request Failed Due to Unknown Error"
        req['responsedata']="Error Captured during execution"
        return jsonify(req)
#pooja bill
@app.route(baseUrl+'/pooja_bill', methods = ['POST'])
def poojabill():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.poojabill(req)
        print("checklog data is",checklog)
        if(isinstance(checklog, str)):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp'] = "SUCCESS"
        if(checklog['resp'] and checklog['resp']!='ERROR' or checklog['resp_type'] == "SUCCESS"):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp_type']=="SUCCESS"
            return jsonify(checklog)
        else:
            respn = {}
            respn['resp_type']="FAIL"
            respn['resp_code']="0"
            respn['message']="Request Failed Due to Unknown Error"
            respn['requestdata']="Error Captured during execution"
            respn['em_reqid']=req["em_reqid"]
            respn['timestamp']=str(datetime.datetime.now())
            respn['em_custid']=req["em_custid"]
            respn['resp_frm_yesb']=""
            respn['resp_frm_ewire']="Error Captured during execution"
            return jsonify(respn)
    else:
        req['resp_type']="FAIL"
        req['resp_code']=0
        req['message']="Request Failed Due to Unknown Error"
        req['responsedata']="Error Captured during execution"
        return jsonify(req)

#kanikka_pay
@app.route(baseUrl+'/kanikka_pay', methods = ['POST'])
def kanikka_pay():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.kanikkapay(req)
        print("checklog data is",checklog)
        if(isinstance(checklog, str)):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp'] = "SUCCESS"
        if(checklog['resp'] and checklog['resp']!='ERROR' or checklog['resp_type'] == "SUCCESS"):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp_type']=="SUCCESS"
            return jsonify(checklog)
        else:
            respn = {}
            respn['resp_type']="FAIL"
            respn['resp_code']="0"
            respn['message']="Request Failed Due to Unknown Error"
            respn['requestdata']="Error Captured during execution"
            respn['em_reqid']=req["em_reqid"]
            respn['timestamp']=str(datetime.datetime.now())
            respn['em_custid']=req["em_custid"]
            respn['resp_frm_yesb']=""
            respn['resp_frm_ewire']="Error Captured during execution"
            return jsonify(respn)
    else:
        req['resp_type']="FAIL"
        req['resp_code']=0
        req['message']="Request Failed Due to Unknown Error"
        req['responsedata']="Error Captured during execution"
        return jsonify(req)
#offering bill
@app.route(baseUrl+'/offering_bill', methods = ['POST'])
def offeringbill():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.offeringBill(req)
        print("checklog data is",checklog)
        if(isinstance(checklog, str)):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp'] = "SUCCESS"
        if(checklog['resp'] and checklog['resp']!='ERROR' or checklog['resp_type'] == "SUCCESS"):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp_type']=="SUCCESS"
            return jsonify(checklog)
        else:
            respn = {}
            respn['resp_type']="FAIL"
            respn['resp_code']="0"
            respn['message']="Request Failed Due to Unknown Error"
            respn['requestdata']="Error Captured during execution"
            respn['em_reqid']=req["em_reqid"]
            respn['timestamp']=str(datetime.datetime.now())
            respn['em_custid']=req["em_custid"]
            respn['resp_frm_yesb']=""
            respn['resp_frm_ewire']="Error Captured during execution"
            return jsonify(respn)
    else:
        req['resp_type']="FAIL"
        req['resp_code']=0
        req['message']="Request Failed Due to Unknown Error"
        req['responsedata']="Error Captured during execution"
        return jsonify(req)

#nearby attraction
@app.route(baseUrl+'/nearby_attraction', methods = ['POST'])
def nearbyatrctin():
    req = request.json
    print(">>>>>>>>>>>",req)
    rqJson = json.dumps(req)
    print("ASSSSasssdf",rqJson)
    req = ast.literal_eval(rqJson)
    print("ASSSSasssdf",req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.nearbyattraction(req)
        print("checklog data is",checklog)
        if(isinstance(checklog, str)):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp'] = "SUCCESS"
        if(checklog['resp'] and checklog['resp']!='ERROR' or checklog['resp_type'] == "SUCCESS"):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp_type']=="SUCCESS"
            return jsonify(checklog)
        else:
            respn = {}
            respn['resp_type']="FAIL"
            respn['resp_code']="0"
            respn['message']="Request Failed Due to Unknown Error"
            respn['requestdata']="Error Captured during execution"
            respn['em_reqid']=req["em_reqid"]
            respn['timestamp']=str(datetime.datetime.now())
            respn['em_custid']=req["em_custid"]
            respn['resp_frm_yesb']=""
            respn['resp_frm_ewire']="Error Captured during execution"
            return jsonify(respn)
    else:
        req['resp_type']="FAIL"
        req['resp_code']=0
        req['message']="Request Failed Due to Unknown Error"
        req['responsedata']="Error Captured during execution"
        return jsonify(req)
#nearest stay
@app.route(baseUrl+'/nearest_stay', methods = ['POST'])
def neareststay():
    req = request.json
    print(">>>>>>>>>>>",req)
    rqJson = json.dumps(req)
    print("ASSSSasssdf",rqJson)
    req = ast.literal_eval(rqJson)
    print("ASSSSasssdf",req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.neareststay(req)
        print("checklog data is",checklog)
        if(isinstance(checklog, str)):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp'] = "SUCCESS"
        if(checklog['resp'] and checklog['resp']!='ERROR' or checklog['resp_type'] == "SUCCESS"):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp_type']=="SUCCESS"
            return jsonify(checklog)
        else:
            respn = {}
            respn['resp_type']="FAIL"
            respn['resp_code']="0"
            respn['message']="Request Failed Due to Unknown Error"
            respn['requestdata']="Error Captured during execution"
            respn['em_reqid']=req["em_reqid"]
            respn['timestamp']=str(datetime.datetime.now())
            respn['em_custid']=req["em_custid"]
            respn['resp_frm_yesb']=""
            respn['resp_frm_ewire']="Error Captured during execution"
            return jsonify(respn)
    else:
        req['resp_type']="FAIL"
        req['resp_code']=0
        req['message']="Request Failed Due to Unknown Error"
        req['responsedata']="Error Captured during execution"
        return jsonify(req)
#diety
@app.route(baseUrl+'/user_diety', methods = ['POST'])
def dietylist():
    req = request.json
    print(">>>>>>>>>>>",req)
    rqJson = json.dumps(req)
    print("ASSSSasssdf",rqJson)
    req = ast.literal_eval(rqJson)
    print("ASSSSasssdf",req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.listdiety(req)
        print("checklog data is",checklog)
        if(isinstance(checklog, str)):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp'] = "SUCCESS"
        if(checklog['resp'] and checklog['resp']!='ERROR' or checklog['resp_type'] == "SUCCESS"):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp_type']=="SUCCESS"
            return jsonify(checklog)
        else:
            respn = {}
            respn['resp_type']="FAIL"
            respn['resp_code']="0"
            respn['message']="Request Failed Due to Unknown Error"
            respn['requestdata']="Error Captured during execution"
            respn['em_reqid']=req["em_reqid"]
            respn['timestamp']=str(datetime.datetime.now())
            respn['em_custid']=req["em_custid"]
            respn['resp_frm_yesb']=""
            respn['resp_frm_ewire']="Error Captured during execution"
            return jsonify(respn)
    else:
        req['resp_type']="FAIL"
        req['resp_code']=0
        req['message']="Request Failed Due to Unknown Error"
        req['responsedata']="Error Captured during execution"
        return jsonify(req)
#location
@app.route(baseUrl+'/location', methods = ['POST'])
def loctn():
    req = request.json
    print(">>>>>>>>>>>",req)
    rqJson = json.dumps(req)
    print("ASSSSasssdf",rqJson)
    req = ast.literal_eval(rqJson)
    print("ASSSSasssdf",req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.location(req)
        print("checklog data is",checklog)
        if(isinstance(checklog, str)):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp'] = "SUCCESS"
        if(checklog['resp'] and checklog['resp']!='ERROR' or checklog['resp_type'] == "SUCCESS"):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp_type']=="SUCCESS"
            return jsonify(checklog)
        else:
            respn = {}
            respn['resp_type']="FAIL"
            respn['resp_code']="0"
            respn['message']="Request Failed Due to Unknown Error"
            respn['requestdata']="Error Captured during execution"
            respn['em_reqid']=req["em_reqid"]
            respn['timestamp']=str(datetime.datetime.now())
            respn['em_custid']=req["em_custid"]
            respn['resp_frm_yesb']=""
            respn['resp_frm_ewire']="Error Captured during execution"
            return jsonify(respn)
    else:
        req['resp_type']="FAIL"
        req['resp_code']=0
        req['message']="Request Failed Due to Unknown Error"
        req['responsedata']="Error Captured during execution"
        return jsonify(req)

#map
@app.route(baseUrl+'/map', methods = ['POST'])
def map():
    req = request.json
    print(">>>>>>>>>>>",req)
    rqJson = json.dumps(req)
    print("ASSSSasssdf",rqJson)
    req = ast.literal_eval(rqJson)
    print("ASSSSasssdf",req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.map(req)
        print("checklog data is",checklog)
        if(isinstance(checklog, str)):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp'] = "SUCCESS"
        if(checklog['resp'] and checklog['resp']!='ERROR' or checklog['resp_type'] == "SUCCESS"):
            checklog = constantslayer.convinptodict(checklog)
            checklog['resp_type']=="SUCCESS"
            return jsonify(checklog)
        else:
            respn = {}
            respn['resp_type']="FAIL"
            respn['resp_code']="0"
            respn['message']="Request Failed Due to Unknown Error"
            respn['requestdata']="Error Captured during execution"
            respn['em_reqid']=req["em_reqid"]
            respn['timestamp']=str(datetime.datetime.now())
            respn['em_custid']=req["em_custid"]
            respn['resp_frm_yesb']=""
            respn['resp_frm_ewire']="Error Captured during execution"
            return jsonify(respn)
    else:
        req['resp_type']="FAIL"
        req['resp_code']=0
        req['message']="Request Failed Due to Unknown Error"
        req['responsedata']="Error Captured during execution"
        return jsonify(req)