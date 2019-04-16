Updated on April 16th, 2019

import scrapy
from scrapy.spiders import SitemapSpider

class eaterSitemMapSpider(SitemapSpider):
    name = 'arstechnica'
    allowed_domains = ["arstechnica.com"]
    sitemap_urls = ["https://arstechnica.com/sitemap.xml"]

    custom_settings = {'FEED_URI': "arstechnica_%(time)s.csv",
                       'FEED_FORMAT': 'csv'}

    def parse(self, response):

        print("processing:" + response.url)
        # Extract data using xpath

        ars_title=response.xpath("//meta[@property='og:title']/@content").extract()
        ars_description = response.xpath("//meta[@property='og:description']/@content").extract()
        ars_image = response.xpath("//meta[@property='og:image']/@content").extract()
        ars_url = response.xpath("//meta[@property='og:url']/@content").extract()
        ars_datetime = response.xpath("//time[@class='date']/text()").extract()
        ars_author = response.xpath("//a[@itemprop='url']/span/text()").extract()
        ars_type = response.xpath("//meta[@property='og:type']/@content").extract()

        ars_body = response.xpath("//div[@itemprop='articleBody']")
        for p in ars_body.xpath('.//p//text()'):
             print(p.get())

        ars_links = response.xpath("//div[@itemprop='articleBody']")
        for href in ars_links.xpath('.//href'):
             print(href.get())

        row_data = zip(ars_title,ars_description, ars_image,ars_url, ars_author, ars_type, ars_datetime)

        # Making extracted data row wise
        for item in row_data:
            # create a dictionary to store the scraped info
            scraped_info = {
                # key:value
                'page': response.url,
                'ars_title': item[0],
                'ars_description': item[1], 
                'ars_image': item[2],
                'ars_url': item[3],
                'ars_author': item[4],
                'ars_type': item[5],
                'ars_datetime': item[6],
            }

            # yield or give the scraped info to scrapy
            yield scraped_info

            NEXT_PAGE_SELECTOR = 'c-pagination__next c-pagination__link p-button + a::attr(href)'
            next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse)
