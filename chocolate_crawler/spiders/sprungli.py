import scrapy

class SprungliSpider(scrapy.Spider):
    name = 'sprungli_spider'
    allowed_domains = ['spruengli.ch']
    start_urls = ['https://www.spruengli.ch/']

    def parse(self, response):
        # Extract information about chocolates from the webpage
        for product in response.css('.product-item'):
            chocolate_info = {
                'name': product.css('.product-title a::text').get(),
                'description': product.css('.product-description::text').get(),
                'price': product.css('.product-price .price::text').get(),
            }

            # Check if any relevant data is present
            if any(chocolate_info.values()):
                yield chocolate_info

        # Follow pagination links to crawl additional pages
        next_page = response.css('.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
