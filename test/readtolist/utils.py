#!/usr/bin/env python
# encoding: utf-8
import pymongo
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#MONODB CONNECTIONS CLASS

class MongoDBConnection(object):

    def __init__(self):

        dbname = 'testdb'
        docname = 'testcollections'

        self.dbname = dbname
        self.docname = docname
        self.client = pymongo.MongoClient()

    def dowithmongo(self,insertitem):
        db_auth = self.client.admin
        db_auth.authenticate('kong','kong123')
        mdb = self.client[self.dbname]
        post = mdb[self.docname]
        data = insertitem
        print 'data数据是{data}'.format(data=data)
        post.insert(data)

class ReadFiletolist(object):

    def __init__(self,filepath):

        self.filepath = filepath
        self.emptylist = []

    def readfile(self):

        with open(self.filepath,'r') as f:

            for line in f.readlines():

                self.emptylist.append(line)

            return self.emptylist



