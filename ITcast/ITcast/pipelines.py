# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class ItcastPipeline(object):
    def __init__(self):
        self.f = open('itcast.json','w',encoding='utf-8')

    # def open_spider(self,spider):
        #可选方法，当spider开启时，这个方法被调用
    #     pass

    def process_item(self, item, spider):   #此方法必须实现
        # item (Item对象) - 被爬取的item
        # spider (spider对象) - 爬取该item的spider
        content = json.dumps(dict(item),ensure_ascii=False,indent=2) + ','
        self.f.write(content)
        return item

    def close_spider(self,spider):
        # spider参数必须加上，不然此方法会报错，无法执行此步
        self.f.close()