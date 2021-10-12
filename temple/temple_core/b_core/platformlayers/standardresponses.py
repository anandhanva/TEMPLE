from b_core.statics.urlconstants import LOGIN
from b_core.statics import ipconstants


commonValues = {}
commonValues['LOGIN'] = {
                            "modulename":"checkUser",
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/user",
                            "reqtype" : "LOGINREQ",
                            "methodtype" : "POST"
                        }
commonValues['CORELOGIN']={
                            "checkUserServer": "",
                            "checkUserHeader":"",
                            "checkUserReqType":"",
                            "checkUserMethodType":"",
                            "checkUserEndpoint":"/"
                            }
                    