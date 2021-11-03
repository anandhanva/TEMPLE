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




baseUrl="/api/v1/temple/"

@app.route('/', methods=['POST','GET'])
def base():
    return responses.upGetResponse()

# USER APIS
# USER LOGIN
@app.route(urlconstants.ENDPOINT+'/user', methods = ['POST'])
def user():
    
    return bllayer.processLoginRequest(request.json)

@app.route(urlconstants.ENDPOINT+'/ac', methods = ['POST'])
def ac():
    
    # Check User credentials and perform login operation
    return bllayer.accstmtfrmdb(request)



# ADD TEMPLE
@app.route(urlconstants.ENDPOINT+'/add_temple', methods = ['POST'])
def addtemples():
    
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

# # CREATE ACCOUNT
@app.route(urlconstants.ENDPOINT+'/create_account', methods = ['POST'])
def addaccount():
    
    return bllayer.createAccount(request)


# LIST ACCOUNT
@app.route(urlconstants.ENDPOINT+'/list_account', methods = ['POST'])
def listaccount():
    
    return bllayer.listAccountApi(request)



# CREATE FIN ADMIN
@app.route(urlconstants.ENDPOINT+'/add_finadmin', methods = ['POST'])
def createfinadmins():
    
    return bllayer.createFinAdmin(request)
#TEMPLE ADMIN--------------------------------------------------------------------------------------------
#CREATE POOJA
@app.route(urlconstants.ENDPOINT+'/create_pooja', methods = ['POST'])
def addpooja():
    
    return bllayer.createPooja(request.json)

#LIST POOJA
@app.route(urlconstants.ENDPOINT+'/list_pooja', methods = ['POST'])
def listpooja():
    
    return bllayer.listPooja(request.json)

#CREATE PRASADAM
@app.route(urlconstants.ENDPOINT+'/create_prasadam', methods = ['POST'])
def addprasadam():
    
    return bllayer.createPrasadam(request.json)

#LIST PRASADAM
@app.route(urlconstants.ENDPOINT+'/list_prasadam', methods = ['POST'])
def listprasadam():
    
    return bllayer.listPrasadam(request)

#CREATE OFFERINGS
@app.route(urlconstants.ENDPOINT+'/create_offerings', methods = ['POST'])
def addofferings():
    
    return bllayer.createOfferings(request.json)

#LIST OFFERINGS
@app.route(urlconstants.ENDPOINT+'/list_offerings', methods = ['POST'])
def listofferings():
    
    return bllayer.listOfferings(request)

#CREATE DIETY
@app.route(urlconstants.ENDPOINT+'/create_diety', methods = ['POST'])
def adddiety():
    
    return bllayer.createDiety(request.json)

#LIST DIETY
@app.route(urlconstants.ENDPOINT+'/list_diety', methods = ['POST'])
def listdiety():
    
    return bllayer.listDiety(request)

#CREATE HISTORY
@app.route(urlconstants.ENDPOINT+'/create_history', methods = ['POST'])
def addhistory():
    
    return bllayer.createHistory(request.json)

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

# DROPDOWN - -DIETY

@app.route(urlconstants.ENDPOINT+'/dropdown_diety', methods = ['POST'])
def dropDiety():
    
    return bllayer.dropdownDietyApi(request)


# DROPDOWN - -RATE

@app.route(urlconstants.ENDPOINT+'/dropdown_rate', methods = ['POST'])
def dropRate():
    
    return bllayer.dropdownRateApi(request)

#DROPDOWN - - QTY
@app.route(urlconstants.ENDPOINT+'/dropdown_qty', methods = ['POST'])
def dropQty():
    
    return bllayer.dropdownPrasadamQtyApi(request)

#CREATE KANIKKA
@app.route(urlconstants.ENDPOINT+'/create_kanikka', methods = ['POST'])
def createKanikka():
    
    return bllayer.createKanikkaApi(request.json)
