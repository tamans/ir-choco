import scrapy

class SprungliSpider(scrapy.Spider):
    name = 'sprungli_spider'
    allowed_domains = ['spruengli.ch']
    start_urls = ['https://www.spruengli.ch/']

    def parse(self, response):
        # Extract information about the page
        page_info = {
            'title': response.css('title::text').get(),
            'description': response.css('meta[name="description"]::attr(content)').get(),
            'ingredients': response.css('div.ingredients::text').get(),
            'price': response.css('span.price::text').get(),
        }

        # Check if any relevant data is present
        if any(page_info.values()):
            yield page_info

        # Follow links to other pages if needed
        for next_page in response.css('a::attr(href)'):
            yield response.follow(next_page, self.parse)
