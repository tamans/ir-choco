import scrapy

class ChocolateSpider(scrapy.Spider):
    name = 'chocolate_spider'
    allowed_domains = ['laderach.com']
    start_urls = ['https://laderach.com']

    def parse(self, response):
        # Extract information about chocolate from the webpage
        chocolate_info = {
            'docno': response.url,  # Replace with a suitable identifier
            'title': response.css('h1::text').get(),
            'description': response.css('p::text').get(),
            'ingredients': response.css('div.ingredients::text').get(),
            'price': response.css('span.price::text').get(),
        }

        # Check if any relevant data is present
        if any(chocolate_info.values()):
            yield chocolate_info

        # Follow links to other pages if needed
        for next_page in response.css('a::attr(href)'):
            yield response.follow(next_page, self.parse)
