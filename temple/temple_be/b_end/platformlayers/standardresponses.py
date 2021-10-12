from b_end.statics.urlconstants import LOGIN
from b_end.statics import ipconstants
commonValues = {}
commonValues['LOGIN'] = {
                            "modulename":"checkUser",
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/user",
                            "reqtype" : "LOGINREQ",
                            "methodtype" : "POST"
                        }
commonValues['CORELOGIN']={
                            "checkUserServer":  ipconstants.checkUser,
                            "checkUserHeader":{"Content-Type":"application/json"},
                            "checkUserReqType":"",
                            "checkUserMethodType":"POST",
                            "checkUserEndpoint":"/user"
                            }
commonValues['TEMPLELIST']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/temple_list",
                            "reqtype" : "TEMPLIST",
                            "methodtype" : "POST"

                            }


