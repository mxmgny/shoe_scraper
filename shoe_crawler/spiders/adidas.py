# import scrapy
# import json
#
# api = "https://www.adidas.com/api/search/product/EE6465?sitePath=us"
# start_url = "https://www.adidas.com/api/search/taxonomy?sitePath=us&isPrefetch=true&query=shoes&start=5"
#
#
# class Adidas(scrapy.Spider):
#     name = 'adidas'
#
#     start_urls = [
#         'https://www.adidas.com/api/search/taxonomy?sitePath=us&isPrefetch=true&query=shoes'
#     ]
#
#     def parse(self, response):
#         json_obj = json.loads(response.body)
#         items = json_obj['itemList']['items']