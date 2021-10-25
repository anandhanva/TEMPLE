


# Prepare and pass the dictionary to db and generate QR Link by storing generated qr to cloud link
from pymongo import collation, collection, database
from b_core.statics import dbconstants

def createQRfromDict(data):
    dbQuery = {"order_id":data['datafrm']['order_id']}
    data[database]="temple"
    data[collection]="order"
    rowcount = dbconstants.MongoAPI(data).count(dbQuery)
    if(rowcount >=1):
        getrowfrmdb = dbconstants.MongoAPI(data).readOne(dbQuery)
    else:
        insertrowtodb = dbconstants.MongoAPI(data).write(dbQuery)
    return data

# Code to read the qr data and prepare database lookup
def readQRdata(data):
    dbQuery = {"order_id":data['datafrm']['order_id']}
    data[database]="temple"
    data[collection]="qr"
    dataval = dbconstants.MongoAPI(data).readOne(dbQuery)
    return dataval

# Lookup the prepared query from above module to decode the data
def returnDataforQRfromdb(data):
    return data

# Use the decoded data to provide the list that needs to be sent back to the user interface
def prepareresponsefromQRdata(data):
    return data