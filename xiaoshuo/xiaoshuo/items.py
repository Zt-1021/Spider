# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaoshuoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 小说类型
    storyStyle = scrapy.Field()
    # 小说名
    storyName = scrapy.Field()
    # 小说章节
    storyChapter = scrapy.Field()
    # 总点击
    storyClick = scrapy.Field()
    # 作者
    storyAuthor = scrapy.Field()
    # 更新时间
    storyUpdateTime = scrapy.Field()
