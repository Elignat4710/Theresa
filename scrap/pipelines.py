# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from theresa_app.tasks import save_product


class ScrapPipeline(object):
    def __init__(self):
        self.items = []
    
    def process_item(self, item, spides):
        self.items.append(item._values)
        if len(self.items) >= 15:
            save_product.delay(self.items)
            self.items.clear()
        return item

    def close_spider(self, spider):
        if self.items:
            save_product.delay(self.items)