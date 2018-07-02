# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentjobItem(scrapy.Item):
    # define the fields for your item here like:
    # 职位名称
    positionName = scrapy.Field()
    # 工作地点
    positionCity = scrapy.Field()
    # 职位类别
    positionType = scrapy.Field()
    # 招聘人数
    positionNum = scrapy.Field()
    # 发布时间
    releaseTime = scrapy.Field()
    # 工作职责
    positionduty = scrapy.Field()
    # 职位要求
    positionrequest = scrapy.Field()
    # pass
