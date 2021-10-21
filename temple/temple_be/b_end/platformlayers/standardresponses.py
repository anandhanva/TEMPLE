from b_end.statics.urlconstants import LOGIN
from b_end.statics import ipconstants
commonValues = {}
commonValues['LOGIN'] = {
                            
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


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#USER API

#index
commonValues['INDEX']={
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/index",
                            "reqtype" : "INDEX",
                            "methodtype" : "POST"
                                }

#user kanikka
commonValues['USERKANIKKA']={
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/user_kanikka",
                            "reqtype" : "USRKANIKKA",
                            "methodtype" : "POST"
                                }
#get_star drop

commonValues['GETSTARDROP']={
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/get_stardrop",
                            "reqtype" : "GETSTRDRP",
                            "methodtype" : "POST"
                                }

#get_prasadam_bill_list


commonValues['GETPRASADAMBILL']={
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/get_prasadambill",
                            "reqtype" : "GETPRSDMBLLST",
                            "methodtype" : "POST"
                                }
#user_list_kanikka

commonValues['USERLISTKANIKKA']={
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/userlist_kanikka",
                            "reqtype" : "USRLSTKANIKKA",
                            "methodtype" : "POST"
                                }

#history

commonValues['HISTORY']={
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/history",
                            "reqtype" : "HISTORY",
                            "methodtype" : "POST"
                                }
#pooja bill

commonValues['POOJABILL']={
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/pooja_bill",
                            "reqtype" : "POOJABL",
                            "methodtype" : "POST"
                                }
#kanikka_pay
 

commonValues['KANIKKAPAY']={
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/kanikka_pay",
                            "reqtype" : "KANPAY",
                            "methodtype" : "POST"
                                }
#offer_bill

commonValues['OFFERINGBILL']={
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/kanikka_pay",
                            "reqtype" : "KANPAY",
                            "methodtype" : "POST"
                                }
#nearby_attraction
commonValues['NEARBYATRCTIN']={
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/nearby_attraction",
                            "reqtype" : "NERBYATRCTIN",
                            "methodtype" : "POST"
                                }
#neareststay

commonValues['NEARESTSTAY']={
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/nearest_stay",
                            "reqtype" : "NERSTAY",
                            "methodtype" : "POST"
                                }


#lord
commonValues['LORD']={
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/lord",
                            "reqtype" : "LORD",
                            "methodtype" : "POST"
                                }




































