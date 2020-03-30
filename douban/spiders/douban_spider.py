# -*- coding: utf-8 -*-
import scrapy

from douban.items import DoubanItem


class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        movie_list = response.xpath("//ol[@class='grid_view']/li")
        for i in movie_list:
            douban_item = DoubanItem()
            douban_item['serial_number'] = i.xpath(".//div[@class='item']//em/text()").extract_first()
            douban_item['movie_name'] = i.xpath(
                ".//div[@class='item']//div[@class='info']//div[@class='hd']/a/span[1]/text()").extract_first()
            blanck_space_introduce = i.xpath(
                ".//div[@class='item']//div[@class='info']//div[@class='bd']/p[1]/text()").extract()
            for j in blanck_space_introduce:
                final_introduce = ''.join(j.split())
                douban_item['introduce'] = final_introduce
            douban_item['start'] = i.xpath(
                ".//div[@class='item']//div[@class='info']//div[2]//div[@class='star']//span[2]/text()").extract_first()
            douban_item['comment_number'] = i.xpath(
                ".//div[@class='item']//div[@class='info']//div[2]//div[@class='star']//span[4]/text()").extract_first()
            douban_item['describe'] = i.xpath(
                ".//div[@class='item']//div[@class='info']//div[2]//p[@class='quote']//span[1]/text()").extract_first()
            yield douban_item
            next_link = response.xpath("//span[@class='next']/link/@href").extract()
            if next_link:
                next_link = next_link[0]
                yield scrapy.Request("https://movie.douban.com/top250"+next_link, callback=self.parse)
