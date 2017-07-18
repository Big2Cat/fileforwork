#!/usr/bin/env python
# encoding: utf-8

import urllib #负责编码的处理
import urllib2 #请求和添加UA

headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

s_word = {'wd':'孔潜宇'}
url = 'http://www.baidu.com/s'
encod_s_word = urllib.urlencode(s_word)
new_url = url+'?'+encod_s_word

request = urllib2.Request(url = new_url,headers = headers)

response = urllib2.urlopen(request)

print response.read()

