# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from urllib import request
import os

# 保存下载文件
class PikjPipeline(object):
    def process_item(self, item, spider):
    #    req=request.Request(url=item['addr'])
    #    req=request.urlopen(req)
    #    filename=os.path.join(r"D:\aa",item['name']+'.jpg')
    #    with open(filename,"wb") as f:
    #        f.write(req.read())


        import requests
        req=requests.get(url=item['addr'])
        filename = os.path.join(r"D:\aa")
        with open(filename,"wb") as f:
            f.write(req.content)
