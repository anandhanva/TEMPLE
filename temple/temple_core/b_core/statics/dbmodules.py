import json
from b_core.statics import dbconstants

def pooja(query,datadict,op,pooja):
    d1 = {}
    d1['collection'] = pooja
    d1['database'] = "temple"
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
        return datavalue

def offering(query,datadict,op,offering,):
    datadict['collection'] = offering
    datadict['database'] = "temple"
    if op=='i':
        datavalue = dbconstants.MongoAPI(datadict).write(datadict)
    elif op=='u':
        datavalue = dbconstants.MongoAPI(datadict).update(query)
    elif op=='l':
        datavalue = dbconstants.MongoAPI(datadict).read(query)
    elif op=='lc':
        datavalue = dbconstants.MongoAPI(datadict).readOne(query)
    elif op=='c':
        datavalue = dbconstants.MongoAPI(datadict).count(query)
    return datavalue

def prasadam(query,datadict,op,prasadam,):
    datadict['collection'] = prasadam
    datadict['database'] = "temple"
    if op=='i':
        datavalue = dbconstants.MongoAPI(datadict).write(datadict)
    elif op=='u':
        datavalue = dbconstants.MongoAPI(datadict).update(query)
    elif op=='l':
        datavalue = dbconstants.MongoAPI(datadict).read(query)
    elif op=='lc':
        datavalue = dbconstants.MongoAPI(datadict).readOne(query)
    elif op=='c':
        datavalue = dbconstants.MongoAPI(datadict).count(query)
    return datavalue

def diety(query,datadict,op,diety):
    datadict['collection'] = diety
    datadict['database'] = "temple"
    if op=='i':
        datavalue = dbconstants.MongoAPI(datadict).write(datadict)
    elif op=='u':
        datavalue = dbconstants.MongoAPI(datadict).update(query)
    elif op=='l':
        datavalue = dbconstants.MongoAPI(datadict).read(query)
    elif op=='lc':
        datavalue = dbconstants.MongoAPI(datadict).readOne(query)
    elif op=='c':
        datavalue = dbconstants.MongoAPI(datadict).count(query)
    return datavalue

def rate(query,datadict,op,rate):
    datadict['collection'] = rate
    datadict['database'] = "temple"
    if op=='i':
        datavalue = dbconstants.MongoAPI(datadict).write(datadict)
    elif op=='u':
        datavalue = dbconstants.MongoAPI(datadict).update(query)
    elif op=='l':
        datavalue = dbconstants.MongoAPI(datadict).read(query)
    elif op=='lc':
        datavalue = dbconstants.MongoAPI(datadict).readOne(query)
    elif op=='c':
        datavalue = dbconstants.MongoAPI(datadict).count(query)
    return datavalue


def history(query,datadict,op,history):
    datadict['collection'] = history
    datadict['database'] = "temple"
    if op=='i':
        datavalue = dbconstants.MongoAPI(datadict).write(datadict)
    elif op=='u':
        datavalue = dbconstants.MongoAPI(datadict).update(query)
    elif op=='l':
        datavalue = dbconstants.MongoAPI(datadict).read(query)
    elif op=='lc':
        datavalue = dbconstants.MongoAPI(datadict).readOne(query)
    elif op=='c':
        datavalue = dbconstants.MongoAPI(datadict).count(query)
    return datavalue


def airport(query,datadict,op,history):
    datadict['collection'] = history
    datadict['database'] = "temple"
    if op=='i':
        datavalue = dbconstants.MongoAPI(datadict).write(datadict)
    elif op=='u':
        datavalue = dbconstants.MongoAPI(datadict).update(query)
    elif op=='l':
        datavalue = dbconstants.MongoAPI(datadict).read(query)
    elif op=='lc':
        datavalue = dbconstants.MongoAPI(datadict).readOne(query)
    elif op=='c':
        datavalue = dbconstants.MongoAPI(datadict).count(query)
    return datavalue

