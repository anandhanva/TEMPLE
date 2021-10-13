from flask.globals import request
from b_end.statics import staticfunctions
from b_end.platformlayers import standardresponses
# Log the activity in Maass Logger Micro Service
def masslogger(data, error):
    maassdata = {"req_type":request['req_type'],"req_code":request['req_code'],
                        "apiname":request['apiname'],"em_reqid":request['em_reqid'],
                        "partner_reqid":request['partner_reqid'],"requestdata":request['requestdata'],"authToken":request['authtoken'],"em_endpoint":request['em_endpoint'],
                        "em_custid":request['em_custid'],"txntype":request["txntype"],"hashstr":request['hashstr'],"checksum":request['checksum']}
    #Log the error and the request data parameters
    maassobj=standardresponses.commonValues
    #core
    maaass=staticfunctions.performRequest(maassobj['CORELOGIN'],maassdata)
    return maaass