#CREATE AIRPORT
@app.route(urlconstants.ENDPOINT+'/add_airport', methods = ['POST'])
def addAirport():
    
    return bllayer.addAirportApi(request.json)

#CREATE RATE
@app.route(urlconstants.ENDPOINT+'/add_rate', methods = ['POST'])
def addRate():
    
    return bllayer.addRateApi(request.json)

#CREATE QUANTITY
@app.route(urlconstants.ENDPOINT+'/add_quantity', methods = ['POST'])
def addQnty():
    
    return bllayer.addQntyApi(request.json)


#USER
#=============================================================================
#INDEX
@app.route(urlconstants.ENDPOINT+'/user_index', methods = ['POST'])
def userIndex():
    
    return bllayer.userIndexApi(request.json)


#GET KANIKKA BY DIETYID
@app.route(urlconstants.ENDPOINT+'/kanikka_bydietyid', methods = ['POST'])
def kanikkaByDietyid():
    
    return bllayer.kanikkaByDietyidApi(request.json)



#GET OFFERING BY TEMPLEID
@app.route(urlconstants.ENDPOINT+'/offering_bytempleid', methods = ['POST'])
def offeringByTempleid():
    
    return bllayer.offeringByTempleidApi(request)

#GET OFFERING BY DIETYID
@app.route(urlconstants.ENDPOINT+'/offering_bydietyid', methods = ['POST'])
def offeringByDietyid():
    
    return bllayer.offeringByDietyidApi(request)


#GET PRASADAM BY TEMPLEID
@app.route(urlconstants.ENDPOINT+'/prasadam_bytempleid', methods = ['POST'])
def prasadamByTempleid():
    
    return bllayer.prasadamByTempleidApi(request)

#GET POOJA BY TEMPLEID
@app.route(urlconstants.ENDPOINT+'/diety_bytempleid', methods = ['POST'])
def dietyjaByTempleid():
    
    return bllayer.dietyByTempleidApi(request)



#CREATE CATEGORY
@app.route(urlconstants.ENDPOINT+'/create_category', methods = ['POST'])
def createCategory():
    
    return bllayer.createCategoryApi(request)

#LIST CATEGORY
@app.route(urlconstants.ENDPOINT+'/list_category', methods = ['POST'])
def listCategory():
    
    return bllayer.listCategoryApi(request)


# DROPDOWN - -CATEGORY

@app.route(urlconstants.ENDPOINT+'/dropdown_category', methods = ['POST'])
def dropCategory():
    
    return bllayer.dropdownCategoryApi(request)

# CREATE - -FESTIVAL

@app.route(urlconstants.ENDPOINT+'/create_festival', methods = ['POST'])
def createFestival():
    
    return bllayer.createFestivalApi(request)

# LIST - -FESTIVAL

@app.route(urlconstants.ENDPOINT+'/list_festival', methods = ['POST'])
def listFestival():
    
    return bllayer.listFestivalApi(request)

# CREATE ACCOUNT STATEMENT
@app.route(urlconstants.ENDPOINT+'/create_acstatement', methods = ['POST'])
def createStatement():
    
    return bllayer.createStatementApi(request)
# LIST STATEMENT
@app.route(urlconstants.ENDPOINT+'/list_statement', methods = ['POST'])
def listStatement():
    
    return bllayer.listStatementApi(request)
#=====================================================================
#QR

#CREATE QR
@app.route(urlconstants.ENDPOINT+'/createqr', methods = ['POST'])
def qrGen():
    return bllayer.createQR(request)


#READ QR
@app.route(urlconstants.ENDPOINT+'/rdqrdata', methods = ['POST'])
def rdQr():
    return bllayer.rdQRdata(request)



# DROPDOWN - FINANCE-ACTIVITY

@app.route(urlconstants.ENDPOINT+'/dropdown_activity', methods = ['POST'])
def dropActivity():
    
    return bllayer.dropdownActivityApi(request)


