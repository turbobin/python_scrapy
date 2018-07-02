# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery as pq

from ScrapyTest.items import ScrapytestItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['https://movie.douban.com/']
    start_urls = ['https://movie.douban.com/top250/',]

    def parse(self, response):
        # print(response.body.decode())   #scrapy中用body，返回二进制数据
        html_str = response.body.decode()

        for data in pq(html_str)('.item'):
            item = ScrapytestItem()
            item['title'] = pq(data)('.title').html()
            item['desc'] = pq(data)('.inq').html()
            # print(item)
            #返回提取到的每个值，交给管道文件处理，然后返回进行下一次循环
            yield item

