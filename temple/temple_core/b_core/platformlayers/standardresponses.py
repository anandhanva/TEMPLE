from b_core.statics.urlconstants import LOGIN
from b_core.statics import ipconstants


commonValues = {}

commonValues['LOGIN'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/hash",
                            "reqtype" : "LOGINREQ",
                            "methodtype" : "POST"
                        }
commonValues['CORELOGIN']={
                            "checkUserServer": ipconstants.templeBcoreServers,
                            "checkUserHeader":{"Content-Type":"application/json"},
                            "checkUserEndpoint":"/checkuserLogin",
                            "checkUserReqType":"LOGINREQ",
                            "checkUserMethodType":"POST",
                            }

commonValues['HASH_MO'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.hashServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/hashrequest",
                            "reqtype" : "HASHREQ",
                            "methodtype" : "POST"
                        }

commonValues['ACCOUNT_STATEMENT']={
                            "checkUserServer": ipconstants.templeBcoreServers,
                            "checkUserHeader":{"Content-Type":"application/json"},
                            "checkUserEndpoint":"/checkuserLogin",
                            "checkUserReqType":"ACCSTMTREQ",
                            "checkUserMethodType":"POST",
                            }



commonValues['ADD_TEMPLE'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.hashServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/add_temple",
                            "reqtype" : "ADDTEMPLEREQ",
                            "methodtype" : "POST"
                        }
commonValues['LIST_TEMPLE'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.hashServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_temple",
                            "reqtype" : "LISTTEMPLEREQ",
                            "methodtype" : "POST"
                        }
commonValues['CREATETEMPLE_ADMIN'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.hashServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/createtemple_admin",
                            "reqtype" : "CREATETEMPLEADMINREQ",
                            "methodtype" : "POST"
                        }
commonValues['LISTTEMPLE_ADMIN'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.hashServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/listtemple_admin",
                            "reqtype" : "LISTTEMPLEADMINREQ",
                            "methodtype" : "POST"
                        }
commonValues['CREATE_ACCOUNT'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.hashServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_account",
                            "reqtype" : "CREATEACCOUNTREQ",
                            "methodtype" : "POST"
                        }
commonValues['LIST_ACCOUNT'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.hashServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_account",
                            "reqtype" : "LISTACCOUNTREQ",
                            "methodtype" : "POST"
                        }


commonValues['ADD_FINADMIN'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.hashServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/add_finadmin",
                            "reqtype" : "CREATEFINADMINREQ",
                            "methodtype" : "POST"
                        }

commonValues['CREATEPOOJA'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_pooja",
                            "reqtype" : "CREATEPOOJAREQ",
                            "methodtype" : "POST"
                        }

commonValues['LISTPOOJA'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_pooja",
                            "reqtype" : "LISTPOOJAREQ",
                            "methodtype" : "POST"
                        }


commonValues['CREAOFFERINGS'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_offerings",
                            "reqtype" : "CREATEOFFERINGREQ",
                            "methodtype" : "POST"
                        }

commonValues['LISTOFFERINGS'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_offerings",
                            "reqtype" : "LISTOFFERINGREQ",
                            "methodtype" : "POST"
                        }
commonValues['CREAPRASADAM'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_prasadam",
                            "reqtype" : "CREATEPRASADAMREQ",
                            "methodtype" : "POST"
                        }
commonValues['LISTPRASADAM'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_prasadam",
                            "reqtype" : "LISTPRASADAMREQ",
                            "methodtype" : "POST"
                        }
commonValues['CREATEDIETY'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_diety",
                            "reqtype" : "CREATEDIETYREQ",
                            "methodtype" : "POST"
                        }

commonValues['LISTDIETY'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_diety",
                            "reqtype" : "LISTDIETYREQ",
                            "methodtype" : "POST"
                        }
commonValues['CREHISTORY'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_history",
                            "reqtype" : "CREATEHISTORYREQ",
                            "methodtype" : "POST"
                        }
commonValues['LISTHISTORY'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_history",
                            "reqtype" : "LISTHISTORYREQ",
                            "methodtype" : "POST"
                        }
commonValues['DROPDOWNDIETY'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/dropdown_diety",
                            "reqtype" : "DROPDOWNDIETYREQ",
                            "methodtype" : "POST"
                        }
