# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import json
import pymysql

class TencentjobPipeline(object):
    def __init__(self):
        # 打开数据库连接
        self.conn = pymysql.connect(host="localhost", user="root", password="root", db="mysql", port=3306,charset="utf8")
        self.cursor = self.conn.cursor()
        self.cursor.execute("use mydatabase")
        self.cursor.execute("drop table if exists tencentjob;")
        self.cursor.execute('create table if not exists tencentjob'
                            '(job_id int primary key auto_increment,'
                            'releaseTime varchar(10),'
                            'positionName varchar(100),'
                            'positionCity varchar(10),'
                            'positionType varchar(20),'
                            'positionNum varchar(10),'
                            'positionduty varchar(2000),'
                            'positionrequest varchar(2500))'
                            'charset=utf8;')
    def process_item(self, item, spider):

        # content = json.dumps(dict(item),ensure_ascii=False,indent=2)
        # self.f.write(content)
        item_list = dict(item).values()
        print('列表',item_list)
        self.cursor.execute("insert into tencentjob values("
                            "null,%s,%s,%s,%s,%s,%s,%s);",list(item_list))

        return item


    def close_spider(self,spider):
        # spider参数必须加上，否则此方法报错不执行.
        print("关闭爬虫，数据已写入MySQL数据库...")
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
