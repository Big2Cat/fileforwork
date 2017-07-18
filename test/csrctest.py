#!/usr/bin/env python
# encoding: utf-8

import urllib
import requests
import datetime
from lxml import etree
from PIL import Image
from io import BytesIO

headers = {'Host': 'shixin.csrc.gov.cn',
           'Connection': 'keep-alive',
           'Cache-Control': 'max-age=0',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, sdch',
           'Accept-Language': 'zh-CN,zh;q=0.8',
           }
headers_sec = {'Host': 'shixin.csrc.gov.cn',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
               'Accept': '*/*',
               'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
               'Accept-Encoding': 'gzip, deflate',
               'Referer': 'http://shixin.csrc.gov.cn/honestypub/',
               'Connection': 'keep-alive'}
headers_query = {'Host': 'shixin.csrc.gov.cn',
                 'Connection': 'keep-alive',
                 'Cache-Control': 'max-age=0',
                 'Origin': 'http://shixin.csrc.gov.cn',
                 'Upgrade-Insecure-Requests': '1',
                 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                 'Content-Type': 'application/x-www-form-urlencoded',
                 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                 'Referer': 'http://shixin.csrc.gov.cn/honestypub/',
                 'Accept-Encoding': 'gzip, deflate',
                 'Accept-Language': 'zh-CN,zh;q=0.8'
                 }
mianpage_url = 'http://shixin.csrc.gov.cn/honestypub/'
vcode_url = 'http://shixin.csrc.gov.cn/honestypub/login/ycode.do'
query_url = 'http://shixin.csrc.gov.cn/honestypub/honestyObj/query.do'
r = requests.get(mianpage_url,headers=headers)
tree = etree.HTML(r.text)
randSesion = tree.xpath('*//input[@name="randSesion"]/@value')[0]
print randSesion
#print randSesion
gmt_time = datetime.datetime.utcnow().strftime('%a %d %b %Y %H:%M:%S GMT+0800')
print gmt_time
param = {'d':gmt_time}
v_image = requests.get(vcode_url,headers=headers_sec,params=param)
i = Image.open(BytesIO(v_image.content))
#with open('./csrctestimage/a.jpg','wb') as f:
#    f.write(v_image.content())
#im = Image.open('./csrctestimage/a.jpg')
i.show()

v_input = raw_input('请输入验证码:')
object_input = raw_input('请输入要查询的内容:')
print v_input
query_body = {'randSesion':randSesion,
              'objName':object_input,
              'realCardNumber':'',
              'ycode':v_input}
r_query = requests.post(query_url,body=urllib.urlencode(query_body),headers=headers_query)



