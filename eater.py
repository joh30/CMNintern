import scrapy
import csv

class eaterSpider(scrapy.Spider):
    name = 'eater'
    #allowed_domains = ['https://www.eater.com/']
    start_urls = ['https://www.eater.com/',
                  'https://www.eater.com/archives',
                  'https://www.eater.com/archives/2']
    custom_settings = {'FEED_URI': "eater_%(time)s.csv",
                       'FEED_FORMAT': 'csv'}

    def parse(self, response):
        print("processing:" + response.url)
        # Extract data using css selectors
        # Extract data using xpath


        eater_title = response.xpath("//h2[@class='c-entry-box--compact__title']/a/text()").extract()
        eater_author = response.xpath("//span[@class='c-byline__item']/a/text()").extract()
        eater_publishedtime = response.xpath("//span[@class='c-byline__item']/time/text()").extract()
        eater_source = response.xpath("//li[@class='c-entry-box--compact__label c-entry-box--compact__label-primary']/a/span/text()").extract()
        #eater_subtitle = response.xpath("//h2[@class='c-entry-summary p-dek']/text()").extract()
        eater_image = response.css('img::attr(src)').extract()


        row_data = zip(eater_title, eater_image, eater_author, eater_source, eater_publishedtime)

        # Making extracted data row wise
        for item in row_data:
            # create a dictionary to store the scraped info
            scraped_info = {
                # key:value
                'page': response.url,
                'eater_title': item[0],
                'eater_image': item[1],
                'eater_author': item[2],
                'eater_source': item[3],
                'eater_publishedtime': item[4]
            }



            # yield or give the scraped info to scrapy
            yield scraped_info

            NEXT_PAGE_SELECTOR = '.ui-pagination-active + a::attr(href)'
            next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse)
