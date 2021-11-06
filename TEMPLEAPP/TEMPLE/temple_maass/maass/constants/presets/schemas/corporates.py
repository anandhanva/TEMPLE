corpSchema = {
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"}, 
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'corporate_type': {'type':'string'},
                     'organization_type': {'type':'string'},
                     'address': {'type':'string'},
                     'corporate_name': {'type':'string'},
                     'account_number': {'type':'integer'},
                     'name_of_the_bank': {'type':'string'},
                     'primary_mobile_number': {'type':'integer'},
                     'cin': {'type':'string'},
                     'corporate_address': {'type':'string'},
                     'state': {'type':'string'},
                     'country': {'type':'string'},
                     'currency': {'type':'string'},
                     'select_type_of_integration': {'type':'string'},
                     'size_of_engagement': {'type':'string'}},
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}