
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

@app.route(baseUrl+'/temple_list', methods = ['POST'])
def templelist_be():
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

@app.route(baseUrl+'/temple_admin', methods = ['POST'])
def templeadmin_be():
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

@app.route(baseUrl+'/create_bank', methods = ['POST'])
def createbank_be():
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

@app.route(baseUrl+'/list_bank', methods = ['POST'])
def list_bank_be():
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


@app.route(baseUrl+'/create_lords', methods = ['POST'])
def create_lords_be():
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


@app.route(baseUrl+'/list_lords', methods = ['POST'])
def list_lords_be():
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

@app.route(baseUrl+'/create_pooja', methods = ['POST'])
def create_pooja_be():
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


@app.route(baseUrl+'/list_total', methods = ['POST'])
def list_total_be():
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



@app.route(baseUrl+'/create_account', methods = ['POST'])
def create_account_be():
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


@app.route(baseUrl+'/list_account', methods = ['POST'])
def list_account_be():
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



@app.route(baseUrl+'/create_tran_stemp', methods = ['POST'])
def create_trans_be():
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

@app.route(baseUrl+'/list_trans_temp', methods = ['POST'])
def list_trans_temp_be():
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


@app.route(baseUrl+'/create_devaswom', methods = ['POST'])
def create_devaswom_be():
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


@app.route(baseUrl+'/list_devaswom', methods = ['POST'])
def list_devaswom_be():
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

@app.route(baseUrl+'/create_bank_admin', methods = ['POST'])
def create_bank_admin_be():
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


@app.route(baseUrl+'/ list_manage_bank_admin', methods = ['POST'])
def  list_mng_bank_admin_be():
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


@app.route(baseUrl+'/card_allocate', methods = ['POST'])
def  card_allocate_be():
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

@app.route(baseUrl+'/list_card_allocate', methods = ['POST'])
def  list_card_allocate_be():
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


@app.route(baseUrl+'/create_block_temple', methods = ['POST'])
def  create_block_temple_be():
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
   

@app.route(baseUrl+'/list_block_temple', methods = ['POST'])
def  list_block_temple_be():
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
   

@app.route(baseUrl+'/create_block_devaswom', methods = ['POST'])
def  create_block_devaswom_be():
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


@app.route(baseUrl+'/list_block_devaswom', methods = ['POST'])
def  list_block_devaswom_be():
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

#create_block_cust

@app.route(baseUrl+'/create_block_customer', methods = ['POST'])
def  create_block_customer_be():
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

#list_block_customer

@app.route(baseUrl+'/list_block_customer', methods = ['POST'])
def  list_block_customer_be():
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

#create_block_card

@app.route(baseUrl+'/create_block_card', methods = ['POST'])
def  create_block_card_be():
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

#list_block_card

@app.route(baseUrl+'/list_block_card', methods = ['POST'])
def  list_block_card_be():
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

#create_block_bank

@app.route(baseUrl+'/create_block_bank', methods = ['POST'])
def  create_block_bank_be():
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

@app.route(baseUrl+'/list_block_bank', methods = ['POST'])
def  list_block_bank_be():
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
