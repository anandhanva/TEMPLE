DB_NAME = 'temple'
ENCRYPTION_KEY = "WHENTHESKIESAREBLUESEEYOUONCEAGA"
USER_NOT_EXIST = {"Error-Response":"USER NOT FOUND"}
INVALID_USER_PASS = {"Error-Response":"Invalid USERNAME, PASSWORD"}

# LOG_TABLE = 'log'
schemas = {}

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
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

# ADD TEMPLE SCHEMA
addTempleSchema = {
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"}, 
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {"d_templename":{'type':'string'},
                        "d_address1":{'type':'string'} ,
                        "d_address2":{'type':'string'},
                        "d_address3":{'type':'string'},
                        "d_lattitude":{'type':'string'},
                        "d_longitude":{'type':'string'},
                        "d_vintage":{'type':'string'},
                        "d_found":{'type':'string'},
                        "prasadham_desc":{'type':'string'}},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

accStatementSchema={
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
    'hasstr': {'type':'string'},
    'checksum': {'type':'string'}}

listTempleSchema = {
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"}, 
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {
        "type":"all"
        },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}


addTempleAdminSchema = {
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"}, 
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {"tmp_name":{'type':'string'},
                        "ad_name":{'type':'string'} ,
                        "contact":{'type':'string'},
                        "d_email":{'type':'string'},
                        "d_add1":{'type':'string'},
                        "d_add2":{'type':'string'},
                        "d_state":{'type':'string'},
                        },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

listTempleAdminSchema = {
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"}, 
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {"list":{"type":"all"}
                        },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}
createAccountSchema = {
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"}, 
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {"tmp_name":{'type':'string'},
                        "bank_name":{'type':'string'} ,
                        "acc_no":{'type':'string'},
                        "ifsc":{'type':'string'},
                        "d_add1":{'type':'string'},
                        },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}
listAccountSchema = {
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"}, 
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {"list":{"type":"all"}
                        },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},


    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}


createFinAccountSchema = {
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"}, 
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': { "tmpname": {'type':'string'},        
        "ad_name": {'type':'string'},
        "d_email": {'type':'string'},
        "d_add1": {'type':'string'},        
        "d_add2": {'type':'string'},
        "d_state": {'type':'string'},         
        "bank_name": {'type':'string'},        
        "d_accno": {'type':'string'},
        "ifsc": {'type':'string'},
                        },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}


schemas['templecreatepoojaapiSchema'] = {
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"}, 
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': { "pooja_id": {'type':'integer'},        
        "pooja_rateid": {'type':'integer'},
        "pooja_descr": {'type':'string'},
        "pooja_name": {'type':'string'},        
                        },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}
schemas['templelistpoojaapiSchema'] = {
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"}, 
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {"type":"all"
                        },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},


    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}



schemas['templecreateofferingapiSchema'] = {
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"}, 
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': { "templeid": {'type':'integer'},        
        "offering_name": {'type':'string'},
        "offering_amount": {'type':'integer'},
        "offering_description": {'type':'string'},        
                        },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

schemas['templelistofferingapi'] = {
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"}, 
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {"type":"all"
                        },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},


    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

schemas['templecreatedietyapiSchema'] = {
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"}, 
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': { "templeid": {'type':'integer'},        
        "diety_name": {'type':'string'},
        "diety_desc": {'type':'integer'},
        "diety_photo": {'type':'string'}, 
        "diety_oftemp": {'type':'string'},        
       
                        },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

schemas['templelistprasadamapiSchema'] = {
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"}, 
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {"type":"all"
                        },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},


    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

schemas['templelistdietyapiSchema'] = {
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"}, 
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {"type":"all"
                        },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},


    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}


schemas['templecreateHistoryapi'] = {
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"}, 
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {"templeid": {'type':'integer'},        
        "diety_name": {'type':'string'},
        "diety_desc": {'type':'integer'},
        "diety_photo": {'type':'string'}, 
        "diety_oftemp": {'type':'string'},
                        },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},


    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}