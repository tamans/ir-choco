import scrapy

class MaxChocolatierSpider(scrapy.Spider):
    name = 'maxchocolatier_spider'
    allowed_domains = ['en.maxchocolatier.com']
    start_urls = ['https://en.maxchocolatier.com/']

    def parse(self, response):
        products = response.css('.product-inner')
        print(response.body)
        for product in products:
            product_info = {
                'name': product.css('.pop__product_card_title a::text').get(),
                'description': product.css('.pop__product_card_desc p::text').get(),
                'price': product.css('.pop__product_card_price p::text').get(),
                # 'price': product.css('.price .woocommerce-Price-amount::text').get(),
            }
            

            if any(product_info.values()):
                yield product_info

        # Follow links to other pages if needed
        for next_page in response.css('a.next::attr(href)'):
            yield response.follow(next_page, self.parse)
