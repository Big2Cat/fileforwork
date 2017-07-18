#!/usr/bin/env python
# encoding: utf-8

import requests
import time
headers ={'Host':'table.finance.yahoo.com',
'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language':'en-US,en;q=0.5',
'Accept-Encoding':'gzip, deflate, br',
'Connection':'keep-alive',
'Upgrade-Insecure-Requests': '1'}
for i in range(20):
    print '请求第{time}次'.format(time=i+1)

    time.sleep(1)
    with open (str(i)+'.csv','wb') as handle:
        response = requests.get('https://table.finance.yahoo.com/table.csv?s=IBM&a=4&b=3&c=2017&d=4&e=3&f=2017')
        print response.text
        '''for block in response.iter_content(50):
            if not block:
                break
            handle.write(block)'''
