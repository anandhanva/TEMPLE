import json
from b_core.statics import dbconstants

#LOGIN TABLE
def login(query,datadict,op,pooja):
    d1 = {}
    d1['collection'] = login
    d1['database'] = "templeapp"
    if op=='i':
        datavalue = dbconstants.MongoAPI(d1).write(datadict)
        return datavalue
    elif op=='u':
        datavalue = dbconstants.MongoAPI(d1).update(query)
        return json.loads(datavalue)
    elif op=='l':
        datavalue = dbconstants.MongoAPI(d1).read(query)
        return json.loads(datavalue)
    elif op=='lc':
        datavalue = dbconstants.MongoAPI(d1).readOne(query)
        return json.loads(datavalue)
    elif op=='c':
        datavalue = dbconstants.MongoAPI(d1).count(query)
    elif op=='d':
        datavalue = dbconstants.MongoAPI(d1).delete(query)
        return datavalue