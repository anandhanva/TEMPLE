from b_core.statics.urlconstants import LOGIN
from b_core.statics import ipconstants


commonValues = {}


commonValues['HASH_MO'] = {
                            # "modulename":"checkUser",
                            "server" : ipconstants.hashServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/hashrequest",
                            "reqtype" : "HASHREQ",
                            "methodtype" : "POST"
                        }
#LOGIN
commonValues['LOGIN'] = {
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/login",
                            "reqtype" : "LOGINREQ",
                            "methodtype" : "POST"
                        }

#otpVerification
commonValues['OTPVERIFICATION'] = {
                            "server" : ipconstants.templeBcoreServers,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/otpverification",
                            "reqtype" : "OTPVERIFICATIONREQ",
                            "methodtype" : "POST"
                        }
