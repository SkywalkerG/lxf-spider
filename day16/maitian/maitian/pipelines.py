# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings

class MaitianPipeline(object):
    def process_item(self, item, spider):
        return item

'''
MONGODB_HOST = 'localhost'
MONGODB_PORT = '27017'
MONGODB_DBNAME = 'maitian'
MONGODB_DOCNAME = 'zufang'
'''
class MongoPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        client = pymongo.MongoClient(host, port)

        db_name = settings['MONGODB_DBNAME']
        db = client[db_name]

        table_name = settings['MONGODB_DOCNAME']
        self.table = db[table_name]

    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls(
    #         mongo_url = crawler.settings.get('')
    #     )


    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.table.insert(dict(item))
        return item

'''
MONGODB_HOST = 'localhost'
MONGODB_PORT = '27017'
MONGODB_DBNAME = 'maitian'
MONGODB_DOCNAME = 'zufang'
'''
# class MongoPipeline(object):
#
#     collection_name = 'scrapy_items'
#
#     def __init__(self, mongo_uri, mongo_db):
#         self.mongo_uri = mongo_uri
#         self.mongo_db = mongo_db
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(
#             mongo_uri=crawler.settings.get('MONGO_URI'),
#             mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
#         )

    # def open_spider(self, spider):
    #     self.client = pymongo.MongoClient(self.mongo_uri)
    #     self.db = self.client[self.mongo_db]
    #
    # def close_spider(self, spider):
    #     self.client.close()
    #
    # def process_item(self, item, spider):
    #     self.db[self.collection_name].insert_one(dict(item))
    #     return item