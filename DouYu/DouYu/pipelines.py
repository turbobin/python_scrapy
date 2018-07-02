# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import os

from DouYu.settings import IMAGES_STORE as imgpath


class DouyuPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item["imageUrl"])

    def item_completed(self, results, item, info):
        # results :图片下载结果
        # print(results)
#        [(True, {'url': 'https://rpic.douyucdn.cn/live-cover/appCovers/2018/04/02/4658881_20180402121502_big.jpg',
#                 'path': 'full/4c8dfcb30e0aa93b0470e57d81b9446c4a8fa828.jpg',
#                 'checksum': '17342a2ef6c71246ce5e2350bb162987'})]
        path = [x["path"] for ok, x in results if ok]
        oldname = imgpath + path[0]
        newname = imgpath + "full/" + item["nickname"] + " , " + item["city"]+ ".jpg"
        os.rename(oldname,newname)

        return item
