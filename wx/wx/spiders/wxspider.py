# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import WxItem

class WxspiderSpider(CrawlSpider):
    name = 'wxspider'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.*mod=list&catid=2&page=\d+'), follow=True),
        Rule(LinkExtractor(allow=r'.*article-\d{4}-1.html'),callback='parse_item',follow=False)
    )

    def parse_item(self, response):
        title=response.xpath("//h1[@class='ph']/text()").get()
        auth=response.xpath("//p[@class='authors']/a/text()").get()
        desc=response.xpath("//div[@class='blockquote']/p/text()").get()
        wx_item=WxItem(title=title,auth=auth,desc=desc)
        yield wx_item
