DB_NAME = 'temple'
ENCRYPTION_KEY = "WHENTHESKIESAREBLUESEEYOUONCEAGA"
# LOG_TABLE = 'log'
# user scheema
# SchemaConst=['api_name']+"Schema"
# print("||||||||||||||||||||||||||||||||||||",SchemaConst)
schemas = {}

schemas['templeloginapiSchema'] = {
    'req_type': {'type': 'string'},
    'req_code': {"type": "integer"},
    'apiname': {'type': 'string'},
    'ewire_reqid': {'type': 'string'},
    'modulename': {'type': 'string'},
    'partner_reqid': {'type': 'string'},
    'req_timestamp': {'type': 'integer'},
    'requestdata': {'username': {'type': 'string'},
                    'password': {'type': 'string'}},
    'authtoken': {'type': 'string'},
    'ewire_endpoint': {'type': 'string'},
    'ewire_custid': {'type': 'string'},
    'txntype': {'type': 'string'},
    'hashstr': {'type': 'string'},
    'checksum': {'type': 'string'}}

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#USER API

#INDEX
schemas['userindexapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'modulename': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata':  {'type':'homepage'
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}


#history
schemas['historyapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'modulename': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'templeid':{'type':'string'},
                    'user_id':{'type':'string'},
                    'role_id':{'type':'string'},
                    },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}





#kanikka

schemas['userkanikaapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'modulename': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'kanikka_id':{'type':'string'},
                    'name':{'type':'string'},
                    'star':{'type':'string'},
                    'date':{'type':'date'},
                    'amount':{'type':'integer'}, },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}


#get_star drop


schemas['getstardropapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'modulename': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'type':{'type':'dropdwon'},
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#get_prasadam_bill_list



schemas['getprsdmbllstapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'modulename': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'prasadambill':{'type':'string'},
                     },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#user_list kanikka



schemas['userlistkanikkaapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'modulename': {'type':'string'},
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

#pooja_bill

schemas['poojabillapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'modulename': {'type':'string'},
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
#kanikka_pay

schemas['kanikkapayapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'modulename': {'type':'string'},
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

#offer bill

schemas['offerbillapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'modulename': {'type':'string'},
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

#nearby attraction

schemas['nearbyatrtinapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'modulename': {'type':'string'},
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

#nearest stay
schemas['neareststayapiSchema']={
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"},
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'modulename': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'temple_id': {'type': 'string'},
                    'userid': {'type': 'string'},
                    'roleid': {'type': 'string'}
                    },
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}



#diety
schemas['userdietyapiSchema'] = {
    'req_type': {'type': 'string'},
    'req_code': {"type": "integer"},
    'apiname': {'type': 'string'},
    'ewire_reqid': {'type': 'string'},
    'modulename': {'type': 'string'},
    'partner_reqid': {'type': 'string'},
    'req_timestamp': {'type': 'integer'},
    'requestdata': {'temple_id': {'type': 'string'},
                    'userid': {'type': 'string'},
                    'roleid': {'type': 'string'}
                    },
    'authtoken': {'type': 'string'},
    'ewire_endpoint': {'type': 'string'},
    'ewire_custid': {'type': 'string'},
    'txntype': {'type': 'string'},
    'hashstr': {'type': 'string'},
    'checksum': {'type': 'string'}}
#location 
schemas['locationapiSchema'] = {
    'req_type': {'type': 'string'},
    'req_code': {"type": "integer"},
    'apiname': {'type': 'string'},
    'ewire_reqid': {'type': 'string'},
    'modulename': {'type': 'string'},
    'partner_reqid': {'type': 'string'},
    'req_timestamp': {'type': 'integer'},
    'requestdata': {'temple_id': {'type': 'string'},
                    'userid': {'type': 'string'}
                    },
    'authtoken': {'type': 'string'},
    'ewire_endpoint': {'type': 'string'},
    'ewire_custid': {'type': 'string'},
    'txntype': {'type': 'string'},
    'hashstr': {'type': 'string'},
    'checksum': {'type': 'string'}}

#map
schemas['mapapiSchema'] = {
    'req_type': {'type': 'string'},
    'req_code': {"type": "integer"},
    'apiname': {'type': 'string'},
    'ewire_reqid': {'type': 'string'},
    'modulename': {'type': 'string'},
    'partner_reqid': {'type': 'string'},
    'req_timestamp': {'type': 'integer'},
    'requestdata': {'temple_id': {'type': 'string'},
                    'userid': {'type': 'string'}
                    },
    'authtoken': {'type': 'string'},
    'ewire_endpoint': {'type': 'string'},
    'ewire_custid': {'type': 'string'},
    'txntype': {'type': 'string'},
    'hashstr': {'type': 'string'},
    'checksum': {'type': 'string'}}