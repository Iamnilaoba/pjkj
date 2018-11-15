# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter

class WxPipeline(object):
    def __init__(self):
        self.fp=open("aa.json","wb")
        self.expor=JsonLinesItemExporter(self.fp,ensure_ascii=False)

    def process_item(self, item, spider):
        self.expor.export_item(item)
        return item

    def close_spider(self,spider):
        self.fp.close()