commonValues['DROPDOWNRATE'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/dropdown_rate",
                            "reqtype" : "DROPDOWNRATEREQ",
                            "methodtype" : "POST"
                        }
commonValues['CREATE_TRAVEL_BY_AIR'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/add_airport",
                            "reqtype" : "CREATEAIRPORTREQ",
                            "methodtype" : "POST"}
commonValues['CREATESTAY'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_stay",
                            "reqtype" : "CREATESTAYREQ",
                            "methodtype" : "POST"
                        }
commonValues['LISTSTAY'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_stay",
                            "reqtype" : "LISTSTAYREQ",
                            "methodtype" : "POST"
                        }
commonValues['ADDRATE'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/add_rate",
                            "reqtype" : "CREATERATEREQ",
                            "methodtype" : "POST"
                        }
commonValues['QUANTITYLIST'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/add_quantity",
                            "reqtype" : "CREATEQNTYREQ",
                            "methodtype" : "POST"
                        }


#=======================================================================
#USER
commonValues['QRGENERATION'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/createqr",
                            "reqtype" : "QRGENREQ",
                            "methodtype" : "POST"
                        }

commonValues['READQRDATA'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/rdqrdata",
                            "reqtype" : "READQRREQ",
                            "methodtype" : "POST"
                        }


#INDEX
commonValues['USERINDEX'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/user_index",
                            "reqtype" : "USERINDEXREQ",
                            "methodtype" : "POST"
                        }


commonValues['GETKANIKKABYDIETYID'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/kanikka_bydietyid",
                            "reqtype" : "GETKANIKKABYDIETYIDREQ",
                            "methodtype" : "POST"
                        }

commonValues['GETOFFERINGBYTEMPLEID'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/offering_bytempleid",
                            "reqtype" : "GETOFFERINGBYTEMPLEIDREQ",
                            "methodtype" : "POST"
                        }



commonValues['GETOFFERINGBYDIETYID'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/offering_bydietyid",
                            "reqtype" : "GETOFFERINGBYDIETYIDREQ",
                            "methodtype" : "POST"
                        }

commonValues['GETPRASADAMTEMPLEID'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/prasadam_bytempleid",
                            "reqtype" : "GETPRASADAMTEMPLEIDREQ",
                            "methodtype" : "POST"
                        }


commonValues['GETDIETYTEMPLEID'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/diety_bytempleid",
                            "reqtype" : "GETDIETYTEMPLEIDREQ",
                            "methodtype" : "POST"
                        }
commonValues['CREATECATEGORY'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_category",
                            "reqtype" : "CREATECATEGORYREQ",
                            "methodtype" : "POST"
                        }
commonValues['LISTCATEGORY'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_category",
                            "reqtype" : "LISTCATEGORYREQ",
                            "methodtype" : "POST"
                        }
commonValues['DROPDOWNCATEGORY'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/dropdown_category",
                            "reqtype" : "DROPDOWNCATEGORYREQ",
                            "methodtype" : "POST"
                        }
commonValues['CREATEFESTIVAL'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_festival",
                            "reqtype" : "CREATEFESTIVALREQ",
                            "methodtype" : "POST"
                        }
commonValues['LISTFESTIVAL'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_festival",
                            "reqtype" : "LISTFESTIVALREQ",
                            "methodtype" : "POST"
                        }
commonValues['CREATESTATEMENT'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_acstatement",
                            "reqtype" : "CREATESTATEMENTREQ",
                            "methodtype" : "POST"
                        }
commonValues['LISTSTATEMENT'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_statement",
                            "reqtype" : "LISTSTATEMENTREQ",
                            "methodtype" : "POST"
                        }
commonValues['DROPDOWNACTIVITY'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/dropdown_activity",
                            "reqtype" : "DROPDOWNACTIVITYREQ",
                            "methodtype" : "POST"
                        }


commonValues['GETDATABYACNUMBER'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/dropdown_data",
                            "reqtype" : "GETDATABYACNUMBERREQ",
                            "methodtype" : "POST"
                        }
commonValues['CREATEDEVASWOMBANK'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_devasom",
                            "reqtype" : "CREATEDEVSOMREQ",
                            "methodtype" : "POST"
                        }

commonValues['LISTDEVASOM'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_devasom",
                            "reqtype" : "LISTDEVSOMREQ",
                            "methodtype" : "POST"
                        }

commonValues['CREATEDEVASOMADMIN'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_devasomadmin",
                            "reqtype" : "CREATEDEVSOMADMINREQ",
                            "methodtype" : "POST"
                        }

