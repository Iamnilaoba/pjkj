# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import ssl,os
from urllib import request


class CarPipeline(object):

    def open_spider(self,spider):
        ssl._create_default_https_context = ssl._create_unverified_context
        basedir=os.path.dirname(os.path.dirname(__file__))
        self.path=os.path.join(basedir,"imgs")
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def process_item(self, item, spider):
        categary=item["categary"]
        ps=os.path.join(self.path,categary)
        if not os.path.exists(ps):
            os.makedirs(ps)

        img_urls=item["img_urls"]
        for url in img_urls:             # 下载保存照片
            imgName=url.split("/")[-1]
            filePs=os.path.join(ps,imgName)
            request.urlretrieve(url,filePs)


from scrapy.pipelines.images import ImagesPipeline

class myImgPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        requests=super(myImgPipeline,self).get_media_requests(item,info)
        for request in requests:
            request.categary=item['categary']
        return requests

    def file_path(self, request, response=None, info=None):
        imgname = super(myImgPipeline,self).file_path(request,response,info) # /%s.jpg
        imgname = imgname.replace("full/",'') # 获取到图片的名字
        categary = request.categary
        return '%s/%s' % (categary, imgname)






