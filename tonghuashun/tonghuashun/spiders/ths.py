# -*- coding: utf-8 -*-
import scrapy
import os
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy.spiders import Spider
from tonghuashun.items import TonghuashunItem


class ThsSpider(Spider):
    name = "ths"
    allowed_domains = ["10jqka.com.cn"]
    start_urls = ["http://www.10jqka.com.cn"]
    #redis_key = 'ThsSpider:start_urls'

    def parse(self, response):
        items = []
        # 父标题
        partenttitle = response.xpath('//div[@class="box guide"]//div[@class="item"]/a/text()').extract()
        # 父标题链接
        partentlink = response.xpath('//div[@class="box guide"]//div[@class="item"]/a/@href').extract()
        # 子标题
        sontitle = response.xpath('//div[@class="box guide"]//div[@class="content"]/a/text()').extract()
        # 子标题链接
        sonlink = response.xpath('//div[@class="box guide"]//div[@class="content"]/a/@href').extract()

        for i in range(0, len(partenttitle)):
        # 指定父标题文件夹
            partentfilename = "./news/" + partenttitle[i]
            if(not os.path.exists(partentfilename)):
                os.makedirs(partentfilename)

            for j in range(0, len(sontitle)):
                item = TonghuashunItem()

                item['partenttitle'] = partenttitle[i]
                item['partentlink'] = partentlink[i]

                if_belong = sonlink[j].startswith(item['partentlink'])

                if(if_belong):
                    sonfilename = partentfilename + '/' +sontitle[j]

                    if(not os.path.exists(sonfilename)):
                        os.makedirs(sonfilename)

                    item['sontitle'] = sontitle[j]
                    item['sonlink'] = sonlink[j]
                    item['sonfilename'] = sonfilename

                    items.append(item)

        for item in items:
            yield scrapy.Request(url = item['sonlink'], meta ={"meta_1":item},callback = self.parse_son)

    def parse_son(self, response):

        meta_1 = response.meta["meta_1"]

        # 新闻链接
        newlink = response.xpath('//div[@class="list-con"]//span[@class="arc-title"]/a/@href').extract()
        items = []
        for i in range(0, len(newlink)):
            if_belong = newlink[i].endswith(".shtml") and newlink[i].startswith(meta_1['partentlink'])

            if (if_belong):
                item = TonghuashunItem()
                item['partenttitle'] = meta_1['partenttitle']
                item['partentlink'] = meta_1['partentlink']
                item['sontitle'] = meta_1['sontitle']
                item['sonlink'] = meta_1['sonlink']
                item['newlink'] = newlink[i]
                item['sonfilename'] = meta_1['sonfilename']

                items.append(item)

        for item in items:
            yield scrapy.Request(url=item['newlink'],meta={"meta_2":item},callback=self.parse_item)

    def parse_item(self, response):

        item = response.meta['meta_2']
        contents = ""

        # 新闻标题
        newtitle = response.xpath('//div[@class="main-fl fl"]//h2[@class="main-title"]/text()')
        # 新闻内容
        newcontent = response.xpath('//div[@class="main-text atc-content"]/p/text()').extract()

        for content in newcontent:
            contents += content
        if newtitle !="" and newcontent != "":
            item['newtitle'] = newtitle
            item['newcontent'] = contents

        yield item

"""
#父标题
partenttitle:'//div[@class="box guide"]//div[@class="item"]/a/text()'
#父标题链接
partentlink:'//div[@class="box guide"]//div[@class="item"]/a/@href'
#子标题
sontitle:'//div[@class="box guide"]//div[@class="content"]/a/text()'
#子标题链接
sonlink:'//div[@class="box guide"]//div[@class="content"]/a/@href'
#新闻链接
newlink:'//div[@class="list-con"]//span[@class="arc-title"]/a/@href'
#新闻标题
newtitle:'//div[@class="main-fl fl"]//h2[@class="main-title"]/text()'
#新闻内容
newcontent:'//div[@class="main-text atc-content"]/p/text()'


"""