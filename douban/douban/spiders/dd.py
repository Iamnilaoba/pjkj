# -*- coding: utf-8 -*-
import scrapy
from urllib import request
import ssl
import requests
from base64 import b64encode


class DdSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['douban.com']
    start_urls = ['https://www.douban.com/accounts/login?']
    login_url = 'https://www.douban.com/login'
    user_info = 'https://www.douban.com/people/187315023/'
    edit_url = 'https://www.douban.com/people/187315023/edit_signature'

    def parse(self, response):
        ssl._create_default_https_context = ssl._create_default_https_context  # 不验证证书
        formdata = {"source": "Null",
                    "redir": "https://www.douban.com",
                    "form_email": "957879670@qq.com",
                    "form_password": "zhangsan123",
                    "remember": "on"}
        img_url = response.xpath("//img[@id='captcha_image']/@src").get()
        if img_url:
            captcha_id = response.xpath("//input[@name='captcha-id']/@value").get()
            formdata['captcha-id'] = captcha_id
            request.urlretrieve(img_url, 'captcha_img.png')
            captcha = self.getCaptche()
            formdata['captcha-solution'] = captcha
        req = scrapy.FormRequest(url=self.login_url, formdata=formdata, callback=self.parse_user_info)
        yield req

    def parse_user_info(self, response):
        if response.url == "http://www.douban.com":
            print("登录成功")
            yield scrapy.Request(url=self.user_info, callback=self.show_user_info)
        else:
            print("登录失败")

    def show_user_info(self, response):
        ck = response.xpath("//input[@name='ck']/@value").get()
        signature = "我是一个神"
        formdata = {"ck": ck, "signature": signature}
        yield scrapy.FormRequest(url=self.edit_url, formdata=formdata, callback=self.show_result)

    def show_result(self, response):
        print("修改签名成功")

    def getCaptche(self):
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=QY6lRGrCGfpjWdBvPBLmXlPj&client_secret=oYbv8U7PxAOGoTgoE41EgADlawzCmqkh&'
        request = requests.post(host)
        access_token = request.json()['access_token']
        header = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        with open("captcha_img.png", "rb") as f:
            img = b64encode(f.read())
        img = str(img, 'utf-8')
        data = {"image_type": "BASE64", "image": img}
        url = ' https://aip.baidubce.com/rest/2.0/ocr/v1/accurate?access_token=' + access_token
        r = requests.post(url=url, headers=header, data=data)
        return r.json().get('words_result')[0].get('words').strip()

