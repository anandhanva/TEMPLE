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


def category(query,datadict,op,category):
    d1= {}
    d1['collection'] = category
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


def festival(query,datadict,op,festival):
    d1 = {}
    d1['collection'] = festival
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




def statement(query,datadict,op,statement):
    d1 = {}
    d1['collection'] = statement
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


def activity(query,datadict,op,activity):
    d1 = {}
    d1['collection'] = activity
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



def temple(query,datadict,op,temple):
    d1 = {}
    d1['collection'] = temple
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


def devaswom(query,datadict,op,devaswom):
    d1 = {}
    d1['collection'] = devaswom
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

def devasomadmin(query,datadict,op,devasomadmin):
    d1 = {}
    d1['collection'] = devasomadmin
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


def pool(query,datadict,op,bpool):
    d1 = {}
    d1['collection'] = bpool
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

def fund(query,datadict,op,bfund):
    d1 = {}
    d1['collection'] = bfund
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

def bank(query,datadict,op,bank):
    d1 = {}
    d1['collection'] = bank
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

def bankadmin(query,datadict,op,bankadmin):
    d1 = {}
    d1['collection'] = bankadmin
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


def card(query,datadict,op,card):
    d1 = {}
    d1['collection'] = card
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



def transactionDevaswom(query,datadict,op,card):
    d1 = {}
    d1['collection'] = card
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

def Finance(query,datadict,op,Finance):
    d1 = {}
    d1['collection'] = Finance
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

def reconciliation(query,datadict,op,recon):
    d1 = {}
    d1['collection'] = recon
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

def reqmoney(query,datadict,op,reqmoney):
    d1 = {}
    d1['collection'] = reqmoney
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

def lords(query,datadict,op,lords):
    d1 = {}
    d1['collection'] = lords
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

def forgotpin(query,datadict,op,forgotpin):
    d1 = {}
    d1['collection'] = forgotpin
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

def templetra(query,datadict,op,templetra):
    d1 = {}
    d1['collection'] = templetra
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

def block(query,datadict,op,block):
    d1 = {}
    d1['collection'] = block
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