commonValues['LISTDEVASOMADMINLIST'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_devasomadmin",
                            "reqtype" : "LISTDEVSOMADMINREQ",
                            "methodtype" : "POST"
                        }

commonValues['CREATEPOOL'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_pool",
                            "reqtype" : "CREATEPOOLREQ",
                            "methodtype" : "POST"
                        }

commonValues['LISTPOOL'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_pool",
                            "reqtype" : "LISTPOOLREQ",
                            "methodtype" : "POST"
                        }

commonValues['CREATEFUNDTRANSFER'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_fundtransfer",
                            "reqtype" : "CREATEFUNDTRANSFERREQ",
                            "methodtype" : "POST"
                        }

commonValues['LISTFUNDTRANSFER'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_fundtransfer",
                            "reqtype" : "LISTFUNDTRANSFERREQ",
                            "methodtype" : "POST"
                        }

commonValues['DROPDOWNBANK'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/dropdown_bank",
                            "reqtype" : "DROPDOWNBANKREQ",
                            "methodtype" : "POST"
                        }

commonValues['DROPDOWNTEMPLE'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/dropdown_temple",
                            "reqtype" : "DROPDOWNTEMPLEREQ",
                            "methodtype" : "POST"
                        }

commonValues['DROPDOWNIFSC'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/dropdown_IFSC",
                            "reqtype" : "DROPDOWNIFSCREQ",
                            "methodtype" : "POST"
                        }

commonValues['LISTFINANCEACTIVITY'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_financeactivity",
                            "reqtype" : "LISTFINANCEACTIVITYREQ",
                            "methodtype" : "POST"
                        }

commonValues['CREATERECONCILIATION'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_reconciliation",
                            "reqtype" : "CREATERECONCILIATIONREQ",
                            "methodtype" : "POST"
                        }

commonValues['LISTRECONCILIATION'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_reconciliation",
                            "reqtype" : "LISTRECONCILIATIONREQ",
                            "methodtype" : "POST"
                        }

commonValues['CREATEFORGOTPIN'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_forgotpin",
                            "reqtype" : "CREATEFORGOTREQ",
                            "methodtype" : "POST"
                        }

commonValues['CREATETRANSACTIONDEVASWOM'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_transactiondevaswom",
                            "reqtype" : "CREATETRANSACTIONREQ",
                            "methodtype" : "POST"
                        }

commonValues['LISTTRANSACTIONDEVASWOM'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_transactiondevaswom",
                            "reqtype" : "LISTTRANSACTIONDEVASWOMREQ",
                            "methodtype" : "POST"
                        }


#SUPER ADMIN---------------------------------------------------------------------------

commonValues['CREATEBANK'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_bank",
                            "reqtype" : "CREATEBANKREQ",
                            "methodtype" : "POST"
                        }

commonValues['LISTBANK'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_bank",
                            "reqtype" : "LISTBANKREQ",
                            "methodtype" : "POST"
                        }

commonValues['CREATEBANKADMIN'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_bankdadmin",
                            "reqtype" : "CREATEBANKADMINREQ",
                            "methodtype" : "POST"
                        }

commonValues['LISTBANKADMIN'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_bankdadmin",
                            "reqtype" : "LISTBANKADMINREQ",
                            "methodtype" : "POST"
                        }

commonValues['CREATECARDALLOCATION'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_cardallocation",
                            "reqtype" : "CREATECARDREQ",
                            "methodtype" : "POST"
                        }

commonValues['LISTCARDALLOCATION'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_cardallocation",
                            "reqtype" : "LISTCARDALLOCATIONREQ",
                            "methodtype" : "POST"
                        }

commonValues['CREATEREQUESTMONEY'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_reqmoney",
                            "reqtype" : "CREATEREQUESTMONEYREQ",
                            "methodtype" : "POST"
                        }

commonValues['CREATEFUNDTRANSFER'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_fundtransfer",
                            "reqtype" : "CREATEFUNDTRANSFERREQ",
                            "methodtype" : "POST"
                        }

commonValues['DROPDOWNDEVASWOM'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/dropdown_devaswom",
                            "reqtype" : "DROPDOWNDEVASWOMREQ",
                            "methodtype" : "POST"
                        }

commonValues['CREATELORDS'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_lords",
                            "reqtype" : "CREATELORDSREQ",
                            "methodtype" : "POST"
                        }

