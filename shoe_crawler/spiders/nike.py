import scrapy
import json
from shoe_crawler.items import Shoe
from scrapy.loader import ItemLoader

class NikeSpider(scrapy.Spider):
    name = 'nike'
    base_url = 'https://www.nike.com/'
    start_urls = [
        "https://www.nike.com/product_feed/rollup_threads/v2?filter=marketplace%28US%29&filter=language%28en%29&filter=employeePrice%28true%29&filter=attributeIds%280f64ecc7-d624-4e91-b171-b83a03dd8550%2C16633190-45e5-4830-a068-232ac7aea82c%29&anchor=0&count=24&consumerChannelId=d9a5bc42-4b9c-4976-858a-f159cf99c647",
    ]

    def parse(self, response):

        data = json.loads(response.text)

        for obj in data['objects']:
            prod_info = obj['productInfo'][0]

            l = ItemLoader(item=Shoe())

            l.add_value('title', prod_info['productContent']['title'])
            l.add_value('subtitle', prod_info['productContent']['subtitle'])
            l.add_value('full_price', prod_info['merchPrice']['fullPrice'])
            l.add_value('current_price', prod_info['merchPrice']['currentPrice'])
            yield l.load_item()

        if data['pages']['next']:
            next_page = self.base_url + data['pages']['next']
            yield scrapy.Request(url=next_page, callback=self.parse)



