DB_NAME = 'temple'
ENCRYPTION_KEY = "WHENTHESKIESAREBLUESEEYOUONCEAGA"
# LOG_TABLE = 'log'
#user scheema
userSchema = {
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'username': {'type':'string'},
                     'password': {'type':'string'}},
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
'hashstr': {'type':'string'},    'checksum': {'type':'string'}}

templelistSchema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'address': {'type':'string'},
                     'lattitude': {'type':'string'},
                     'longitude': {'type':'string'},
                     'vintage': {'type':'string'},
                     'foundation day': {'type':'string'},
                     'Description': {'type':'string'}
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
'hashstr': {'type':'string'},    'checksum': {'type':'string'}}


templeadminSchema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'address': {'type':'string'},
                     'lattitude': {'type':'string'},
                     'longitude': {'type':'string'},
                     'vintage': {'type':'string'},
                     'foundation day': {'type':'string'},
                     'Description': {'type':'string'}
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
'hashstr': {'type':'string'},    'checksum': {'type':'string'}}

#devaswom add temple 

devaswomaddtempleschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'d_templename': {'type':'string'},
                     'd_address1': {'type':'string'},
                     'd_address2': {'type':'string'},
                     'd_address3': {'type':'string'},
                     'd_lattitude': {'type':'string'},
                     'd_longitude': {'type':'string'},
                     'd_vintage': {'type':'string'},
                     'd_found': {'type':'string'},
                     'prasadham_desc': {'type':'string'}

                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
'hashstr': {'type':'string'},    'checksum': {'type':'string'}}

#devaswom block temple 

devaswomblocktempleschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'prasadham_counts': {'type':'string'},
                     'd_comment': {'type':'string'}
                    
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
'hashstr': {'type':'string'},    'checksum': {'type':'string'}}

#devaswom block temple admin

devaswomblocktempleadminschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'tmpname': {'type':'string'},
                     'ad_name': {'type':'string'}
                    
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
'hashstr': {'type':'string'},    'checksum': {'type':'string'}}

#create finance admin

financeadminschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'tmpname': {'type':'string'},
                    'ad_name': {'type':'string'},
                    'd_add1': {'type':'string'},
                    'd_add2': {'type':'string'},
                    'd_state': {'type':'string'},
                    'bank_name': {'type':'string'},
                    'd_accno': {'type':'string'},
                    'ifsc': {'type':'string'}

                    
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
'hashstr': {'type':'string'},    'checksum': {'type':'string'}}

#create temple admin devaswom

createtempleadminschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'tmp_name': {'type':'string'},
                    'ad_name': {'type':'string'},
                     'contact': {'type':'string'},
                     'd_email': {'type':'string'},'d_add1': {'type':'string'},
                    'd_add2': {'type':'string'},
                    'd_state': {'type':'string'},
                    'd_state': {'type':'string'}
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
'hashstr': {'type':'string'},    'checksum': {'type':'string'}}

#create account devaswom

createaccdevschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'tmp_name': {'type':'string'},
                    'bank_name': {'type':'string'},
                     'acc_no': {'type':'string'},
                     'ifsc': {'type':'string'},
                     'd_add1': {'type':'string'},
                    'd_add1': {'type':'string'}},
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
'hashstr': {'type':'string'},    'checksum': {'type':'string'}}
#list add temple

listtempleschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {},
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
'hashstr': {'type':'string'},    'checksum': {'type':'string'}}
#list block temple

listblocktempleschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'prasadham_counts': {'type':'string'},
                     'd_comment': {'type':'string'}},
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
'hashstr': {'type':'string'},    'checksum': {'type':'string'}}

#list block admin

listblockadminschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'tmpname': {'type':'string'},
                     'ad_name': {'type':'string'}},
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
'hashstr': {'type':'string'},    'checksum': {'type':'string'}}

#list fin admin

listfinadminschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'tmpname': {'type':'string'},
                    'ad_name': {'type':'string'},
                    'd_add1': {'type':'string'},
                    'd_add2': {'type':'string'},
                    'd_state': {'type':'string'},
                    'bank_name': {'type':'string'},
                    'd_accno': {'type':'string'},
                    'ifsc': {'type':'string'}},
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
'hashstr': {'type':'string'},    'checksum': {'type':'string'}}
#create fin admin

listtempleadminschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {
                   },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
'hashstr': {'type':'string'},    'checksum': {'type':'string'}}

#list account devaswom

listaccdevasschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'tmp_name': {'type':'string'},
                    'bank_name': {'type':'string'},
                     'acc_no': {'type':'string'},
                     'ifsc': {'type':'string'},
                     'd_add1': {'type':'string'},
                    'd_add1': {'type':'string'}
                   },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
'hashstr': {'type':'string'},    'checksum': {'type':'string'}}

#temple data by virtual acc number

tempdatavaschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': { 'acc_no': {'type':'string'}
                   },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
'hashstr': {'type':'string'},    'checksum': {'type':'string'}}

