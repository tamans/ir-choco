from typing import Any, Optional
import scrapy
import logging

class MaxChocolatier(scrapy.Spider):
    name = 'maxchocolatier_spider'
    allowed_domains = ['en.maxchocolatier.com']
    # start_urls = ['http://en.maxchocolatier.com/shop']

    def __init__(self, tags=None,*args, **kwargs):
        if tags == 'null':
            self.tags = []
        elif tags:
            self.tags = tags.split(',')
        else:
            self.tags = ['pralinen', 'schokoladentafeln', 'plaettli', 
                        'degustationsboxen', 'nuesse', 'schoggi-abos', 'max-favoriten']
        self.start_urls = [f'https://en.maxchocolatier.com/shop?category={tag}' for tag in self.tags]
        super().__init__(**kwargs)

    def parse(self, response):

        max_info = {
            'site': self.name,
            'page_link': response.url,
            'title': response.css('h1::text').get(),
            'description': response.css('p.pdp__product_desc::text, p.pdp__accordion_desc::text').getall(),
            'ingredients': response.css(
                'div.pdp__accordion_declaration > p strong::text, div.pdp__accordion_declaration > p::text').getall(),
            'price': response.css('p.pdp__price::text').get()
        }

        if all(value for value in max_info.values()):
            yield max_info
        else:
            logging.warning(f"Missing data for {response.url}. Skipping.")
        
        for next_page in response.css('a::attr(href)'):
            yield response.follow(next_page, self.parse)


# import scrapy

# class MaxChocolatierSpider(scrapy.Spider):
#     name = 'maxchocolatier_spider'
#     start_urls = ['https://en.maxchocolatier.com/shop']

#     def parse(self, response):
#         products = response.xpath('//div[@class="pop__col__wrapper jetboost-list-wrapper-lv23 jetboost-list-wrapper-41nl jetboost-list-wrapper-4nrx jetboost-list-wrapper-4gee jetboost-list-wrapper-lm2b jetboost-list-wrapper-4p2g w-dyn-list"]//*')  # Replace with the actual XPath for product items
     
#         for product in products:
#             name = product.xpath('.//a[@class="pop__product_card_title"]/text()').extract_first()
#             desc = product.xpath('.//p[@class="pop__product__card_desc"]/text()').extract_first()
#             price = product.xpath('.//p[@class="pop__product_card_price"]/text()').extract_first()

#             print(name)
#             print(desc)
#             print(price)

#             if name and desc and price:
#                 yield {"name": name.strip(), "desc": desc.strip(), "price": price.strip()}

#         # Follow links to other pages if needed
#         for next_page in response.css('a.next::attr(href)'):
#             yield response.follow(next_page, self.parse)