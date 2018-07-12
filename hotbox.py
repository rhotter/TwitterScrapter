import scrapy



class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://twitter.com/realDonaldTrump',
    ]

    def parse(self, response):
        for quote in response.css('div.tweet'):
            yield {
                'name': quote.css('strong::text').extract_first(),
            }
        '''
        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
        '''
