##1.创建一个Scrapy项目 
 - scrapy startproject TencentJob 

##2.定义提取的Item
```python  
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
```
##3.编写爬取网站的 spider 并提取 Item
 - 创建spider，指定爬虫名tencentjob和爬取的范围  
 	* scrapy genspider tencentjob 'hr.tencent.com'
 	* 执行入口url：
 	```python  
    q = "请输入关键词"  
    start = 0  
    start_urls = ['https://hr.tencent.com/position.php?lid=&tid=&keywords={}&start={}'.format(q,start)]
	```
	* 在parse方法中使用xpath提取数据
	* 创建item对象，使用 request.meta 在回调函数间传递参数，用于从多个页面构建item的数据  
	```python
	item = TencentjobItem()
    positionUrl  = "https://hr.tencent.com/" + job.xpath("./td[1]/a/@href").extract()[0]
    releaseTime = job.xpath("./td[5]/text()").extract()
    item["releaseTime"] = releaseTime[0]
    request = scrapy.Request(positionUrl, callback=self.parse_detail)

    # 使用 request.meta 在回调函数间传递参数，用于从多个页面构建item的数据
    request.meta['item'] = item
    yield request
	``` 
	* 传递item给管道：yield item
	* 获取到下一页url，发送下一个请求
##4.编写 Item Pipeline 来存储提取到的Item(即数据)
 - 使用pymysql，打开mysql数据库，创建表tencentjob
 - 定义表字段，设置job_id为主键，且自动递增
 - 按顺序insert表tencentjob

##5.启动spider程序
 - scrapy crawl tencentjob
 - 爬取结果如下：
![](https://i.imgur.com/fKjbkLs.png)