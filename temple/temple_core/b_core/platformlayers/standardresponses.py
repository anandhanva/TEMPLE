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
                    