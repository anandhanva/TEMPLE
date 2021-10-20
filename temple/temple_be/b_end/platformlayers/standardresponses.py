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
                                "endpoint" : "/create_pooja",
                                "reqtype" : "CREPOOJA",
                                "methodtype" : "POST"

                                }
#listpooja(TEMPLE ADMIN)
commonValues['LISTPOOJA']={
                                "server" : ipconstants.checkUser,
                                "headerz" : {"Content-Type":"application/json"},
                                "endpoint" : "/list_pooja",
                                "reqtype" : "LISTPOOJA",
                                "methodtype" : "POST"

                                }
#createprasadam(TEMPLE ADMIN)
commonValues['CREAPRASADAM']={
                                "server" : ipconstants.checkUser,
                                "headerz" : {"Content-Type":"application/json"},
                                "endpoint" : "/create_prasadam",
                                "reqtype" : "CREAPRSDM",
                                "methodtype" : "POST"

                                }

#listprasadam(TEMPLE ADMIN)
commonValues['LISTPRASADAM']={
                                "server" : ipconstants.checkUser,
                                "headerz" : {"Content-Type":"application/json"},
                                "endpoint" : "/list_prasadam",
                                "reqtype" : "LISTPRSDM",
                                "methodtype" : "POST"

                                }


#createofferings(TEMPLE ADMIN)
commonValues['CREAOFFERINGS']={
                                "server" : ipconstants.checkUser,
                                "headerz" : {"Content-Type":"application/json"},
                                "endpoint" : "/create_offerings",
                                "reqtype" : "CREAOFFRNG",
                                "methodtype" : "POST"

                                }
#listofferings(TEMPLE ADMIN)
commonValues['LISTOFFERINGS']={
                                "server" : ipconstants.checkUser,
                                "headerz" : {"Content-Type":"application/json"},
                                "endpoint" : "/list_offerings",
                                "reqtype" : "LSTOFFRNG",
                                "methodtype" : "POST"
}
#Add Rate (TEMPLE ADMIN)
commonValues['ADDRATE']={
                                "server" : ipconstants.checkUser,
                                "headerz" : {"Content-Type":"application/json"},
                                "endpoint" : "/add_rate",
                                "reqtype" : "ADRATE",
                                "methodtype" : "POST"
}
#list rate (TEMPLE ADMIN)
commonValues['LISTRATE']={
                                "server" : ipconstants.checkUser,
                                "headerz" : {"Content-Type":"application/json"},
                                "endpoint" : "/list_rate",
                                "reqtype" : "LSTRATE",
                                "methodtype" : "POST"
}
###############################################################################################################################
#REPORT BY DIETY
commonValues['REPDIETY']={
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/rep_diety",
                            "reqtype" : "REPDIETY",
                            "methodtype" : "POST"
                                }
#REPORT BY DATE
commonValues['REPDATE']={
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/rep_date",
                            "reqtype" : "REPDATE",
                            "methodtype" : "POST"
                                }
#REPORT BY customer city
commonValues['REPCUSTCITY']={
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/rep_custcity",
                            "reqtype" : "REPCUSTCITY",
                            "methodtype" : "POST"
                                }
#INVOICE VIEW
commonValues['INVOICEVIEW']={
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/invoice_view",
                            "reqtype" : "INVOICEVIEW",
                            "methodtype" : "POST"
                                }
#INVOICE LIST
commonValues['INVOICELIST']={
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/invoice_list",
                            "reqtype" : "INVOICELIST",
                            "methodtype" : "POST"
                                }
#INVOICE SEARCH
commonValues['INVOICELIST']={
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/invoice_search",
                            "reqtype" : "INVOICESEARCH",
                            "methodtype" : "POST"
                                }
#create parking
commonValues['CREPARKING']={
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_parking",
                            "reqtype" : "CREPARKING",
                            "methodtype" : "POST"
                                }
#list parking
commonValues['LISTPARKING']={
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_parking",
                            "reqtype" : "LISTPARKING",
                            "methodtype" : "POST"
                                }
#create sightseeing
commonValues['CRESIGHTSEEING']={
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_sightseeing",
                            "reqtype" : "CRESIGHTSEEING",
                            "methodtype" : "POST"
                                }
#list SIGHTSEEING
commonValues['LISTSIGHTSEEING']={
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_sightseeing",
                            "reqtype" : "LISTSIGHTSEEING",
                            "methodtype" : "POST"
                                }
