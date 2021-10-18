DB_NAME = 'temple'
ENCRYPTION_KEY = "WHENTHESKIESAREBLUESEEYOUONCEAGA"
# LOG_TABLE = 'log'
#user scheema
# SchemaConst=['api_name']+"Schema"
# print("||||||||||||||||||||||||||||||||||||",SchemaConst)
schemas = {}
#FINANCE ADMIN
schemas['templeloginapiSchema'] = {
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'modulename': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'username': {'type':'string'},
                     'password': {'type':'string'}},
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

schemas['accstatementapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'modulename': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'type':{'type':'all'}
                    
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}


schemas['activitytypeapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'modulename': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'type':{'type':'all'}
                    
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

schemas['pooldetailsapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'modulename': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'type':{'type':'all'}
                    
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

schemas['fundtransferapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'modulename': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'virtualaccno':{'type':'integer'},
                    'amount':{'type':'integer'},
                    'comment':{'type':'string'}
                    },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}



schemas['selectdevaswomapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'modulename': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata':  {'type':{'type':'all'}
                    
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}


schemas['selecttempleapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'modulename': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata':  {'type':{'type':'all'}
                    
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

schemas['requestmoneyapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'modulename': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata':  {'devaswom':{'type':'string'},
                    'temple':{'type':'string'},
                    'amount':{'type':'string'},
                    'comment':{'type':'string'}
                    
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}


#create_pooja(TEMPLE_ADMIN)
schemas['createpoojaapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'modulename': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata':  {'temple_id':{'type':'string'},
                    'pooja_amount':{'type':'integer'},
                    'pooja_description':{'type':'string'},
                    'pooja_name':{'type':'string'}
                    
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#list_pooja(TEMPLE_ADMIN)
schemas['listpoojaapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'modulename': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata':  {'pooja_id':{'type':'string'}
                   
                    
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#createprasadam(TEMPLE_ADMIN)

schemas['createprasadamapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'modulename': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata':  {'temple_id':{'type':'string'},
                    'prasadam_name':{'type':'string'},
                    'prasadam_amount':{'type':'string'},
                    'prasadam_count':{'type':'string'},
                    'prasadam_measure':{'type':'string'}
                    
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#listprasadam(TEMPLE_ADMIN)
schemas['listprasadamapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'modulename': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata':  {'prasadam_id':{'type':'string'}
                   
                    
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}




#create_offerings(TEMPLE_ADMIN)
schemas['createofferingsapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'modulename': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata':{'temple_id':{'type':'string'},
                    'offering_name':{'type':'string'},
                    'offering_amount':{'type':'string'},
                    'offering_description':{'type':'string'}
                    
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#super_admin

#create_bank
schemas['createbankapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'bankname': {'type':'string'},
                     'ifsc': {'type':'string'},
                     'mail': {'type':'string'},
                     'phone': {'type':'string'},
                     'addrs1': {'type':'string'},
                     'addrs2': {'type':'string'},
                     'state': {'type':'string'},
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#list_bank

schemas['listbankapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'list': {'type':'string'},
                     
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#create_lords

schemas['createlordsapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'dietyname': {'type':'string'},
                     'dietyDescrip': {'type':'string'},
                     'deityTemple': {'type':'string'},
                     'file': {'type':'string'}
                     
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

    #list_lords

schemas['listlordsapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'list': {'type':'string'},
                     
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#create_pooja

schemas['createpoojaapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'poojaname': {'type':'string'},
                     'poojaDescrip': {'type':'string'},
                     'amount': {'type':'string'}
                     
                      },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

    #list_total


schemas['list_totalapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': 
                    {'list': {'type':'string'},
                     
                     
                      },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#create_account

schemas['createaccountapichema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': 
                   {'bankname': {'type':'string'},
                     'ifsc': {'type':'string'},
                     'date1': {'type':'string'},
                     'date2': {'type':'string'}
                     
                      },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}


#list_account

schemas['listaccountapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': 
                   {'list': {'type':'string'},
                
                      },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#createtranstemp

schemas['createtranstempapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': 
                   {'devaswom': {'type':'string'},
                     'temple': {'type':'string'},
                     'comment': {'type':'string'},
                     
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#list trans 

schemas['listtranstempapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': 
                   {'list': {'type':'string'},
                     
                     
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#create_devaswom

schemas['createdevaswomapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': 
                   {'devaswom': {'type':'string'},
                   'date':{'type':'string'}
                     
                     
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#list_devaswom

schemas['listevaswomapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': 
                   {'list': {'type':'string'}
                     
                     
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

 #create_bank_admin

schemas['createbankadminapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': 
                   {'list': {'type':'string'}
                     
                     
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}


#list_manage_bank_admin_schema

schemas['list_manage_bank_admin_apiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': 
                   {'list': {'type':'string'}
                     
                     
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#card_allocate_schema

schemas['card_allocate_apiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': 
                   {'count': {'type':'string'},
                   'devaswom': {'type':'string'},
                   'temple': {'type':'string'}
                     
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#list_card_allocate_schema

schemas['list_card_allocate_apiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': 
                   {'list': {'type':'string'}
                     
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#create_block_temple

schemas['create_block_temple_apiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': 
                   {'devaswom': {'type':'string'},
                   'temple': {'type':'string'},
                   'comment':{'type':'string'}
                     
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#list_block_temple

schemas['list_block_temple_apiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': 
                   {'list': {'type':'string'}
                     
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#create_block_devaswom


schemas['create_block_devaswom_apiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': 
                   {'devaswom': {'type':'string'},
                   'comment': {'type':'string'}
                     
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#list_block_devaswom

schemas['list_block_devaswom_apiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': 
                   {'list': {'type':'string'}
                     
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#create_block_customer

schemas['create_block_customerbeSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': 
                   {'phonenum': {'type':'string'},
                   'name': {'type':'string'},
                   'email': {'type':'string'}
                     
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#list_block_customer_Schema

schemas['list_block_customer_apiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': 
                   {'list': {'type':'string'}
                     
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#create_block_card

schemas['create_block_cardrapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': 
                   {'phonenum': {'type':'string'},
                   'cardnum': {'type':'string'},
                   'comment': {'type':'string'}
                     
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#list_block_card

schemas['list_block_card_apiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': 
                   {'list': {'type':'string'}
                     
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#create_block_bank

schemas['create_block_bank_apiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': 
                   {'bank': {'type':'string'},
                   'comment': {'type':'string'}
                     
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#list_block_bank

schemas['list_block_bank_apiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': 
                   {'list': {'type':'string'}
                     
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#list_offerings(TEMPLE_ADMIN)
schemas['listofferingsapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'modulename': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata':  {'offering_id':{'type':'string'}
                   },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}


