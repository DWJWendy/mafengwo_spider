# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy import log
from items import TravelnoteItem,TravelhotelItem,TravelfoodItem,TravelCrawlItem

class MongoDBPipleline(object):
    def __init__(self):
        clinet = pymongo.MongoClient("localhost", 27017)
        db = clinet["mfw_pic"]
        self.spot_review = db["spot_review"]
        self.note = db["note"]
        self.food_review = db["food_review"]
        self.hotel_review = db["hotel_review"]

    def process_item(self, item, spider):
        """ 判断item的类型，并作相应的处理，再入数据库 """
        if isinstance(item, TravelCrawlItem):
            try:
                self.spot_review.insert(dict(item))
                log.msg("News added to MongoDB database!", level=log.DEBUG, spider=spider)
            except Exception:
                pass
        elif isinstance(item, TravelnoteItem):
            try:
                self.note.insert(dict(item))
                log.msg("News added to MongoDB database!", level=log.DEBUG, spider=spider)
            except Exception:
                pass
        elif isinstance(item, TravelfoodItem):
            try:
                self.food_review.insert(dict(item))
                log.msg("News added to MongoDB database!", level=log.DEBUG, spider=spider)
            except Exception:
                pass
        elif isinstance(item, TravelhotelItem):
            try:
                self.hotel_review.insert(dict(item))
                log.msg("News added to MongoDB database!", level=log.DEBUG, spider=spider)
            except Exception:
                pass
        return item