#drop diety
commonValues['DROPDOWNDIETY']={
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/drop_diety",
                            "reqtype" : "DROPDIETY",
                            "methodtype" : "POST"
                                }
#drop RATE
commonValues['DROPDOWNRATE']={
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/drop_rate",
                            "reqtype" : "DROPRATE",
                            "methodtype" : "POST"
                                }



























































#################################################################################################################################

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
#super admin
commonValues['LISTTOTAL']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_total",
                            "reqtype" : "LISTTOTAL",
                            "methodtype" : "POST"

                            }
#super admin
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
#devaswom add temple
commonValues['devaaddtemple'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/devaddtemple",
                            "reqtype" : "devaddt",
                            "methodtype" : "POST"
}

#devaswom block temple
commonValues['devablocktemple'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/devblocktemple",
                            "reqtype" : "devblockt",
                            "methodtype" : "POST"
}
#devaswom block temple admin
commonValues['devablocktempleadmin'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/devblocktempleadmin",
                            "reqtype" : "devblocktadmin",
                            "methodtype" : "POST"
}
#create finance admin
commonValues['crefinanceadmin'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/crefinadmin",
                            "reqtype" : "crefinaadmin",
                            "methodtype" : "POST"}
#create temple admin
commonValues['cretempleadmin'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/cretemadmin",
                            "reqtype" : "cretempleaadmin",
                            "methodtype" : "POST"}
#create account devaswom
commonValues['creaccdevas'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/creaccdev",
                            "reqtype" : "creaccdevaswom",
                            "methodtype" : "POST"}
#list add temple 
commonValues['listaddtemple'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/listaddtemple",
                            "reqtype" : "listaddtemple",
                            "methodtype" : "POST"}
#list block temple 
commonValues['listblocktemple'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/listblocktemple",
                            "reqtype" : "listblocktemple",
                            "methodtype" : "POST"}
#list block admin  
commonValues['listblockadmin'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/listblockadmin",
                            "reqtype" : "listblockadmin",
                            "methodtype" : "POST"}
#list fin admin 
commonValues['listfinadmin'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/listfinadmin",
                            "reqtype" : "listfinadmin",
                            "methodtype" : "POST"}
#create fin admin 
commonValues['createfinadmin'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/createfinadmin",
                            "reqtype" : "createfinadmin",
                            "methodtype" : "POST"}

#list account devaswom
commonValues['listaccdevas'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/listaccdev",
                            "reqtype" : "listaccdevaswom",
                            "methodtype" : "POST"}
#temple details by virtual acc number
commonValues['get_tmpdata_byva'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/tmpdatabyva",
                            "reqtype" : "tmpdatabyviracc",
                            "methodtype" : "POST"}
#move money to devaswom
commonValues['move_ moneyto_dev'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/movemoney",
                            "reqtype" : "movemoneydev",
                            "methodtype" : "POST"}

#money load list
commonValues['moneyload_list'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/moneyload",
                            "reqtype" : "moveloadlist",
                            "methodtype" : "POST"}

#withdraw details
commonValues['withdraw_dets'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/withdrawdets",
                            "reqtype" : "moveloadlist",
                            "methodtype" : "POST"}

#get temple details by id
commonValues['get_tempdata_byid'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/tempdetbyid",
                            "reqtype" : "temdetid",
                            "methodtype" : "POST"}
#devaswom fund transfer
commonValues['dvsm_fundtxn'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/fundtxn",
                            "reqtype" : "fundtxndevaswom",
                            "methodtype" : "POST"}
#select temple admin dropdown
commonValues['select_tmpadmin'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/selecttempleadmin",
                            "reqtype" : "selecttempleadmin",
                            "methodtype" : "POST"}
#select bank
commonValues['select_bank'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/selectbank",
                            "reqtype" : "selectbank",
                            "methodtype" : "POST"}
#create devaswom admin
commonValues['createdevadmin'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/credevadmin",
                            "reqtype" : "credevadmin",
                            "methodtype" : "POST"}
#list devaswom admin
commonValues['listdevadmin'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/listdevadmin",
                            "reqtype" : "listdevadmin",
                            "methodtype" : "POST"}
#create acc statement
commonValues['createaccountstatement'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/creaccstatement",
                            "reqtype" : "creaccstatement",
                            "methodtype" : "POST"}

