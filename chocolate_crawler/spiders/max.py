from typing import Any, Optional
import scrapy
import logging
import re

class MaxChocolatier(scrapy.Spider):
    name = 'maxchocolatier_spider'
    allowed_domains = ['en.maxchocolatier.com']

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

        description = self.clean_text(' '.join(response.css('p.pdp__product_desc::text, p.pdp__accordion_desc::text').getall()).strip())
        ingredients = self.clean_text(' '.join(response.css('div.pdp__accordion_declaration > p strong::text, div.pdp__accordion_declaration > p::text').getall()).strip())

        max_info = {
            'site': self.name,
            'page_link': response.url,
            'title': response.css('h1::text').get(),
            'img_link': response.css('img.pdp__product_img_open::attr(src)').get(),
            'description': description,
            'ingredients': ingredients,
            'price': response.css('p.pdp__price::text').get()
        }

        if all(value for value in max_info.values()):
            yield max_info
        else:
            logging.warning(f"Missing data for {response.url}. Skipping.")
            
        for next_page in response.css('a::attr(href)').getall():
            print(next_page)
            yield response.follow(next_page, self.parse)

    def clean_text(self, raw_text: Optional[str]) -> Optional[str]:
        """
        Clean text by removing extra spaces, including those from line breaks.
        """
        if raw_text:
            return re.sub(r'\s+', ' ', raw_text).strip()
        else:
            return None