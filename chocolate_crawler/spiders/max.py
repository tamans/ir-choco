import scrapy

class MaxChocolatierSpider(scrapy.Spider):
    name = 'maxchocolatier_spider'
    start_urls = ['https://en.maxchocolatier.com/shop']

    def parse(self, response):
        products = response.xpath('//div[@class="pop__col__wrapper jetboost-list-wrapper-lv23 jetboost-list-wrapper-41nl jetboost-list-wrapper-4nrx jetboost-list-wrapper-4gee jetboost-list-wrapper-lm2b jetboost-list-wrapper-4p2g w-dyn-list"]//*')  # Replace with the actual XPath for product items
     
        for product in products:
            name = product.xpath('.//a[@class="pop__product_card_title"]/text()').extract_first()
            desc = product.xpath('.//p[@class="pop__product__card_desc"]/text()').extract_first()
            price = product.xpath('.//p[@class="pop__product_card_price"]/text()').extract_first()

            print(name)
            print(desc)
            print(price)

            if name and desc and price:
                yield {"name": name.strip(), "desc": desc.strip(), "price": price.strip()}

        # Follow links to other pages if needed
        for next_page in response.css('a.next::attr(href)'):
            yield response.follow(next_page, self.parse)
