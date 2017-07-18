#!/usr/bin/env python
# encoding: utf-8

from pymongo import MongoClient

client = MongoClient()

client = MongoClient('localhost', 27017)

mdb = client.rmfygg

post = mdb.rmfyggdoc

numinmongo = post.find().count()

print numinmongo


