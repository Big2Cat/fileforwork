#!/usr/bin/env python
# encoding: utf-8

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from mySpider.items import TencentItem

class TencentItem(CrawlSpider):

    name = 'tencent'
    allowed_domains = ['hr.tencent.com',]
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a',]
    page_lx = LinkExtractor(allow=('start=\d+'))
    rules = [Rule(page_lx,callback='parseContent',follow = True)]

    def parseContent(self, response):



