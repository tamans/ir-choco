from typing import Any, Optional
import scrapy
import re

class SprungliSpider(scrapy.Spider):
    name = 'spruengli_spider'
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
        cleaned_description = self.clean_text(response.css('div.tab-pane.active#tab-description p').xpath('string()').get());
        cleaned_ingredients = self.clean_text(' '.join(response.xpath('//div[@id="tab-2"]//p//text()').getall()).strip());
        cleaned_price = self.clean_text(response.css('li.price-rating-box > h2::text').get())

        page_info = {
            'site': self.name,
            'docno': response.url,
            'title': response.css('title::text').get(),
            'description': cleaned_description,
            'ingredients': cleaned_ingredients,
            'price': cleaned_price,
        }

        # Check if any relevant data is present
        if any(page_info.values()):
            yield page_info

        # Follow links to other pages if needed
        for next_page in response.css('a.caption::attr(href)').getall():
            yield response.follow(next_page, self.parse)
        # for next_page in response.css('a.caption::attr(href)'):
        #     next_page_url = response.urljoin(next_page.extract().strip())

        # if next_page_url and next_page_url != '#':
        #     yield response.follow(next_page_url, self.parse)

    
    def clean_text(self, raw_text: Optional[str]) -> Optional[str]:
        """
        Clean text by removing extra spaces, including those from line breaks.
        """
        if raw_text:
            return re.sub(r'\s+', ' ', raw_text).strip()
        else:
            return None