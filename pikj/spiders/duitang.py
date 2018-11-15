# -*- coding: utf-8 -*-
import scrapy
from pikj.items import PikjItem

# 解析url，编写爬虫规则
class DuitangSpider(scrapy.Spider):
    name = 'duitang'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com']

    def parse(self, response):
        resp=response.xpath("//div[@id='content-left']/div")
        for i in resp:
            auth=i.xpath("./div/a[2]/h2/text()").get()
            dz=i.xpath("./a[1]/div/span/text()").get().strip()
            yield PikjItem(auth=auth,dz=dz)

        next_url=response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
        if next_url:
            next_url="https://www.qiushibaike.com"+next_url
            yield scrapy.Request(next_url,callback=self.parse)
        else:
            pass
