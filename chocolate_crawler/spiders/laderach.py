import logging
from typing import Any, Optional
import scrapy
import re
from scrapy.selector import Selector

class LaderachSpider(scrapy.Spider):
    name = 'laderach_spider'
    allowed_domains = ['laderach.com']
    
    def __init__(self, tags=None, *args, **kwargs):

        self.start_urls = []

        if tags == 'null':
            self.tags = []
        elif tags:
            self.tags = tags.split(',')
        else:
            self.tags = ['alle-produkte', 'geschenke', 'frischschoggitm', 'pralines-truffes',
                        'tafeln','snacking','vegan', 'celebration-gifts', 'gifts-for-sharing',
                        'thank-you-gifts', 'greeting-cards']
            
        base_url = 'https://laderach.com/ch-en/'  # Use a base URL without subdomains
        self.start_urls = [f'{base_url}{tag}' for tag in self.tags]
        # self.start_urls = [f'https://laderach.com/ch-en/{tag}' for tag in self.tags]

        super().__init__(**kwargs)
        

    def parse(self, response):
        logging.info(f"Processing page: {response.url}")

        # remove extra spaces from the texts
        cleaned_title = self.clean_text(response.css('h1::text').get() or response.css('h2::text').get() or response.css('h3::text').get());
        cleaned_description = self.clean_text(response.css('div.product-facts::text').get() 
                            or response.css('div.main-text::text').get() or response.css('div.category-view.container > p::text').get());
        cleaned_ingredients = self.clean_text(self.extract_ingredients(response));
        cleaned_allergens = self.clean_text(self.extract_additional_info(response));


        laderach_info = {
            'site': self.name,
            'page_link': response.url,  # Replace with a suitable identifier
            'title': cleaned_title,
            'description': cleaned_description,
            'ingredients': cleaned_ingredients,
            'allergens': cleaned_allergens,
            'price': response.css('span.price::text').get() or response.css('div.price-box.price-final_price').get(),
        }

        # Check if any relevant data is present
        if all( value for value in laderach_info.values()):
            yield laderach_info
        # else:
        #     logging.warning(f"Missing data for {response.url}. Skipping.")

        # Follow links to other pages if needed
        # for next_page in response.css('a::attr(href)'):
            
        #     yield response.follow(next_page, self.parse)

        for next_page in response.css('a.product-item-link::attr(href)'):
            next_page_url = next_page.extract().strip()

            if next_page_url and '/ch-en/' in next_page_url:
                logging.info(f"Following link to: {next_page_url}")
                yield response.follow(next_page_url, self.parse)


    # combines the underlined and normal ingredient elements
    def extract_ingredients(self, response):
        # Extracting text content of nodes following the "Ingredients" label
        ingredients_nodes = response.xpath('//strong[contains(text(), "Ingredients")]/following-sibling::text()').extract()
        ingredients_text = ' '.join(ingredients_nodes).strip()

        # Extracting text content of <u> elements within <p> tags
        additional_ingredients = response.xpath('//p//u/text()').extract()
        additional_ingredients_text = ' '.join(additional_ingredients).strip()

        # Combine both sets of ingredients
        combined_ingredients = f'{ingredients_text} {additional_ingredients_text}'

        return combined_ingredients.strip()

    # Allergens 
    def extract_additional_info(self, response):
        additional_info = response.css('span.alt-edited::text').get()
        return additional_info.strip() if additional_info else None
    
    def clean_text(self, raw_text: Optional[str]) -> Optional[str]:
        """
        Clean text by removing extra spaces, including those from line breaks.
        """
        if raw_text:
            return re.sub(r'\s+', ' ', raw_text).strip()
        else:
            return None