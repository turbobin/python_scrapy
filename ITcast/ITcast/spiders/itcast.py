# -*- coding: utf-8 -*-
import scrapy

from ITcast.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn'] # 可选参数，可注释
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # print(response)
        node_list = response.xpath('//div[@class="li_txt"]')
        for node in node_list:
            item = ItcastItem()
            # extract()方法将xpath对象转换为Unicode字符串
            name = node.xpath('./h3/text()').extract()
            title = node.xpath('./h4/text()').extract()
            info = node.xpath('./p/text()').extract()

            #xpath取出的是list，转换成str需取下标
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            yield item
