#!/usr/bin/env python
# encoding: utf-8

import requests

def codHandler(picnums):

    query_url = 'http://shixin.csrc.gov.cn/honestypub/login/ycode.do'
    headers = {'Host': 'shixin.csrc.gov.cn',
               'Connection': 'keep-alive',
               'Cache-Control': 'max-age=0',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.8'}
    for i in range(picnums):
        r = requests.get(query_url,headers=headers)
        with open('./'+str(i)+'.jpg','wb') as f:
            f.write(r.content)
            print '........在下载页数：{}.......'.format(i)

codHandler(1000)
