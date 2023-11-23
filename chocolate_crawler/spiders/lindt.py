from typing import Any, Optional
import scrapy

class LindtChocolatierSpider(scrapy.Spider):
    name = 'lindt_spider'
    allowed_domains = ['https://www.chocolate.lindt.com']

    def __init__(self, tags=None, *args, **kwargs):

        self.start_urls = []

        if tags == 'null':
            self.tags = []
        elif tags:
            self.tags = tags.split(',')
        else:
            self.tags = ['our-chocolate'
                        #  'our-chocolate/our-brands', 'our-chocolate/our-brands/lindor', 'our-brands/excellence',
                        # 'our-chocolate/our-brands/pralines','our-chocolate/our-brands/creation','our-chocolate/our-brands/hello', 'our-chocolate/gift-ideas', 
                        # 'our-chocolate/type',
                        # 'our-chocolate/type/dark-chocolate', 'our-chocolate/type/white-chocolate', 'our-chocolate/type/milk-chocolate'
                        ]

        self.start_urls = [f'https://www.chocolate.lindt.com/{tag}' for tag in self.tags]

        super().__init__(**kwargs)

    def parse(self, response):

        lindt_info = {
            'site': self.name,
            'page_link': response.url,  # Replace with a suitable identifier
            'title': response.css('h1::text').get() or response.css('h2::text').get() or response.css('h3::text').get(),
            'description': response.css('div.product.attribute.description::text').get(),
            'ingredients': response.css('span.ingredient-label:contains("Ingredients:") + p::text').get(),
            'allergens': response.css('span.ingredient-label.contains("Allergens:") + p::text').get(),
            'cacao solids': response.css('span.ingredient-label.contains("Cacao Solids %") + p::text').get(),
            'price': response.css('span.price::text').get() or response.css('div.price-box.price-final_price').get(),
        }

        # Check if any relevant data is present
        if all( value for value in lindt_info.values()):
            yield lindt_info
        # else:
        #     logging.warning(f"Missing data for {response.url}. Skipping.")
       
        # products = response.xpath('//*[@id="w-node-_5bb703ca-8687-69b9-7189-c26191c5fd53-f5d46110"]')  # Replace with the actual XPath for product items

        # for product in products:
        #     product_info = {
        #         'name': product.xpath('a[1]/text()').get(),
        #         'description': product.xpath('p/text()').get(),
        #         'price': product.xpath('div[2]/p[1]/text()').get(),
        #     }

        #     # Check if any relevant data is present
        #     if any(product_info.values()):
        #         yield product_info

        # Follow links to other pages if needed
        for next_page in response.css('a.next::attr(href)'):
            yield response.follow(next_page, self.parse)
