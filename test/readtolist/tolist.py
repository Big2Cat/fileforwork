#!/usr/bin/env python
# encoding: utf-8
import re
import sys
import md5
from utils import MongoDBConnection
reload(sys)
sys.setdefaultencoding('utf-8')


f = open('company.txt','r')
for line in f.readlines():

    m = md5.new()
    m.update(line)

    try:
        line = re.sub('\n','',line)
    except:
        pass


    to_insert = {'_id':m.hexdigest(),'company_name':line}

    MongoDBConnection().dowithmongo(to_insert)
