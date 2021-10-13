
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
# devaswom add temple
@app.route(baseUrl+'/devaddtemple', methods = ['POST'])
def adtemple():
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
# devaswom block temple
@app.route(baseUrl+'/devblocktemple', methods = ['POST'])
def blocktemple():
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
# devaswom block temple admin
@app.route(baseUrl+'/devblocktempleadmin', methods = ['POST'])
def blocktempleadmin():
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
# create finance admin
@app.route(baseUrl+'/crefinadmin', methods = ['POST'])
def crefinadmin():
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
# create temple admin
@app.route(baseUrl+'/cretemadmin', methods = ['POST'])
def cretemadmin():
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
# create account devaswom
@app.route(baseUrl+'/creaccdev', methods = ['POST'])
def creaccount():
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

# list  temple api
@app.route(baseUrl+'/listaddtemple', methods = ['POST'])
def listtemple():
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

# list block  temple api
@app.route(baseUrl+'/listblocktemple', methods = ['POST'])
def listblocktemple():
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

# list fin admin
@app.route(baseUrl+'/listfinadmin', methods = ['POST'])
def listfinadmin():
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

# list temple admin
@app.route(baseUrl+'/listtempleadmin', methods = ['POST'])
def listtempleadmin():
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

# list account devaswom
@app.route(baseUrl+'/listaccdev', methods = ['POST'])
def listaccdev():
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

# temple details by virtual acc number
@app.route(baseUrl+'/tmpdatabyva', methods = ['POST'])
def tmpdatabyva():
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

# move money to devaswom
@app.route(baseUrl+'/movemoney', methods = ['POST'])
def movemoney():
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

# money load list
@app.route(baseUrl+'/moneyload', methods = ['POST'])
def moneyload():
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

# withdraw details
@app.route(baseUrl+'/withdrawdets', methods = ['POST'])
def withdrawdets():
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

# get temple details by id
@app.route(baseUrl+'/tempdetbyid', methods = ['POST'])
def tempdetbyid():
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

# fund transaction
@app.route(baseUrl+'/fundtxn', methods = ['POST'])
def fundtxn():
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

# select temple admin dropdown
@app.route(baseUrl+'/selecttempleadmin', methods = ['POST'])
def selecttempleadmin():
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

# select bank
@app.route(baseUrl+'/select_bank', methods = ['POST'])
def select_bank():
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

# create devaswom admin
@app.route(baseUrl+'/credevadmin', methods = ['POST'])
def credevadmin():
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

# list devaswom admin
@app.route(baseUrl+'/listdevadmin', methods = ['POST'])
def listdevadmin():
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

#create account statement
@app.route(baseUrl+'/creaccstatement', methods = ['POST'])
def creaccstatement():
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
#list account statement
@app.route(baseUrl+'/listaccstatement', methods = ['POST'])
def listaccstatement():
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

#create devaswom
@app.route(baseUrl+'/credevaswom', methods = ['POST'])
def credevaswom():
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

#list devaswom
@app.route(baseUrl+'/listdevaswom', methods = ['POST'])
def listdevaswom():
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

#forgot pin by phone
@app.route(baseUrl+'/forpinphone', methods = ['POST'])
def forpinphone():
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
#forgot pin request
@app.route(baseUrl+'/forpinreq', methods = ['POST'])
def forpinreq():
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
#fund transfer
@app.route(baseUrl+'/fundtrans', methods = ['POST'])
def fundtrans():
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
#list fund transfer
@app.route(baseUrl+'/listfundtrans', methods = ['POST'])
def listfundtrans():
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
#load pool
@app.route(baseUrl+'/loadpool', methods = ['POST'])
def loadpool():
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

#list load pool
@app.route(baseUrl+'/listloadpool', methods = ['POST'])
def listloadpool():
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
#select bank drop
@app.route(baseUrl+'/selectbank', methods = ['POST'])
def selectbank():
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
#select devsom drop
@app.route(baseUrl+'/selectdevsom', methods = ['POST'])
def selectdevsom():
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







        


