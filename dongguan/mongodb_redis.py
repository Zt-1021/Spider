import redis
import json
import pymongo

def main():
    rediscli = redis.StrictRedis(host="127.0.0.1", port=6379, db=0)
    mongocli = pymongo.MongoClient(host="127.0.0.1", port=27017)
    db = mongocli["dongguan"]
    sheet = db["dg"]
    while True:
        source, data = rediscli.blpop(["dongguan:items"])
        item = json.loads(data)
        sheet.insert(item)


if __name__ == "__main__":
    main()
