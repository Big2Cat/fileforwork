#!/usr/bin/env python
# encoding: utf-8

import requests

def postdata(postbody):

    posturl = 'http://www.shclearing.com/wcm/shch/pages/client/download/download.jsp'
    headers = {'Host': 'www.shclearing.com',
               'User-Agenti': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0i',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
               'Accept-Encoding': 'gzip, deflate',
               'Referer': 'http://www.shclearing.com/xxpl/xypj/zxpl/cp_555/201702/t20170213_223971.html',
               'Connection': 'keep-alive',
               'Upgrade-Insecure-Requests': '1',
               'Content-Type': 'application/x-www-form-urlencoded',
               }
    postbody = postbody
    r = requests.post(posturl,headers = headers,data = postbody,stream = True)
    with open('1.pdf','wb') as opdf:
        for chunk in r.iter_content(1):
            opdf.write(chunk)

    #print 'r.text is:'+r.text
    print type(r)
    print 'r.code is:'+str(r.status_code)

postbody = 'FileName=P020170213347414511178.pdf&DownName=%25E5%25BC%25A0%25E5%25AE%25B6%25E6%25B8%25AF%25E4%25BF%259D%25E7%25A8%258E%25E5%258C%25BA%25E5%25BC%25A0%25E4%25BF%259D%25E5%25AE%259E%25E4%25B8%259A%25E6%259C%2589%25E9%2599%2590%25E5%2585%25AC%25E5%258F%25B8%25E4%25B8%25BB%25E4%25BD%2593%25E4%25B8%258E2016%25E5%25B9%25B4%25E5%25BA%25A6%25E7%25AC%25AC%25E4%25BA%258C%25E6%259C%259F%25E7%259F%25AD%25E6%259C%259F%25E8%259E%258D%25E8%25B5%2584%25E5%2588%25B82017%25E5%25B9%25B4%25E5%25BA%25A6%25E8%25B7%259F%25E8%25B8%25AA%25E8%25AF%2584%25E7%25BA%25A7%25E6%258A%25A5%25E5%2591%258A.pdf'
postdata(postbody)