@app.route(urlconstants.ENDPOINT+'/dropdown_data', methods = ['POST'])
def dropAcctData():
    
    return bllayer.dataByAcnumberApi(request)


@app.route(urlconstants.ENDPOINT+'/create_devasom', methods = ['POST'])
def createdevasam():
    
    return bllayer.createDevasamApi(request)

@app.route(urlconstants.ENDPOINT+'/list_devasom', methods = ['POST'])
def listdevasam():
    
    return bllayer.listDevasomApi(request)

@app.route(urlconstants.ENDPOINT+'/create_devasomadmin', methods = ['POST'])
def createdevasamadmin():
    
    return bllayer.createDevasomAdminApi(request)

@app.route(urlconstants.ENDPOINT+'/list_devasomadmin', methods = ['POST'])
def listdevasamadmin():
    
    return bllayer.listDevasomAdminApi(request)

#create poool

@app.route(urlconstants.ENDPOINT+'/create_pool', methods = ['POST'])
def createpool():
    
    return bllayer.createPoolApi(request)

#list poool

@app.route(urlconstants.ENDPOINT+'/list_pool', methods = ['POST'])
def listpool():
    
    return bllayer.listPoolsApi(request)

#create fund transfer
@app.route(urlconstants.ENDPOINT+'/create_fundtransfer', methods = ['POST'])
def createfdtra():
    
    return bllayer.createFundsTransfer(request)

#list fund transfer
@app.route(urlconstants.ENDPOINT+'/list_fundtransfer', methods = ['POST'])
def listfundtra():
    
    return bllayer.listFundsTransfer(request)

# BANK ADMIN--------------------------------------------------------------------------------------------
# CREATE FORGOT PIN
@app.route(urlconstants.ENDPOINT+'/create_forgotpin', methods = ['POST'])
def createforgotpin():
    
    return bllayer.createforgotpinApi(request)

#DROPDOWN DEVASWOM
@app.route(urlconstants.ENDPOINT+'/dropdown_devaswom', methods = ['POST'])
def dropdowndevaswom():
    
    return bllayer.dropdowndevaswomApi(request)

#DROPDOWN BANK
@app.route(urlconstants.ENDPOINT+'/dropdown_bank', methods = ['POST'])
def dropdownBank():
    
    return bllayer.dropDownBankApi(request)


#DROPDOWN TEMPLE
@app.route(urlconstants.ENDPOINT+'/dropdown_temple', methods = ['POST'])
def dropdownTemple():
    
    return bllayer.dropDownTempleApi(request)

#DROPDOWN IFSC
@app.route(urlconstants.ENDPOINT+'/dropdown_IFSC', methods = ['POST'])
def dropdownIFSC():
    
    return bllayer.dropDownIFSCApi(request)


# LIST - FINANCE-ACTIVITY

@app.route(urlconstants.ENDPOINT+'/list_financeactivity', methods = ['POST'])
def listActivity():
    
    return bllayer.listActivityApi(request)


#CREATE RECONCILIATION
@app.route(urlconstants.ENDPOINT+'/create_reconciliation', methods = ['POST'])
def createreconciliation():
    
    return bllayer.createReconciliationApi(request)

#LIST RECONCILIATION
@app.route(urlconstants.ENDPOINT+'/list_reconciliation', methods = ['POST'])
def listreconciliation():
    
    return bllayer.listReconciliationApi(request)


#CREATE TRANSACTION DEVASWOM
@app.route(urlconstants.ENDPOINT+'/create_transactiondevaswom', methods = ['POST'])
def createTransactionDevaswom():
    
    return bllayer.createTransactionDevaswomApi(request)


#LIST TRANSACTION DEVASWOM
@app.route(urlconstants.ENDPOINT+'/list_transactiondevaswom', methods = ['POST'])
def listTransactionDevaswom():
    
    return bllayer.listTransactionDevaswomApi(request)


