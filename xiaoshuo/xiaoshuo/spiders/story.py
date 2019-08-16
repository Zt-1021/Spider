# -*- coding: utf-8 -*-
import scrapy
from xiaoshuo.items import XiaoshuoItem


class StorySpider(scrapy.Spider):
    name = "story"
    allowed_domains = ["zongheng.com"]
    index = 1
    start_urls = (
        "http://huayu.zongheng.com/store/c0/c0/u1/p1/v0/s0/ALL.html",
    )

    def parse(self, response):

        for each in response.xpath("//div[@class='table_con']"):
            item = XiaoshuoItem()
            # 小说类型
            storystyle = each.xpath(".//span[@class='book']/em/a/text()").extract()
            # 小说名
            storyname = each.xpath(".//span[@class='book']//a[@class='f14']/text()").extract()
            # 小说章节
            storychapter = each.xpath(".//span[@class='book']/a[@target='_blank'][2]/text()").extract()
            # 总点击
            storyclick = each.xpath(".//span[@class='click']/text()").extract()
            # 作者
            storyauthor = each.xpath(".//span[@class='author']/a/text()").extract()
            # 更新时间
            storyupdatetime = each.xpath(".//span/span[@class='time']/text()").extract()

        for i in range(0, 50):
            item['storyStyle'] = storystyle[i].strip()
            item['storyName'] = storyname[i].strip()
            item['storyChapter'] = storychapter[i].strip()
            item['storyClick'] = storyclick[i].strip()
            item['storyAuthor'] = storyauthor[i].strip()
            item['storyUpdateTime'] = storyupdatetime[i].strip()


            yield item
        if self.index < 5:
            self.index += 1

        yield scrapy.Request("http://huayu.zongheng.com/store/c0/c0/u1/p" + str(self.index) + "/v0/s0/ALL.html",
                             callback=self.parse)


