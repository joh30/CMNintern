import scrapy




class BrickSetSpider(scrapy.Spider):
    name = 'brick_spider'
    start_urls = ['http://brickset.com/sets/year-2016']

    def parse(self, response):
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'h1 a ::text'
            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            IMAGE_SELECTOR = 'img ::attr(src)'
            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(),
                'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
                'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
                'image': brickset.css(IMAGE_SELECTOR).extract_first(),
            }
_________________________________________________________________________________________________________________________________________
#OTHER EXAMPLES
'''
'''
class RedditSpider(scrapy.Spider):
    name = 'RedditBot'
    start_urls = ['http://www.reddit.com/r/gameofthrones//']

    def parse(self, response):
        # Extracting the content using css selectors
        titles = response.css('.title.may-blank::text').extract()
        votes = response.css('.score.unvoted::text').extract()
        times = response.css('time::attr(title)').extract()
        comments = response.css('.comments::text').extract()

        # Give the extracted content row wise
        for item in zip(titles, votes, times, comments):
            # create a dictionary to store the scraped info
            scraped_info = {
                'title': item[0],
                'vote': item[1],
                'created_at': item[2],
                'comments': item[3],
            }

            # yield or give the scraped info to scrapy
            yield scraped_info
            '''

'''class QouteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = {
            'http://quotes.toscrape.com/'
}

    def parse(self, response):
        all_div_quotes = response.css('div.quote')

        title =  all_div_quotes.css('span.text::text').extract()
        author = all_div_quotes.css('.author::text').extract()
        tag = all_div_quotes.css('.tag::text').extract()
        yield{
            'title' : title,
            'author' : author,
            'tag' : tag,
        }'''
