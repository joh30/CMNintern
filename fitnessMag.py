import scrapy
import csv

class fitnessMagazineSpider(scrapy.Spider):
    name = 'fitness_magazines'
    #allowed_domains = ['https://www.fitnessmagazine.com/']
    start_urls = ['https://www.fitnessmagazine.com/']
    custom_settings = {'FEED_URI': "fitnessmagazine_%(time)s.csv",
                       'FEED_FORMAT': 'csv'}

    def parse(self, response):
        print("procesing:" + response.url)
        # Extract data using css selectors
        # Extract data using xpath
        article_title = response.xpath("//h4[@class='field-content']/a/text()").extract()
        article_author = response.xpath("//span[@class='byline']/a/text()").extract()
        article_category = response.xpath("//div[@class='field-content']/a/text()").extract()
        article_creation = response.xpath("//em[@class='placeholder']/text()").extract()
        article_subtitle = response.xpath("//meta[@property='og:description']/@content").extract()
        #article_subtitle = response.css('.field-content::p').extract()
        article_image = response.css('img::attr(src)').extract()


        row_data = zip(article_title, article_image, article_author, article_category, article_creation, article_subtitle)

        # Making extracted data row wise
        for item in row_data:
            # create a dictionary to store the scraped info
            scraped_info = {
                # key:value
                'page': response.url,
                'article_title': item[0],
                'article_image': item[1],
                'article_author': item[2],
                'article_category': item[3],
                'article_creation': item[4],
                'article_subtitle': item[5]

            }



            # yield or give the scraped info to scrapy
            yield scraped_info

            NEXT_PAGE_SELECTOR = '.ui-pagination-active + a::attr(href)'
            next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse)
