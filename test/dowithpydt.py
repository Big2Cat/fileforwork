#!/usr/bin/env python
# encoding: utf-8

import requests


headers ={'Host':'www.py-dt.com',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
'Accept':'*/*',
'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding':'gzip, deflate',
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'X-Requested-With':'XMLHttpRequest',
'Referer':'http://www.py-dt.com/bond/zhaipingji.html',
'Connection':'keep-alive'}
#headers = headers.strip().split('\n')
#headers = {x.split(':')[0] : x.split(':')[1] for x in headers}
#print headers
post_url = 'http://www.py-dt.com/api/bonds/creditLevels'
payload = {'loginName':'lovedata','loginToken':'65822ef419904fceaa6bfcfd4c718da4','page':'1','pagesize':'15'}

response_pydt = requests.post(url=post_url,headers=headers,params=payload)

print response_pydt.text


