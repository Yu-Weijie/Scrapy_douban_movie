# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #序号
    serial_number = scrapy.Field()
    #名称
    movie_name = scrapy.Field()
    #介绍
    introduce = scrapy.Field()
    #评论数
    comment_number = scrapy.Field()
    #星级
    start = scrapy.Field()
    #描述
    describe = scrapy.Field()


