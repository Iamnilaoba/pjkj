# -*- coding: utf-8 -*-
import scrapy
from pikj.items import PikjItem

# 解析url，编写爬虫规则
class DuitangSpider(scrapy.Spider):
    name = 'duitang'
    allowed_domains = ['doutula.com']
    start_urls = ['https://www.doutula.com']

    def parse(self, response):
        imgs = response.xpath('//div[@class="col-xs-6 col-sm-3"]/img')
        for img in imgs:
            item = PikjItem()
            addr = img.xpath('./@src').extract()[0]
            name = img.xpath('./@alt').extract()
            item['name']=name[0] if name else None
            addr = 'https://www.doutula.com' + addr
            item['name'] = name
            item['addr'] = addr
            yield item
