# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest

class PostgsxtSpider(scrapy.Spider):
    name = "postgsxt"
    allowed_domains = ["gsxt.gov.cn"]
    start_urls = (
        'http://yd.gsxt.gov.cn/',
    )
    headers = {
        'Host': 'yd.gsxt.gov.cn',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'Origin': 'file://',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.4; SOL26 Build/23.0.C.0.296) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 Html5Plus/1.0',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'zh-CN,en-US;q=0.8',
        'X-Requested-With': 'com.zongjucredit',
    }


    def parse(self,response):
        print response.body
        yield Request(url = 'http://yd.gsxt.gov.cn/QuerySummary',
                       headers = self.headers,
                       method = 'POST',
                       body = 'mobileAction=entSearch&keywords=%E9%98%BF%E9%87%8C%E5%B7%B4%E5%B7%B4&topic=1&pageNum=1&pageSize=10&userID=id001&userIP=192.123.123.13',
                       callback = self.get_response)
    def get_response(self,response):
        print 'print thing'
        print response.body

