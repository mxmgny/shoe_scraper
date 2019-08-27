import scrapy


class Shoe(scrapy.Item):
    title = scrapy.Field()
    subtitle = scrapy.Field()
    current_price = scrapy.Field()
    full_price = scrapy.Field()
    manufacturer = scrapy.Field()