#move money to devaswom

movemoneyschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': { 'dev_name': {'type':'string'},
                    'tmpname': {'type':'string'},
                     'vano': {'type':'string'},
                       'amount': {'type':'string'},
                        'comment': {'type':'string'}},
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
'hashstr': {'type':'string'},    'checksum': {'type':'string'}}

#moneyload list

moneyloadschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'dev_name': {'type':'string'},
                    'tmpname': {'type':'string'},
                     'vano': {'type':'string'},
                      'acc_no': {'type':'string'},
                       'amount': {'type':'string'},
                        'comment': {'type':'string'} },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
'hashstr': {'type':'string'},    'checksum': {'type':'string'}}

#withdraw details

withdrawdetsschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': { },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
'hashstr': {'type':'string'},    'checksum': {'type':'string'}}

#temple details by id

tempdetbyidsschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': { 
        'temp_id': {'type':'string'}
    },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
'hashstr': {'type':'string'},    'checksum': {'type':'string'}}

#devaswom fund transfer

fundtxnschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': { 
        'tmpname': {'type':'string'},
         'vano': {'type':'string'},
          'amount': {'type':'string'},
           'comment': {'type':'string'}

    },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
'hashstr': {'type':'string'},    'checksum': {'type':'string'}}

#select temple admin

selecttempleadminschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': { 
        
    },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
'hashstr': {'type':'string'},    'checksum': {'type':'string'}}

#select bank

selectbankschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': { 
        
    },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
'hashstr': {'type':'string'},    'checksum': {'type':'string'}}

#create devaswom admin
credevadminschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': { 'devsom_option': {'type':'string'},
                    'devadmin_name': {'type':'string'},
                    'dev_phone': {'type':'string'},
                    'email': {'type':'string'},
                    'addressline1': {'type':'string'},
                    'addressline2': {'type':'string'},
                    'state': {'type':'string'}},
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
'hashstr': {'type':'string'},    'checksum': {'type':'string'}}

#list devaswom admin
listdevadminschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': { 'devsom_option': {'type':'string'},
                    'devadmin_name': {'type':'string'},
                    'dev_phone': {'type':'string'},
                    'email': {'type':'string'},
                    'addressline1': {'type':'string'},
                    'addressline2': {'type':'string'},
                    'state': {'type':'string'}},
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
'hashstr': {'type':'string'},    'checksum': {'type':'string'}}

#create acc statement
creaccstatementschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': { 'date': {'type':'string'},
                    'accno': {'type':'string'},
                    'credit': {'type':'string'},
                    'debit': {'type':'string'},
                    'remainingamt': {'type':'string'}
                    },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
'hashstr': {'type':'string'},    'checksum': {'type':'string'}}

#list acc statement
listaccstatementschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': { 'date': {'type':'string'},
                    'accno': {'type':'string'},
                    'credit': {'type':'string'},
                    'debit': {'type':'string'},
                    'remainingamt': {'type':'string'}
                    },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
'hashstr': {'type':'string'},    'checksum': {'type':'string'}}

#create devaswom
createdevaswomschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': { 'devname': {'type':'string'},
                    'email': {'type':'string'},
                    'address': {'type':'string'},
                    'contactno': {'type':'string'},
                    'ifsc': {'type':'string'}
                    },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
'hashstr': {'type':'string'},    'checksum': {'type':'string'}}

#list devaswom
listdevaswomschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': { 'devname': {'type':'string'},
                    'email': {'type':'string'},
                    'address': {'type':'string'},
                    'contactno': {'type':'string'},
                    'ifsc': {'type':'string'}
                    },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
'hashstr': {'type':'string'},    'checksum': {'type':'string'}}

#forgot pin by phone
pinbyphoneschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': { 'phone': {'type':'string'}
                    
                    },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#forgot pin request
pinbyreqschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': { 'phone': {'type':'string'},
                    'number': {'type':'string'},
                    'cardno': {'type':'string'}
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#fund transfer
fundtransSchema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': { 'bank': {'type':'string'},
                    'accno': {'type':'string'},
                    'ifsc': {'type':'string'},
                     'amount': {'type':'string'}
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#list fund transfer
listfundtransSchema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': { 'bank': {'type':'string'},
                    'accno': {'type':'string'},
                    'ifsc': {'type':'string'},
                     'amount': {'type':'string'}
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#load pool
loadpoolschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': { 'devsom': {'type':'string'},
                    'accno': {'type':'string'},
                    'comment': {'type':'string'},
                     'amount': {'type':'string'}
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#list load pool
listloadpoolschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': { 'devsom': {'type':'string'},
                    'accno': {'type':'string'},
                    'comment': {'type':'string'},
                     'amount': {'type':'string'}
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#select bank dropdown
selectbankschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': { 'devsom': {'type':'string'},
                    'accno': {'type':'string'},
                    'comment': {'type':'string'},
                     'amount': {'type':'string'}
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}
#select devsom dropdown
selectdevsomschema={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': { 
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