#SUPER ADMIN---------------------------------------------------------------------------------------------
#MANAGE BANK
#CREATE BANK
@app.route(urlconstants.ENDPOINT+'/create_bank', methods = ['POST'])
def createbank():
    
    return bllayer.createBank(request)

#LIST BANK
@app.route(urlconstants.ENDPOINT+'/list_bankdetails', methods = ['POST'])
def listbankdetails():
    
    return bllayer.listBankDetails(request)

#MANAGE BANK ADMIN
#CREATE BANK ADMIN
@app.route(urlconstants.ENDPOINT+'/create_bankadmin', methods = ['POST'])
def createbankadmin():
    
    return bllayer.createBankAdmin(request)

#LIST BANK ADMIN
@app.route(urlconstants.ENDPOINT+'/list_bankadmin', methods = ['POST'])
def listbankadmin():
    
    return bllayer.listBankAdmin(request)

#MANAGE CARD
#CREATE CARD ALLOCATION
@app.route(urlconstants.ENDPOINT+'/create_cardallocation', methods = ['POST'])
def createCardAllocation():
    
    return bllayer.createCardAllocationApi(request)

#LIST CARD ALLOCATION
@app.route(urlconstants.ENDPOINT+'/list_cardallocation', methods = ['POST'])
def listCardAllocation():
    
    return bllayer.listCardAllocationApi(request)


#CREATE REQUEST MONEY
@app.route(urlconstants.ENDPOINT+'/create_reqmoney', methods = ['POST'])
def createreqmoney():
    
    return bllayer.createReqMoneyApi(request)

#MANAGE LORDS
#CREATE LORDS
@app.route(urlconstants.ENDPOINT+'/create_lords', methods = ['POST'])
def createlords():
    
    return bllayer.createlordsApi(request)

# LIST LORDS
@app.route(urlconstants.ENDPOINT+'/list_lords', methods = ['POST'])
def listlords():
    
    return bllayer.listlordsApi(request)


# GET TRANASACTION DEVASWOM
@app.route(urlconstants.ENDPOINT+'/get_transactiondevaswom', methods = ['POST'])
def gettranascactiondevaswom():
    
    return bllayer.gettransactiondevaswomApi(request)

# GET TRANASACTION BANK
@app.route(urlconstants.ENDPOINT+'/get_transactionbank', methods = ['POST'])
def gettranascactionbank():
    
    return bllayer.gettransactionbankApi(request)

# LIST TRANASACTION BANK
@app.route(urlconstants.ENDPOINT+'/list_transactionbank', methods = ['POST'])
def listtranascactionbank():
    
    return bllayer.listtransactionbankApi(request)

# GET TRANASACTION TEMPLE
@app.route(urlconstants.ENDPOINT+'/get_transactiontemple', methods = ['POST'])
def gettranascactiontemple():
    
    return bllayer.gettransactiontempleApi(request)

# LIST TRANASACTION TEMPLE
@app.route(urlconstants.ENDPOINT+'/list_transactiontemple', methods = ['POST'])
def listtranascactiontemple():
    
    return bllayer.listtransactiontempleApi(request)

#MANAGE TEMPLE
# CREATE BLOCK TEMPLE
@app.route(urlconstants.ENDPOINT+'/create_blocktemple', methods = ['POST'])
def createblocktemple():
    
    return bllayer.createblocktempleApi(request)

# LIST BLOCK TEMPLE
@app.route(urlconstants.ENDPOINT+'/list_blocktemple', methods = ['POST'])
def listblocktemple():
    
    return bllayer.listblocktempleApi(request)

#MANAGE DEVASWOM
# CREATE BLOCK DEVASWOM
@app.route(urlconstants.ENDPOINT+'/create_blockdevaswom', methods = ['POST'])
def createblockdevaswom():
    
    return bllayer.createblockdevaswomApi(request)

