# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 设定要下载的文件
class PikjItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    addr=scrapy.Field()
    name=scrapy.Field()