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