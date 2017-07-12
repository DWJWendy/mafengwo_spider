# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TravelreviewItem(scrapy.Item):
    source = scrapy.Field()  # 数据来源
    user_id = scrapy.Field()  # 评论用户id
    avatar = scrapy.Field()  # 评论用户头像
    level = scrapy.Field()  # 评论用户等级
    useful_num = scrapy.Field()  # 评论有用数
    star = scrapy.Field()  # 评论星级
    content = scrapy.Field()  # 评论内容
    user_name = scrapy.Field()  # 用户名
    time = scrapy.Field()  # 评论时间

class TravelCrawlItem(scrapy.Item):
    # 定义爬取的景点评论
    review = scrapy.Field() #关于景点评论
    location = scrapy.Field()  #景点位置
    attraction = scrapy.Field() #景点名
    attraction_id = scrapy.Field() #景点id
    info = scrapy.Field()  #关于景点的具体地址、浏览量、评论量等信息


class TravelfoodItem(scrapy.Item):
    # 定义爬取的美食评论
    food_name = scrapy.Field()  #美食名
    food_id = scrapy.Field() #美食id
    info = scrapy.Field() #关于美食的具体地址、浏览量、评论量等信息
    review = scrapy.Field() #关于此美食的评论数据
    location = scrapy.Field() #输入城市

class TravelhotelItem(scrapy.Item):
    # 定义爬取的酒店评论
    hotel_name = scrapy.Field()  #酒店名
    hotel_id = scrapy.Field() #酒店id
    info = scrapy.Field() #关于酒店的具体地址、浏览量、评论量等信息
    review = scrapy.Field() #关于此酒店的评论数据
    location = scrapy.Field()  #输入城市


class TravelnoteItem(scrapy.Item):
    # 定义游记的信息
    time = scrapy.Field()  #出发时间
    day = scrapy.Field()   #出行天数
    people = scrapy.Field() #人物
    cost = scrapy.Field() #花费
    note = scrapy.Field()  # 游记内容
    note_id = scrapy.Field() #游记id
    note_title = scrapy.Field() #游记标题
    position = scrapy.Field()  #景点位置
    location = scrapy.Field() #城市
    info = scrapy.Field()
