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

commonValues['CREATEBANK']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_bank",
                            "reqtype" : "CREATEBANK",
                            "methodtype" : "POST"

                            }

commonValues['LISTBANK']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_bank",
                            "reqtype" : "LISTBANK",
                            "methodtype" : "POST"

                            }

commonValues['CREATELORDS']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_lords",
                            "reqtype" : "CREATELORDS",
                            "methodtype" : "POST"

                            }

commonValues['CREATEPOOJA']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_pooja",
                            "reqtype" : "CREATEPOOJA",
                            "methodtype" : "POST"

                            }

commonValues['LIST_TOTAL']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_total",
                            "reqtype" : "LISTTOTAL",
                            "methodtype" : "POST"

                            }

commonValues['CREATECCOUNT']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_account",
                            "reqtype" : "CREATEACCOUNT",
                            "methodtype" : "POST"

                            }

commonValues['LISTACCOUNT']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_account",
                            "reqtype" : "LISTACCOUNT",
                            "methodtype" : "POST"

                            }

commonValues['CREATETRANSTEMP']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_transtemp",
                            "reqtype" : "CREATETRANSTEMP",
                            "methodtype" : "POST"

                            }

commonValues['LISTTRANSTEMP']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_transtemp",
                            "reqtype" : "LISTTRANSTEMP",
                            "methodtype" : "POST"

                            }

commonValues['CREATEDEVASWOM']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_devaswom",
                            "reqtype" : "CREATDEVASWOM",
                            "methodtype" : "POST"

                            }

commonValues['LISTDEVASWOM']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_devaswom",
                            "reqtype" : "LISTDEVASWOM",
                            "methodtype" : "POST"

                            }
                    
commonValues['CREATEBANKADMIN']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_bank_admin",
                            "reqtype" : "CREATEBANKADMIN",
                            "methodtype" : "POST"

                            }

commonValues['LISTMNGBANKADMIN']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_bank_admin",
                            "reqtype" : "LISTMNGBANKADMIN",
                            "methodtype" : "POST"

                            }

commonValues['CARDALLOCATE']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/card_allocate",
                            "reqtype" : "CARDALLOCATE",
                            "methodtype" : "POST"

                            }

commonValues['LISTCARDALLOCATE']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_card_allocate",
                            "reqtype" : "LISTCARDALLOCATE",
                            "methodtype" : "POST"

                            }

commonValues['CREATEBLOCKTEMPLE']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_block_temple",
                            "reqtype" : "CTREATEBLOCKTEMPLE",
                            "methodtype" : "POST"

                            }


commonValues['LISTBLOCKTEMPLE']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_block_temple",
                            "reqtype" : "LISTBLOCKTEMPLE",
                            "methodtype" : "POST"

                            }


commonValues['CREATEBLOCKDEVASWOM']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_block_devaswom",
                            "reqtype" : "CREATEBLOCKDEVASWOM",
                            "methodtype" : "POST"

                            }

commonValues['LISTBLOCKDEVASWOM']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_block_devaswom",
                            "reqtype" : "LISTBLOCKDEVASWOM",
                            "methodtype" : "POST"

                            }

commonValues['CREATEBLOCKCUSTOMER']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_block_customer",
                            "reqtype" : "CREATEBLOCKCUSTOMER",
                            "methodtype" : "POST"

                            }

commonValues['LISTBLOCKCUSTOMER']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_block_customer",
                            "reqtype" : "LISTBLOCKCUSTOMER",
                            "methodtype" : "POST"

                            }

commonValues['CREATEBLOCKCARD']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_block_card",
                            "reqtype" : "CREATEBLOCKCARD",
                            "methodtype" : "POST"

                            }

commonValues['LISTBLOCKCARD']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_block_card",
                            "reqtype" : "LISTBLOCKCARD",
                            "methodtype" : "POST"

                            }

commonValues['CREATEBLOCKBANK']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_block_bank",
                            "reqtype" : "CREATEBLOCKBANK",
                            "methodtype" : "POST"

                            }

commonValues['LISTBLOCKBANK']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_block_bank",
                            "reqtype" : "LISTBLOCKBANK",
                            "methodtype" : "POST"
                                }

                            