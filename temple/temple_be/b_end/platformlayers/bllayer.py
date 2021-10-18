from b_end.platformlayers import constantslayer
from b_end.maass import maasslogger
from b_end.responsemaster import responses
def processLogRequest(req):
    try:
        #extract hash,checksum and data
        hashchecksumdata=constantslayer.parseRequestHCRD(req)
        maasslogger(req,"PROCESS REQUEST")
    except Exception as e:
        maasslogger(req,str(e))
        return responses.standardErrorResponseToUI("LOGIN",str(e))
    try:
        checklog=constantslayer.checklogin(req)
        maasslogger(req,"LOGIN")
    except Exception as ex:
        maasslogger(req,"LOGIN FAILED")
        return responses.standardErrorResponseToUI("LOGIN",str(ex))


