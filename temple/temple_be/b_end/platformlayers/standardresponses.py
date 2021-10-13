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
commonValues['TEMPLELIST']={
                        
                            "server" : ipconstants.checkUser,
                            "headerz" : {"Content-Type":"application/json"},
                            "endpoint" : "/temple_list",
                            "reqtype" : "TEMPLIST",
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




