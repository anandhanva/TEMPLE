import datetime
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
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        if(checklog):
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

@app.route(baseUrl+'/temple_list', methods = ['POST'])
def templelist_be():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())


@app.route(baseUrl+'/acc_statement', methods = ['POST'])
def AccStatement():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.accountstatement(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())

@app.route(baseUrl+'/temple_admin', methods = ['POST'])
def templeadmin_be():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())

@app.route(baseUrl+'/create_bank', methods = ['POST'])
def createbank_be():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())

@app.route(baseUrl+'/activity_type', methods = ['POST'])
def Activitytype():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())

@app.route(baseUrl+'/list_bank', methods = ['POST'])
def list_bank_be():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())


@app.route(baseUrl+'/create_lords', methods = ['POST'])
def create_lords_be():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())


@app.route(baseUrl+'/list_lords', methods = ['POST'])
def list_lords_be():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())
# TEMPLE ADMIN>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#CREATE POOJA



@app.route(baseUrl+'/create_pooja', methods = ['POST'])
def createpooja():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    print("$$$$$$$$$$$$$valdata",valdata)
    valdata=constantslayer.convinptodict(valdata)
    
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.Createpooja(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        if(checklog):
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
   


# LIST POOJA TEMPLE ADMIN

@app.route(baseUrl+'/list_pooja', methods = ['POST'])
def listpooja():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.Listpooja(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        if(checklog):
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

#CREATE PRASADAM TEMPLE ADMIN

@app.route(baseUrl+'/create_prasadam', methods = ['POST'])
def createprasadam():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer. Createprasadam(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        if(checklog):
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

#LIST PRASADAM TEMPLE ADMIN

@app.route(baseUrl+'/list_prasadam', methods = ['POST'])
def listprasadam():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.Listprasadam(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        if(checklog):
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


#CTREATE OFFERINGS TEMPLE ADMIN

@app.route(baseUrl+'/create_offerings', methods = ['POST'])
def createofferings():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.Createofferings(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        if(checklog):
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


#LIST OFFERINGS  TEMPLE ADMIN
@app.route(baseUrl+'/list_offerings', methods = ['POST'])
def listofferings():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.Listofferings(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        if(checklog):
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


#ADD RATE TEMPLE ADMIN
@app.route(baseUrl+'/add_rate', methods = ['POST'])
def addrate():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.Addrate(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        if(checklog):
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

#LIST RATE TEMPLE ADMIN
@app.route(baseUrl+'/list_rate', methods = ['POST'])
def listrate():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.Listrate(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        if(checklog):
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

#CREATE DIETY TEMPLE ADMIN

@app.route(baseUrl+'/create_diety', methods = ['POST'])
def creatediety():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.CreateDiety(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        if(checklog):
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

#DROP DIETY TEMPLE ADMIN
@app.route(baseUrl+'/drop_diety', methods = ['POST'])
def drop_diety():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.dropdiety(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        if(checklog):
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


#LIST DIETY TEMPLE ADMIN

@app.route(baseUrl+'/list_diety', methods = ['POST'])
def listdiety():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.Listdiety(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        if(checklog):
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

#list total superadmin
@app.route(baseUrl+'/list_total', methods = ['POST'])
def list_total_be():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.listtotal(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())
   

#create account superadmin

@app.route(baseUrl+'/create_account', methods = ['POST'])
def create_account_be():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.creaccsuper(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())
###################################################################################################################################
#reports by diety
@app.route(baseUrl+'/rep_diety', methods = ['POST'])
def rep_diety():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.repbydiety(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        if(checklog):
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
#reports by date
@app.route(baseUrl+'/rep_date', methods = ['POST'])
def rep_date():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.repbydate(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        if(checklog):
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
#reports by customer city
@app.route(baseUrl+'/rep_custcity', methods = ['POST'])
def rep_custcity():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.Listpooja(req)
        print("checklog",checklog)
        checklog = constantslayer.repbycustcity(checklog)
        if(checklog):
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
#invoice view
@app.route(baseUrl+'/invoice_view', methods = ['POST'])
def invoice_view():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.invoiceview(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        if(checklog):
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
#invoice list
@app.route(baseUrl+'/invoice_list', methods = ['POST'])
def invoice_list():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.invoicelist(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        if(checklog):
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
#invoice search
@app.route(baseUrl+'/invoice_search', methods = ['POST'])
def invoice_search():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.invoicesearch(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        if(checklog):
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
#create parking
@app.route(baseUrl+'/create_parking', methods = ['POST'])
def create_parking():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.createparking(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        if(checklog):
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
#list parking
@app.route(baseUrl+'/list_parking', methods = ['POST'])
def list_parking():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.listparking(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        if(checklog):
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
#create sightseeing
@app.route(baseUrl+'/create_sightseeing', methods = ['POST'])
def create_sightseeing():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.createsightseeing(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        if(checklog):
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
#list sightseeing
@app.route(baseUrl+'/list_sightseeing', methods = ['POST'])
def list_sightseeing():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.listsightseeing(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        if(checklog):
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

#drop rate
@app.route(baseUrl+'/drop_rate', methods = ['POST'])
def drop_rate():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.droprate(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        if(checklog):
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


























































































############################################################################################################################       

#list account superadmin

@app.route(baseUrl+'/list_account', methods = ['POST'])
def list_account_be():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.listaccsuper(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())

#create transtemp superadmin
@app.route(baseUrl+'/create_transtemp', methods = ['POST'])
def create_trans_be():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.cretranstemp(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())


#list transtemp superadmin
@app.route(baseUrl+'/list_transtemp', methods = ['POST'])
def list_trans_temp_be():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.listtranstemp(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())
   

#create devaswom superadmin
@app.route(baseUrl+'/create_devaswom', methods = ['POST'])
def create_devaswom_be():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.credevaswomsuper(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())
   

#list devaswom superadmin

@app.route(baseUrl+'/list_devaswom', methods = ['POST'])
def list_devaswom_be():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.listdevaswomsuper(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())

#create bank admin suoeradmin
@app.route(baseUrl+'/create_bank_admin', methods = ['POST'])
def create_bank_admin_be():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.crebankadminsuper(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())

# list manage bank admin superadmin
@app.route(baseUrl+'/ list_bank_admin', methods = ['POST'])
def  list_mng_bank_admin_be():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.listmaangebankadminsuper(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())

#card allocate superadmin
@app.route(baseUrl+'/card_allocate', methods = ['POST'])
def  card_allocate_be():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.cardallocate(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())


#list card allocate superadmin

@app.route(baseUrl+'/list_card_allocate', methods = ['POST'])
def  list_card_allocate_be():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.listcardallocate(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())

#create block temple superadmin
@app.route(baseUrl+'/create_block_temple', methods = ['POST'])
def  create_block_temple_be():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.creblocktemple(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())
   
#list block temple superadmin

@app.route(baseUrl+'/list_block_temple', methods = ['POST'])
def  list_block_temple_be():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.listblocktemple(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())
   
#create block temple superadmin
@app.route(baseUrl+'/create_block_devaswom', methods = ['POST'])
def  create_block_devaswom_be():
    req = request.json
    req = ast.literal_eval(req)
    req = constantslayer.convinptodict(req)
    valdata=validateReq(req)
    valdata=constantslayer.convinptodict(valdata)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.createblocktemple(req)
        print("checklog",checklog)
        checklog = constantslayer.convinptodict(checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())
    

@app.route(baseUrl+'/list_block_devaswom', methods = ['POST'])
def  list_block_devaswom_be():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())

#create_block_cust

@app.route(baseUrl+'/create_block_customer', methods = ['POST'])
def  create_block_customer_be():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())


@app.route(baseUrl+'/pooldetails', methods = ['POST'])
def Pool_Details():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())

#list_block_customer

@app.route(baseUrl+'/list_block_customer', methods = ['POST'])
def  list_block_customer_be():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())
        


@app.route(baseUrl+'/fundtransfer', methods = ['POST'])
def Fundtransfer():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())

#create_block_card

@app.route(baseUrl+'/create_block_card', methods = ['POST'])
def  create_block_card_be():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())
    

@app.route(baseUrl+'/select_devaswom', methods = ['POST'])
def Select_Devaswom():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())

#list_block_card

@app.route(baseUrl+'/list_block_card', methods = ['POST'])
def  list_block_card_be():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())
        

@app.route(baseUrl+'/select_temple', methods = ['POST'])
def SelectTemple():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())

#create_block_bank

@app.route(baseUrl+'/create_block_bank', methods = ['POST'])
def  create_block_bank_be():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())
        


@app.route(baseUrl+'/requestmoney', methods = ['POST'])
def Requestmoney():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())

@app.route(baseUrl+'/list_block_bank', methods = ['POST'])
def  list_block_bank_be():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())
       
# devaswom add temple
@app.route(baseUrl+'/devaddtemple', methods = ['POST'])
def adtemple():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())
# devaswom block temple
@app.route(baseUrl+'/devblocktemple', methods = ['POST'])
def blocktemple():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())
# devaswom block temple admin
@app.route(baseUrl+'/devblocktempleadmin', methods = ['POST'])
def blocktempleadmin():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())
# create finance admin
@app.route(baseUrl+'/crefinadmin', methods = ['POST'])
def crefinadmin():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())
# create temple admin
@app.route(baseUrl+'/cretemadmin', methods = ['POST'])
def cretemadmin():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())
# create account devaswom
@app.route(baseUrl+'/creaccdev', methods = ['POST'])
def creaccount():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())

# list  temple api
@app.route(baseUrl+'/listaddtemple', methods = ['POST'])
def listtemple():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())

# list block  temple api
@app.route(baseUrl+'/listblocktemple', methods = ['POST'])
def listblocktemple():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())

# list fin admin
@app.route(baseUrl+'/listfinadmin', methods = ['POST'])
def listfinadmin():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())