# LIST BLOCK DEVASWOM
@app.route(urlconstants.ENDPOINT+'/list_blockdevaswom', methods = ['POST'])
def listblockdevaswom():
    
    return bllayer.listblockdevaswomApi(request)

#MANAGE CUSTOMER
# CREATE BLOCK CUSTOMER
@app.route(urlconstants.ENDPOINT+'/create_blockcustomer', methods = ['POST'])
def createblockcustomer():
    
    return bllayer.createblockcustomerApi(request)

# LIST BLOCK CUSTOMER
@app.route(urlconstants.ENDPOINT+'/list_blockcustomer', methods = ['POST'])
def listblockcustomer():
    
    return bllayer.listblockcustomerApi(request)

#MANAGE CARD
# CREATE BLOCK CARD
@app.route(urlconstants.ENDPOINT+'/create_blockcard', methods = ['POST'])
def createblockcard():
    
    return bllayer.createblockcardApi(request)

# LIST BLOCK CARD
@app.route(urlconstants.ENDPOINT+'/list_blockcard', methods = ['POST'])
def listblockcard():
    
    return bllayer.listblockcardApi(request)

#MANAGE BANK
# CREATE BLOCK BANK
@app.route(urlconstants.ENDPOINT+'/create_blockbank', methods = ['POST'])
def createblockbank():
    
    return bllayer.createblockbankApi(request)

# LIST BLOCK BANK
@app.route(urlconstants.ENDPOINT+'/list_blockbank', methods = ['POST'])
def listblockbank():
    
    return bllayer.listblockbankApi(request)

#LIST TRANSACTION DEVASWOM
@app.route(urlconstants.ENDPOINT+'/list_transdevaswom', methods = ['POST'])
def listtransactiondevaswom():
    
    return bllayer.superlisttransdevaApi(request)

#LIST ACCONT STATEMENT
@app.route(urlconstants.ENDPOINT+'/list_acctstatement', methods = ['POST'])
def listacctstatement():
    
    return bllayer.listacctstatmeentapi(request)

#DROPDOWN ACTIVITIES TYPE
@app.route(urlconstants.ENDPOINT+'/dropdown_activitytype', methods = ['POST'])
def dropdownactivitytype():
    
    return bllayer.dropdownactivitytypeApi(request)

#DROPDOWN DEVASWOM
@app.route(urlconstants.ENDPOINT+'/dropdown_superdevaswom', methods = ['POST'])
def superdropdowndevaswom():
    
    return bllayer.superdropdowndevaswomapi(request)

#DROPDOWN TEMPLE
@app.route(urlconstants.ENDPOINT+'/dropdown_supertemple', methods = ['POST'])
def superdropdowntemple():
    
    return bllayer.superdropdowntempleapi(request)

#CREATE POOJA
@app.route(urlconstants.ENDPOINT+'/create_superpooja', methods = ['POST'])
def createsuperpooja():
    
    return bllayer.createsuperpoojaapi(request)

#LIST POOJA TOTAL
@app.route(urlconstants.ENDPOINT+'/list_superpooja', methods = ['POST'])
def listsuperpooja():
    
    return bllayer.listsuperpoojaapi(request)

# #CREATE ACCOUNT
# @app.route(urlconstants.ENDPOINT+'/create_superaccount', methods = ['POST'])
# def createsuperpooja():
    
#     return bllayer.createsuperaccountapi(request)

# #LIST ACCOUNT
# @app.route(urlconstants.ENDPOINT+'/list_superaccount', methods = ['POST'])
# def listsuperaccount():
    
#     return bllayer.listsuperaccountapi(request)

#CREATE SUPER DEVASWOM
@app.route(urlconstants.ENDPOINT+'/create_superdevaswom', methods = ['POST'])
def createsuperdevaswom():
    
    return bllayer.createsuperdevaswomapi(request)