# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TonghuashunItem(scrapy.Item):
    # define the fields for your item here like:
    
    #父标题
    partenttitle = scrapy.Field()
    #父标题链接
    partentlink = scrapy.Field()
    #子标题
    sontitle = scrapy.Field()
    #子标题链接
    sonlink = scrapy.Field()
    #子文件名
    sonfilename = scrapy.Field()
    #新闻链接
    newlink = scrapy.Field()
    #新闻标题
    newtitle = scrapy.Field()
    #新闻内容
    newcontent = scrapy.Field()


