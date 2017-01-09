import sys
import pymongo

class db_mongo:
    def __init__(self):
        self.dburi='mongodb://xxh:jh@ds159188.mlab.com:59188/xxhdb'
        self.conn=None

    def get_connection(self):
        self.conn=pymongo.MongoClient(self.dburi)
        return self.conn


defaultDB=db_mongo()

def getData():
    conn=defaultDB.get_connection()
    db=conn.get_default_database()

    songsDb=db['songs']
    cursor = songsDb.find({'weeksAtOne': {'$gte': 10}}).sort('decade', 1)
    ret=[]

    for doc in cursor:
        ret.append(doc['song'])

    conn.close()
    return ret