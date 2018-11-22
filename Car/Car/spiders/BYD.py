# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BydSpider(CrawlSpider):
    name = 'BYD'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/59.html']

    rules = (
        Rule(LinkExtractor(allow=r'.*/pic/series/59.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        categary=response.xpath("//a[@class='filter filter-small']/span/text()").get()
        urls=response.xpath("//ul/li/a/img/@src").getall()
        urls=list(map(lambda item: 'https:'+ item,urls))
        yield {"categary": categary, "img_urls": urls}



    def parse_text(self, response):
        uboxs = response.xpath("//div[@class='uibox']")[1:]
        for ubox in uboxs:
            categary = ubox.xpath("./div/a/text()").get()
            img_urls = ubox.xpath("./div/ul/li/a/img/@src").getall()
            img_urls = list(map(lambda url: "https:"+url,img_urls))
            yield {"categary":categary,"img_urls":img_urls}
