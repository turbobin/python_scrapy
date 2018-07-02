# -*- coding: utf-8 -*-
import scrapy
import json

from DouYu.items import DouyuItem


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['capi.douyucdn.cn']
    offset = 0
    start_url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset={}".format(offset)
    start_urls = [start_url]

    def parse(self, response):
        data_list = json.loads(response.body)["data"]

        #data 值为空时，退出
        if not data_list:
            return

        for data in data_list:
            item = DouyuItem()
            item['nickname'] = data["nickname"]
            item['imageUrl'] = data["vertical_src"]
            item['city'] = data["anchor_city"]
            yield item

        self.offset += 20
        yield scrapy.Request("http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset={}".format(self.offset))
