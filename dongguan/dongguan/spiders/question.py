# -*- coding: utf-8 -*-
#import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from dongguan.items import DongguanItem
from scrapy_redis.spiders import RedisCrawlSpider

class QuestionSpider(RedisCrawlSpider):
    name = 'question'
    allowed_domains = ['wz.sun0769.com']
    #start_urls = ['http://wz.sun0769.com/index.php/question/report?page=0']
    redis_key = "QuestionSpider:start_urls"

    rules = (
        Rule(LinkExtractor(allow=(r"/question/report?"))),
        Rule(LinkExtractor(allow=(r"/question/\d+/\d+.shtml")), callback='parse_item'),
    )

    def parse_item(self, response):
        item = DongguanItem()

        item['question'] = response.xpath("//div[@class='wzy1']//td/span[1]/text()").extract()[0]
        item['num'] = response.xpath("//div[@class='wzy1']//td/span[2]/text()").extract()[0]
        item['context'] = response.xpath("//div[@class='wzy1']//tr[1]/td[@class='txt16_3']/text()").extract()[0]
        item['url'] = response.url


        yield item
