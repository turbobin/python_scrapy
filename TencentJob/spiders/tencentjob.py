# -*- coding: utf-8 -*-
import scrapy

from TencentJob.items import TencentjobItem


class TencentjobSpider(scrapy.Spider):
    name = 'tencentjob'
    allowed_domains = ['hr.tencent.com']
    q = "请输入关键词"
    start = 0
    start_urls = ['https://hr.tencent.com/position.php?lid=&tid=&keywords={}&start={}'.format(q,start)]


    def parse(self, response):
        job_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        for job in job_list:
            item = TencentjobItem()
            positionUrl  = "https://hr.tencent.com/" + job.xpath("./td[1]/a/@href").extract()[0]
            releaseTime = job.xpath("./td[5]/text()").extract()
            item["releaseTime"] = releaseTime[0]
            request = scrapy.Request(positionUrl, callback=self.parse_detail)

            # 使用 request.meta 在回调函数间传递参数，用于从多个页面构建item的数据
            request.meta['item'] = item
            yield request

        # 构造下一页url，发送下一个请求 (此方法不靠谱)
        # total_page = response.xpath("//div[@class='pagenav']/a[10]/text()")
        # if self.start < int(total_page) * 10:
        #     self.start += 10
        #     next_url = 'https://hr.tencent.com/position.php?lid=&tid=&keywords={}&start={}'.format(self.q,self.start)
        #     yield scrapy.Request(next_url,callback=self.parse)

        # 直接获取下一页url，发送下一个请求(不断获取下一页地址)
        no_next = response.xpath("//div[@class='pagenav']/a[@class='noactive' and @id='next']/text()")
        # print("下一页",type(no_next))
        if not no_next:
            next_url = "https://hr.tencent.com/" + \
                       response.xpath("//div[@class='pagenav']/a[@id='next']/@href").extract()[0]
            # 返回请求给引擎，引擎交给调度器去请求响应
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_detail(self,response):
        node_list = response.xpath("//table[@class='tablelist textl']")
        for node in node_list:
            item = response.meta['item']
            positionName = node.xpath(".//tr[1]//td/text()").extract()
            positionCity = node.xpath(".//tr[2]/td[1]/text()").extract()
            positionType = node.xpath(".//tr[2]/td[2]/text()").extract()
            positionNum = node.xpath(".//tr[2]/td[3]/text()").extract()
            positionduty = node.xpath(".//tr[3]//ul/li/text()").extract()
            positionrequest = node.xpath(".//tr[4]//ul/li/text()").extract()

            item['positionName'] = positionName[0]
            item['positionCity'] = positionCity[0]
            item['positionType'] = positionType[0] if positionType else None
            item['positionNum'] = positionNum[0]
            item['positionduty'] = '\n'.join(positionduty) #数组转成字符串，换行隔开
            item['positionrequest'] = '\n'.join(positionrequest)

            yield item

