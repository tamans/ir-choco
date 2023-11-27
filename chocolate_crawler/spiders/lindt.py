from typing import Any, Optional
import scrapy
import logging

class LindtChocolatierSpider(scrapy.Spider):
    name = 'lindt_spider'
    allowed_domains = ['chocolate.lindt.com']
    # start_urls = ['http://www.chocolate.lindt.com/our-chocolate']


    def __init__(self, tags=None, *args, **kwargs):

        self.start_urls = []

        if tags == 'null':
            self.tags = []
        elif tags:
            self.tags = tags.split(',')
        else:
            self.tags = ['our-brands', 'gift-ideas']

        self.start_urls = [f'https://www.chocolate.lindt.com/our-chocolate/{tag}' for tag in self.tags]
        super().__init__(**kwargs)

    def parse(self, response):

        lindt_info = {
            'site': self.name,
            'page_link': response.url,
            'title': response.css('span.base::text').get() or response.css('h2::text').get() or response.css('h3::text').get(),
            'description': response.css('div.value::text').get() or response.css('div.value[itemprop="description"] div[data-decoded="true"]::text').get(),
            'ingredients': response.xpath('//td[@class="col label" and @scope="row"]/p/text()').get(),
            'allergens': self.extract_category(response, 'Allergens:'),
            'cacao_solids': self.extract_category(response, 'Cacao Solids %'),
            'price': response.css('span.price::text').get() or response.css('div.price-box.price-final_price').get(),
        }

        # Check if any relevant data is present
        if all( value for value in lindt_info.values()):
            yield lindt_info
        else:
            logging.warning(f"Missing data for {response.url}. Skipping.")
       
        # Follow links to other pages if needed
        # for next_page in response.css('a.product-item-link::attr(href)'):
        for next_page in response.css('a::attr(href)'):
            yield response.follow(next_page, self.parse)

        # for nxt in response.css('a.product.photo.product-item-photo::attr(href)'):
        #     yield(response.folloow(nxt,self.parse))

    def extract_category(self, response, category_keyword):
        category_selector = f'span.ingredient-label:contains("{category_keyword}")'
        p_selector = f'{category_selector} + p::text'
        return response.css(p_selector).get()

logging.getLogger().setLevel(logging.DEBUG)
