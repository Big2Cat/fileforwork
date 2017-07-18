# -*- coding: utf-8 -*-
import scrapy


class CoserSpider(scrapy.Spider):
    name = "coser"
    allowed_domains = ["bcy.net"]
    start_urls = (
        'http://www.bcy.net/',
    )

    def parse(self, response):
        pass
