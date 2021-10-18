DB_NAME = 'temple'
ENCRYPTION_KEY = "WHENTHESKIESAREBLUESEEYOUONCEAGA"
# LOG_TABLE = 'log'
#user scheema

#FINANCE ADMIN
userSchema = {
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

AccStatementSchema={
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


ActivitiedropSchema={
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

pooldetailsSchema={
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

fundtransferSchema={
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



selectdevaswomSchema={
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


selecttempleSchema={
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

requestmoneySchema={
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
createpoojaSchema={
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
listpoojaSchema={
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

createprasadamSchema={
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
listprasadamSchema={
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
createofferingsSchema={
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

#list_offerings(TEMPLE_ADMIN)
listofferingsSchema={
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


