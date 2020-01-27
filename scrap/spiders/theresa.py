import scrapy
from scrap.items import Product
from scrapy_redis.spiders import RedisSpider 


class TheresaSpider(RedisSpider):
    name = 'theresa'

    def parse(self, response):
        for p in range(1, 3):
            page = response.url + '?p=' + str(p)
            yield scrapy.Request(url=page, callback=self.parse_page)

    def parse_page(self, response):
        urls = response.xpath(
            '//div[contains(@class, "category-products ")]/ul/li/a/@href'
        ).extract()

        for url in urls:
            yield scrapy.Request(
                url=url, callback=self.parse_product
            )

    def parse_product(self, response):
        item = Product()
        item['url'] = response.url
        item['category'] = response.xpath(
            '//li[contains(@class, "category8522")]/a/span/text()'
        ).extract()
        item['title'] = response.xpath(
            '//div[contains(@class, "product-shop")]/div[contains(@class, "product-name")]/span/text()'
        ).extract()
        item['price'] = response.xpath(
            '//div[contains(@class, "price-info")]/div/p[contains(@class, "special-price")]/span/text()'
        ).extract()
        item['description'] = response.xpath(
            '//p[contains(@class, "product-description")]/text()'
        ).extract()
        item['images'] = response.xpath('//div[contains(@class, "more-views")]/ul/li/img/@src').extract()
        item['sizes'] = response.xpath(
            '//div[contains(@class, "fit-advisor")]/ul/li/text()'
        ).extract()
        return item
