#!/usr/bin/env python
# encoding: utf-8

import pymongo
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class DoWithMongo(object):

    def __init__(self,dbname,docname):
        self.dbname = dbname
        self.docname = docname

    def dopost(self,itemdata):

        client = pymongo.MongoClient(host='127.0.0.1',port=27017)
        mdb = client[self.dbname]
        post = mdb[self.docname]
        post.insert({'data':itemdata})


doit = DoWithMongo('dbnamefotest','docnamefortest')
doit.dopost('I love you darling')

