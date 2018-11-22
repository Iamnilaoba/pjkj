# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import BossItem

class BbSpider(CrawlSpider):
    name = 'bb'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query=python&page=1']

    rules = (  # （只在要爬取数据的页面加上callback，不加callback的是为了引入到要爬取数据的页面，注意follow）
        # 列表页数
        Rule(LinkExtractor(allow=r'.*query=python&page=\d+'), follow=True),
        # 职位信息页数
        Rule(LinkExtractor(allow=r'.*job_detail/.+.html'), callback='parse_item', follow=False)
    )

    def parse_item(self, response):
        # 1.职责介绍 2.公司介绍
        job_desc = response.xpath("//div[@class='job-sec']/div/text()").get()
        company_desc = response.xpath("//div[@class='job-sec company-info']/div/text()").get()
        yield BossItem(job_desc=job_desc,company_desc=company_desc)




