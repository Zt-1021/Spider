#!/usr/bin/env python

import redis
import MySQLdb
import json


def parse_item():
    rediscli = redis.Redis(host="127.0.0.1", port=6379, db=0)
    mysqlcli = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="mysql", db="dongguan")

    source,data = rediscli.blpop("question:items")
    item = json.loads(data)
    print item
    cursor = mysqlcli.cursor()
    cursor.execute("insert into dg (num,question,context,url) values(%s,%s,%s,%s)"%[item['num'],item['question'],item['context'],item['url']])
    mysqlcli.commit()
    cursor.close()



if __name__ == "__main__":
    parse_item()
