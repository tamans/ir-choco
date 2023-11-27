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
            'description': ' '.join(response.css('p.pdp__product_desc::text, p.pdp__accordion_desc::text').getall()).strip(),
            'ingredients': ' '.join(response.css('div.pdp__accordion_declaration > p strong::text, div.pdp__accordion_declaration > p::text').getall()).strip(),
            'price': response.css('p.pdp__price::text').get()
        }

        if all(value for value in max_info.values()):
            yield max_info
        else:
            logging.warning(f"Missing data for {response.url}. Skipping.")
        # response.css('a.pop__product_card_title::attr(href)').extract()
        # response.xpath('//a[@class="pop__product_card_title"]/@href').extract()
        # for next_page in response.css('a.pop__product_card_title::attr(href)'):
        for next_page in response.css('a::attr(href)'):
            yield response.follow(next_page, self.parse)