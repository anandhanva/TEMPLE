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
                            "checkUserReqType":"/checkuserLogin",
                            "checkUserMethodType":"LOGINREQ",
                            "checkUserEndpoint":"POST"
                            }

commonValues['HASH_MO'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.hashServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/hashrequest",
                            "reqtype" : "HASHREQ",
                            "methodtype" : "POST"
                        }
                    