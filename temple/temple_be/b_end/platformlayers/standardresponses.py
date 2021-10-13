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