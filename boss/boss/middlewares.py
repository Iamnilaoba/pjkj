import random
import requests
import time


# class BossDownloaderMiddleware(object):
#     lst=["Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)",
#          "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)",
#          "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)"]
#
#     def process_request(self, request, spider):
#         request.headers["User-Agent"]=random.choice(self.lst)
#
#
# class BossIPDownloaderMiddleware(object):   # 最少一百个
#     lst = ['123.138.89.133:9999', '211.138.248.119:49698','183.129.207.80:21213']
#
#     def process_request(self, request, spider):
#         ip = random.choice(self.lst)
#         request.meta['proxy'] = ip
#         return request


class BossDownloaderIPMiddleware(object):
    def process_request(self, request, spider):
        if not request.meta.__contains__("proxy"):
            request.meta["proxy"]=self.getProxy()

    def process_response(self,response,request,spider):
        if response.status == 403:
            request.meta['proxy']=self.getProxy()
            return request
        return response

    def getProxy(self):
        rd = requests.get(  # 快代理生成的ip链接
            "https://dev.kdlapi.com/api/getproxy/?orderid=934235707422473&num=1&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=2&method=2&an_an=1&an_ha=1&sp1=1&dedup=1&sep=4").text
        r = rd.text
        if "普通" in r:
            time.sleep(3)
        else:
            return self.getProxy()


class BossDownloaderMiddleware(object):
    lst=["Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)",
         "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)",
         "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)"]

    def process_request(self, request, spider):
        request.headers["User-Agent"]=random.choice(self.lst)