commonValues['LISTLORDS'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_lords",
                            "reqtype" : "LISTLORDSREQ",
                            "methodtype" : "POST"
                        }

commonValues['GETTRANSACTIONDEVASWOM'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/get_transactiondevaswom",
                            "reqtype" : "GETTRASNSACTIONDEVASWOMREQ",
                            "methodtype" : "POST"
                        }

commonValues['GETTRANSACTIONBANK'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/get_transactionbank",
                            "reqtype" : "GETTRASNSACTIONDBANKREQ",
                            "methodtype" : "POST"
                        }

commonValues['LISTTRANSACTIONBANK'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_transactionbank",
                            "reqtype" : "LISTTRASNSACTIONDBANKREQ",
                            "methodtype" : "POST"
                        }

commonValues['GETTRANSACTIONTEMPLE'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/get_transactiontemple",
                            "reqtype" : "GETTRASNSACTIONDTEMPLEREQ",
                            "methodtype" : "POST"
                        }

commonValues['LISTTRANSACTIONTEMPLE'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_transactiontemple",
                            "reqtype" : "LISTTRASNSACTIONTEMPLEREQ",
                            "methodtype" : "POST"
                        }

commonValues['CREATEBLOCKTEMPLE'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_blocktemple",
                            "reqtype" : "CREATEBLOCKTEMPLEREQ",
                            "methodtype" : "POST"
                        }

commonValues['LISTBLOCKTEMPLE'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_blocktemple",
                            "reqtype" : "LISTBLOCKTEMPLEREQ",
                            "methodtype" : "POST"
                        }

commonValues['CREATEBLOCKDEVASWOM'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_blockdevaswom",
                            "reqtype" : "CREATEBLOCKDEVASWOMREQ",
                            "methodtype" : "POST"
                        }

commonValues['LISTBLOCKDEVASWOM'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_blockdevaswom",
                            "reqtype" : "LISTBLOCKDEVASWOMREQ",
                            "methodtype" : "POST"
                        }

commonValues['CREATEBLOCKCUSTOMER'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_blockcustomer",
                            "reqtype" : "CREATEBLOCKCUSTOMERREQ",
                            "methodtype" : "POST"
                        }

commonValues['LISTBLOCKCUSTOMER'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_blockcustomer",
                            "reqtype" : "LISTBLOCKCUSTOMERREQ",
                            "methodtype" : "POST"
                        }

commonValues['CREATEBLOCKCARD'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_blockcard",
                            "reqtype" : "CREATEBLOCKCARDREQ",
                            "methodtype" : "POST"
                        }

commonValues['LISTBLOCKCARD'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_blockcard",
                            "reqtype" : "LISTBLOCKCARDREQ",
                            "methodtype" : "POST"
                        }

commonValues['CREATEBLOCKBANK'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_blockbank",
                            "reqtype" : "CREATEBLOCKBANKREQ",
                            "methodtype" : "POST"
                        }

commonValues['LISTBLOCKBANK'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_blockbank",
                            "reqtype" : "LISTBLOCKBANKREQ",
                            "methodtype" : "POST"
                        }


commonValues['LISTACCOUNTSTATEMENT'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_acctstatement",
                            "reqtype" : "LISTACCOUNTSTATEMENTREQ",
                            "methodtype" : "POST"
                        }

commonValues['DROPDOWNACTIVITYTYPE'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/dropdown_activitytype",
                            "reqtype" : "DROPDOWNACTIVITYTYPEREQ",
                            "methodtype" : "POST"
                        }

commonValues['SUPERDROPDOWNDEVASWOM'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/dropdown_superdevaswom",
                            "reqtype" : "SUPERDROPDOWNDEVASWOMREQ",
                            "methodtype" : "POST"
                        }

commonValues['SUPERDROPDOWNTEMPLE'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/dropdown_supertemple",
                            "reqtype" : "SUPERDROPDOWNTEMPLEREQ",
                            "methodtype" : "POST"
                        }

commonValues['CREATESUPERPOOJA'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_superpooja",
                            "reqtype" : "CREATESUPERPOOJAREQ",
                            "methodtype" : "POST"
                        }

commonValues['LISTSUPERPOOJA'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_superpooja",
                            "reqtype" : "LISTSUPERPOOJAREQ",
                            "methodtype" : "POST"
                        }