# list temple admin
@app.route(baseUrl+'/listtempleadmin', methods = ['POST'])
def listtempleadmin():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())

# list account devaswom
@app.route(baseUrl+'/listaccdev', methods = ['POST'])
def listaccdev():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())

# temple details by virtual acc number
@app.route(baseUrl+'/tmpdatabyva', methods = ['POST'])
def tmpdatabyva():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())

# move money to devaswom
@app.route(baseUrl+'/movemoney', methods = ['POST'])
def movemoney():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())

# money load list
@app.route(baseUrl+'/moneyload', methods = ['POST'])
def moneyload():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())

# withdraw details
@app.route(baseUrl+'/withdrawdets', methods = ['POST'])
def withdrawdets():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())

# get temple details by id
@app.route(baseUrl+'/tempdetbyid', methods = ['POST'])
def tempdetbyid():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())

# fund transaction
@app.route(baseUrl+'/fundtxn', methods = ['POST'])
def fundtxn():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response()) 

# select temple admin dropdown
@app.route(baseUrl+'/selecttempleadmin', methods = ['POST'])
def selecttempleadmin():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response()) 

# select bank
@app.route(baseUrl+'/select_bank', methods = ['POST'])
def select_bank():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response()) 

# create devaswom admin
@app.route(baseUrl+'/credevadmin', methods = ['POST'])
def credevadmin():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response()) 

