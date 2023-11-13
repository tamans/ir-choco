import scrapy

class LindtChocolatierSpider(scrapy.Spider):
    name = 'lindtchocolatier_spider'
    # allowed_domains = ['en.maxchocolatier.com']
    start_urls = ['https://www.lindt.ch/de/']

    def parse(self, response):
       
        products = response.xpath('//*[@id="w-node-_5bb703ca-8687-69b9-7189-c26191c5fd53-f5d46110"]')  # Replace with the actual XPath for product items

        for product in products:
            product_info = {
                'name': product.xpath('a[1]/text()').get(),
                'description': product.xpath('p/text()').get(),
                'price': product.xpath('div[2]/p[1]/text()').get(),
            }

            # Check if any relevant data is present
            if any(product_info.values()):
                yield product_info

        # Follow links to other pages if needed
        for next_page in response.css('a.next::attr(href)'):
            yield response.follow(next_page, self.parse)