#list acc statement
commonValues['listaccountstatement'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/listaccstatement",
                            "reqtype" : "listaccstatement",
                            "methodtype" : "POST"}
#create devaswom
commonValues['createdevaswom'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/credevaswom",
                            "reqtype" : "credevaswom",
                            "methodtype" : "POST"}
#list devaswom
commonValues['listdevaswom'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/listdevaswom",
                            "reqtype" : "listdevaswom",
                            "methodtype" : "POST"}
#frogot pin by phone
commonValues['forgotpinbyphone'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/forpinphone",
                            "reqtype" : "forpinphone",
                            "methodtype" : "POST"}
#frogot pin request
commonValues['forgotpinrequest'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/forpinreq",
                            "reqtype" : "forpinreq",
                            "methodtype" : "POST"}
#fund transfer
commonValues['fundtrans'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/fundtrans",
                            "reqtype" : "fundtrans",
                            "methodtype" : "POST"}
#list fund transfer
commonValues['fundtrans'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/listfundtrans",
                            "reqtype" : "listfundtrans",
                            "methodtype" : "POST"}

#load pool
commonValues['loadpool'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/loadpool",
                            "reqtype" : "loadpool",
                            "methodtype" : "POST"}
#list load pool
commonValues['listloadpool'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/listloadpool",
                            "reqtype" : "listloadpool",
                            "methodtype" : "POST"}

#select bank drop
commonValues['selectbank'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/selectbank",
                            "reqtype" : "selectbank",
                            "methodtype" : "POST"}
#select devsom drop
commonValues['selectbank'] = {
                            
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/selectdevsom",
                            "reqtype" : "selectdevsom",
                            "methodtype" : "POST"}




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
            
commonValues['CREDIETY']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_diety",
                            "reqtype" : "CREDIETY",
                            "methodtype" : "POST"
                                }

commonValues['LISTDIETY']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_diety",
                            "reqtype" : "LISTDIETY",
                            "methodtype" : "POST"
                                }

commonValues['CREHISTORY']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/cre_history",
                            "reqtype" : "CREHISTORY",
                            "methodtype" : "POST"
                                }
#REPORT BY DIETY
commonValues['REPDIETY']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/rep_diety",
                            "reqtype" : "REPDIETY",
                            "methodtype" : "POST"
                                }

#REPORT BY DATE
commonValues['REPDATE']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/rep_date",
                            "reqtype" : "REPDATE",
                            "methodtype" : "POST"
                                }

#REPORT BY customer city
commonValues['REPCUSTCITY']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/rep_custcity",
                            "reqtype" : "REPCUSTCITY",
                            "methodtype" : "POST"
                                }

#INVOICE VIEW
commonValues['INVOICEVIEW']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/invoice_view",
                            "reqtype" : "INVOICEVIEW",
                            "methodtype" : "POST"
                                }

#INVOICE LIST
commonValues['INVOICELIST']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/invoice_list",
                            "reqtype" : "INVOICELIST",
                            "methodtype" : "POST"
                                }

#INVOICE SEARCH
commonValues['INVOICELIST']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/invoice_search",
                            "reqtype" : "INVOICESEARCH",
                            "methodtype" : "POST"
                                }
#create parking
commonValues['CREPARKING']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_parking",
                            "reqtype" : "CREPARKING",
                            "methodtype" : "POST"
                                }
#list parking
commonValues['LISTPARKING']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_parking",
                            "reqtype" : "LISTPARKING",
                            "methodtype" : "POST"
                                }
#create sightseeing
commonValues['CRESIGHTSEEING']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_sightseeing",
                            "reqtype" : "CRESIGHTSEEING",
                            "methodtype" : "POST"
                                }
#list SIGHTSEEING
commonValues['LISTSIGHTSEEING']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/list_sightseeing",
                            "reqtype" : "LISTSIGHTSEEING",
                            "methodtype" : "POST"
                                }
                            
#drop diety
commonValues['DROPDOWNDIETY']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/drop_diety",
                            "reqtype" : "DROPDIETY",
                            "methodtype" : "POST"
                                }
#drop RATE
commonValues['DROPDOWNRATE']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/drop_rate",
                            "reqtype" : "DROPRATE",
                            "methodtype" : "POST"
                                

}
#create diety temple admin
commonValues['CREATEDIETY']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/create_diety",
                            "reqtype" : "DROPRATE",
                            "methodtype" : "POST"
                                

}
###################################################################################################33