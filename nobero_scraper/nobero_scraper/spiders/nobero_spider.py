import scrapy

class NoberoSpider(scrapy.Spider):
    name = "nobero"
    start_urls = ["https://nobero.com/pages/men"]

    def parse(self, response):
        subcategories = response.css('div[class*="custom-page-season-grid-item"] a::attr(href)').getall()
        for subcategory in subcategories:
            yield response.follow(subcategory, self.parse_subcategory)

    def parse_subcategory(self, response):
        product_urls = response.css('.product-grid-item a::attr(href)').getall()
        for product_url in product_urls:
            yield response.follow(product_url, self.parse_product)

    def parse_product(self, response):
        category = response.css('.breadcrumb li:nth-child(2) a::text').get()
        title = response.css('.product-title h1::text').get()
        price = response.css('.current-price span::text').get()
        mrp = response.css('.price-compare-at span::text').get()
        last_7_day_sale = response.css('.discounted-price span::text').get()
        
        available_skus = []
        for variant in response.css('.product-form__option'):
            color = variant.css('.product-form__option-label::text').get()
            sizes = variant.css('.product-form__option-values li::text').getall()
            available_skus.append({
                'color': color.strip(),
                'size': sizes
            })

        fit = response.css('.product-feature__text::text').re_first(r'Fit: (.+)')
        fabric = response.css('.product-feature__text::text').re_first(r'Fabric: (.+)')
        neck = response.css('.product-feature__text::text').re_first(r'Neck: (.+)')
        sleeve = response.css('.product-feature__text::text').re_first(r'Sleeve: (.+)')
        pattern = response.css('.product-feature__text::text').re_first(r'Pattern: (.+)')
        length = response.css('.product-feature__text::text').re_first(r'Length: (.+)')
        description = response.css('.product-description p::text').get()

        yield {
            'category': category,
            'url': response.url,
            'title': title,
            'price': price,
            'MRP': mrp,
            'last_7_day_sale': last_7_day_sale,
            'available_skus': available_skus,
            'fit': fit,
            'fabric': fabric,
            'neck': neck,
            'sleeve': sleeve,
            'pattern': pattern,
            'length': length,
            'description': description
        }