import scrapy

class MaxChocolatierSpider(scrapy.Spider):
    name = 'maxchocolatier_spider'
    allowed_domains = ['en.maxchocolatier.com']
    start_urls = ['https://en.maxchocolatier.com/']

    def parse(self, response):
        # Extract information about the products from the webpage
        products = response.css('div.product')
        
        for product in products:
            title = product.css('h2.product-title a::text').get()
            description = product.css('div.product-description::text').get()
            price = product.css('span.price::text').get()

            # Check if any relevant data is present
            if title and description and price:
                yield {
                    'title': title.strip(),
                    'description': description.strip(),
                    'price': price.strip(),
                    'url': response.url,
                }

        # Follow links to other pages if needed
        for next_page in response.css('li.item.pages-item-next a::attr(href)'):
            yield response.follow(next_page, self.parse)
