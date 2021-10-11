from b_end.platformlayers import constantslayer
from b_end.maass import maasslogger
from b_end.responsemaster import responses
def processLogRequest(request):
    try:
        #extract hash,checksum and data
        hashchecksumdata=constantslayer.parseRequestHCRD(request)
        maasslogger(request,"PROCESS REQUEST")
    except Exception as e:
        maasslogger(request,str(e))
        return responses.standardErrorResponseToUI("LOGIN",str(e))
    try:
        checklog=constantslayer.checklogin(request)
        maasslogger(request,"LOGIN")
    except Exception as ex:
        maasslogger(request,"LOGIN FAILED")
        return responses.standardErrorResponseToUI("LOGIN",str(ex))
