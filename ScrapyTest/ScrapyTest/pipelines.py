# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class ScrapytestPipeline(object):
    def __init__(self): # 只执行一次
        self.f_obj = open('doubanMV.json','w')

    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii=False,indent=2)
        self.f_obj.write(content)
        return item

    def close_spider(self,spider):  # 最后才执行
        self.f_obj.close()
        print('数据已保存到doubanMV.json')