# list devaswom admin
@app.route(baseUrl+'/listdevadmin', methods = ['POST'])
def listdevadmin():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response())

#create account statement
@app.route(baseUrl+'/creaccstatement', methods = ['POST'])
def creaccstatement():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response()) 
#list account statement
@app.route(baseUrl+'/listaccstatement', methods = ['POST'])
def listaccstatement():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response()) 

#create devaswom
@app.route(baseUrl+'/credevaswom', methods = ['POST'])
def credevaswom():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response()) 

#list devaswom
@app.route(baseUrl+'/listdevaswom', methods = ['POST'])
def listdevaswom():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response()) 

#forgot pin by phone
@app.route(baseUrl+'/forpinphone', methods = ['POST'])
def forpinphone():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response()) 
#forgot pin request
@app.route(baseUrl+'/forpinreq', methods = ['POST'])
def forpinreq():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response()) 
#fund transfer
@app.route(baseUrl+'/fundtrans', methods = ['POST'])
def fundtrans():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response()) 
#list fund transfer
@app.route(baseUrl+'/listfundtrans', methods = ['POST'])
def listfundtrans():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response()) 
#load pool
@app.route(baseUrl+'/loadpool', methods = ['POST'])
def loadpool():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response()) 

#list load pool
@app.route(baseUrl+'/listloadpool', methods = ['POST'])
def listloadpool():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response()) 
#select bank drop
@app.route(baseUrl+'/selectbank', methods = ['POST'])
def selectbank():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response()) 
#select devsom drop
@app.route(baseUrl+'/selectdevsom', methods = ['POST'])
def selectdevsom():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.checklogin(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response()) 

#create history temple admin
@app.route(baseUrl+'/cre_history', methods = ['POST'])
def cre_history():
    valdata=validateReq(request)
    if(valdata['status']==200):
        print("checklogin")
        checklog=constantslayer.crehistory(request)
        print("checklog",checklog)
        checklog['resp_type']=="SUCCESS"
        return jsonify(betoui_response(checklog))
    else:
        request['resp_type']="FAIL"
        return jsonify(betoui_response()) 






