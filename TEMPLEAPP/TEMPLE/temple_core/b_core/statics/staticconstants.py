DB_NAME = 'temple'
ENCRYPTION_KEY = "WHENTHESKIESAREBLUESEEYOUONCEAGA"
USER_NOT_EXIST = {"Error-Response":"USER NOT FOUND"}
INVALID_USER_PASS = {"Error-Response":"Invalid USERNAME, PASSWORD"}

# LOG_TABLE = 'log'
schemas = {}

#user schema
userSchema = {
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"}, 
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'mobile_number': {'type':'string'},},
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}

#otpverification schema
otpVerificationSchema = {
    'req_type': {'type':'string'},
    'req_code': {"type":"integer"}, 
    'apiname': {'type':'string'},
    'ewire_reqid': {'type':'string'},
    'partner_reqid': {'type':'string'},
    'req_timestamp': {'type':'integer'},
    'requestdata': {'otp_number': {'type':'integer'},},
    'authtoken': {'type':'string'},
    'ewire_endpoint': {'type':'string'},
    'ewire_custid': {'type':'string'},
    'txntype': {'type':'string'},
    'hashstr': {'type':'string'},
    'checksum': {'type':'string'}}