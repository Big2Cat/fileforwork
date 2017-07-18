#!/usr/bin/env python
# encoding: utf-8

from pymongo import MongoClient
import requests
import json
import re

class Getjson(object):


    headers = {'Host': 'platform.sina.com.cn',
               'Connection': 'keep-alive',
               'Pragma': 'no-cache',
               'Cache-Control': 'no-cache',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, sdch',
               'Accept-Language': 'zh-CN,zh;q=0.8'}
    def getdata(self,page):

        meta = {'app_key':2733610594,
                'format':'json',
                'ch_id':77,
                'num':10,
                'page':page,
                'jsoncallback':'getDataJson'}

        r = requests.get(url='http://platform.sina.com.cn/slide/album',params=meta,headers=self.headers)
        content = r.text
        return content


    def dowithdata(self,content):

        content_red = re.search('getDataJson\((.*)\)',content).group(1)
#        print content_red
        jsoncontent = json.loads(content_red)['data']
        return jsoncontent


    def dowithdb(slef,data):

        client = MongoClient()
        db_auth = client.admin
        db_auth.authenticate('kong','kong123')
        db = client['sina_gifs']
        post = db['jsondata']
        post.insert(data)



G = Getjson()
content = G.getdata(1)
jsondata = G.dowithdata(content)
for i in jsondata:
    print '处理数据:{}'.format(i)
    G.dowithdb(i)

