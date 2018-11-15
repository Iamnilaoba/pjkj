# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from urllib import request
import os
import requests
# 保存下载文件

from scrapy.exporters import JsonLinesItemExporter

class PikjPipeline(object):
    def __init__(self):
        self.fp=open("duanzi.json","wb")
        self.export=JsonLinesItemExporter(self.fp,ensure_ascii=False)

    def process_item(self, item, spider):
        self.export.export_item(item)
        return item

    def close_item(self,spider):
        self.fp.close()

