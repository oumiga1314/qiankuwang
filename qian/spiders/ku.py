# -*- coding: utf-8 -*-
import scrapy

from  qian.items import QianItem
class KuSpider(scrapy.Spider):
    name = 'ku'
    allowed_domains = ['588ku.com']
    start_urls = ['http://588ku.com/sucai/0-pxnum-0-0-meinv-0-1/']

    def parse(self, response):
      list = response.css('.img-show a::attr(href)').extract()
      for img_url in list:
          yield scrapy.Request(img_url, callback=self.content)
    def content(self, response):
        item = QianItem()
        item['img_url'] = response.css(".img-l-box img::attr(src)").extract()
        yield item