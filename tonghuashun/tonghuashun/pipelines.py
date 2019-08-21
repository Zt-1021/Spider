# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class TonghuashunPipeline(object):
    def process_item(self, item, spider):

        sonlink = item['sonlink']

        filename = sonlink[7:-6].replace("/","_")
        filename += ".txt"

        f = open(item['sonfilename'] + '/' + filename, 'w')
        f.write(item['newcontent'])
        f.close()

        return item
