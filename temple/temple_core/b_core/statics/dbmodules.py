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

def offering(query,datadict,op,offering):
    d1 = {}
    d1['collection'] = offering
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

def prasadam(query,datadict,op,prasadam,):
    d1 = {}
    d1['collection'] = prasadam
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

def diety(query,datadict,op,diety):
    d1 = {}
    d1['collection'] = diety
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

def rate(query,datadict,op,rate):
    d1 = {}
    d1['collection'] = rate
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

def qnty(query,datadict,op,qntymaster):
    d1 = {}
    d1['collection'] = qntymaster
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


def history(query,datadict,op,history):
    d1= {}
    d1['collection'] = history
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


def airport(query,datadict,op,history):
    d1 = {}
    d1['collection'] = history
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

def stay(query,datadict,op,stay,):
    d1 = {}
    d1['collection'] = stay
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


def category(query,datadict,op,history):
    d1= {}
    d1['collection'] = history
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