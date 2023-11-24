from typing import Any, Optional
import scrapy

class SprungliSpider(scrapy.Spider):
    name = 'sprungli_spider'
    allowed_domains = ['spruengli.ch']
    # start_urls = ['https://www.spruengli.ch/en/shop']

    def __init__(self, tags=None, *args,  **kwargs):
        if tags =='null':
            self.tags = []
        elif tags:
            self.tags = tags.split(',')
        else:
            self.tags = ['st-nicholas-gifts', 'christmas-gifts', 'luxemburgerli', 'chocolates-truffle',
                         'mix-and-match-pralines-truffles', 'gift-packages-arrangements', 'chocolate-bars', 'specialities',
                         'cakes', 'dessert']
        
        self.start_urls = [f'https://www.spruengli.ch/en/shop/{tag}' for tag in self.tags]

        super().__init__(**kwargs)

    def parse(self, response):
        # Extract information about the page
        page_info = {
            'docno': response.url,
            'title': response.css('title::text').get(),
            'description': response.css('div.tab-pane.active#tab-description p').xpath('string()').get(),
            'ingredients': response.xpath('//div[@id="tab-2"]//p//text()').getall(),
            'price': response.css('li.price-rating-box > h2::text').get(),
        }

        # Check if any relevant data is present
        if any(page_info.values()):
            yield page_info

        # Follow links to other pages if needed
        for next_page in response.css('a.caption::attr(href)'):
            yield response.follow(next_page, self.parse)
