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

 #accountstatement (FINANCE ADMIN)                          
commonValues['ACCSTATEMENT']={
                                "server" : ipconstants.checkUser,
                                "headerz" : {"Content-Type":"application/json"},
                                "endpoint" : "/acc_statement",
                                "reqtype" : "ACCSTAMNT",
                                "methodtype" : "POST"

                           }

#activities_type (FINANCE ADMIN)
commonValues['ACTIVITYTYPE']={
                                "server" : ipconstants.checkUser,
                                "headerz" : {"Content-Type":"application/json"},
                                "endpoint" : "/activity_type",
                                "reqtype" : "ACCSTAMNT",
                                "methodtype" : "POST"

                                }

#pool_details(FINANCE ADMIN)
commonValues['POOLDETAILS']={
                                "server" : ipconstants.checkUser,
                                "headerz" : {"Content-Type":"application/json"},
                                "endpoint" : "/pooldetails",
                                "reqtype" : "ACCSTAMNT",
                                "methodtype" : "POST"

                                }

#fundtransfer(FINANCE ADMIN)
                                
commonValues['FUNDTRANSFER']={
                                "server" : ipconstants.checkUser,
                                "headerz" : {"Content-Type":"application/json"},
                                "endpoint" : "/fundtransfer",
                                "reqtype" : "FUNDTRNSFR",
                                "methodtype" : "POST"

                                }
                            

#select_devaswom_dropdwon(FINANCE ADMIN)                             
commonValues['SELECTDEVASWOM']={
                                "server" : ipconstants.checkUser,
                                "headerz" : {"Content-Type":"application/json"},
                                "endpoint" : "/select_devaswom",
                                "reqtype" : "SELECTDWSM",
                                "methodtype" : "POST"

                                }

#select_temple_dropdwon(FINANCE ADMIN)                             
commonValues['SELECTTEMPLE']={
                                "server" : ipconstants.checkUser,
                                "headerz" : {"Content-Type":"application/json"},
                                "endpoint" : "/select_temple",
                                "reqtype" : "SELECTTMPLE",
                                "methodtype" : "POST"

                                }

#requestmoney(FINANCE ADMIN)  
commonValues['REQUESTMONEY']={
                                "server" : ipconstants.checkUser,
                                "headerz" : {"Content-Type":"application/json"},
                                "endpoint" : "/requestmoney",
                                "reqtype" : "REQSTMNY",
                                "methodtype" : "POST"

                                }

#createpooja(TEMPLE ADMIN)
commonValues['CREATEPOOJA']={
                                "server" : ipconstants.checkUser,
                                "headerz" : {"Content-Type":"application/json"},
                                "endpoint" : "/createpooja",
                                "reqtype" : "CREPOOJA",
                                "methodtype" : "POST"

                                }
#listpooja(TEMPLE ADMIN)
commonValues['LISTPOOJA']={
                                "server" : ipconstants.checkUser,
                                "headerz" : {"Content-Type":"application/json"},
                                "endpoint" : "/listpooja",
                                "reqtype" : "LISTPOOJA",
                                "methodtype" : "POST"

                                }
#createprasadam(TEMPLE ADMIN)
commonValues['CREAPRASADAM']={
                                "server" : ipconstants.checkUser,
                                "headerz" : {"Content-Type":"application/json"},
                                "endpoint" : "/createprasadam",
                                "reqtype" : "CREAPRSDM",
                                "methodtype" : "POST"

                                }

#listprasadam(TEMPLE ADMIN)
commonValues['LISTPRASADAM']={
                                "server" : ipconstants.checkUser,
                                "headerz" : {"Content-Type":"application/json"},
                                "endpoint" : "/listprasadam",
                                "reqtype" : "LISTPRSDM",
                                "methodtype" : "POST"

                                }


#createofferings(TEMPLE ADMIN)
commonValues['CREAOFFERINGS']={
                                "server" : ipconstants.checkUser,
                                "headerz" : {"Content-Type":"application/json"},
                                "endpoint" : "/createofferings",
                                "reqtype" : "CREAOFFRNG",
                                "methodtype" : "POST"

                                }
#listofferings(TEMPLE ADMIN)
commonValues['LISTOFFERINGs']={
                                "server" : ipconstants.checkUser,
                                "headerz" : {"Content-Type":"application/json"},
                                "endpoint" : "/listofferings",
                                "reqtype" : "LSTOFFRNG",
                                "methodtype" : "POST"

                                }

