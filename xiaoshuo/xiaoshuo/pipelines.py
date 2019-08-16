# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class XiaoshuoPipeline(object):

    def __init__(self):
        self.fileName = open('xiaoshuo.json', 'w')

    def process_item(self, item, spider):
        self.fileName.write((json.dumps(dict(item), ensure_ascii=False)+'\n').encode('utf-8'))
        return item

    def close_file(self):
        self.fileName.close()