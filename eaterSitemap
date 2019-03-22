import scrapy
from scrapy.spiders import SitemapSpider

class eaterSitemMapSpider(SitemapSpider):
    name = 'eater'
    allowed_domains = ["eater.com"]
    sitemap_urls = ["https://www.eater.com/sitemaps"]

    custom_settings = {'FEED_URI': "eaterSitemap_%(time)s.csv",
                       'FEED_FORMAT': 'csv'}

    def parse(self, response):
        print("processing:" + response.url)
        
        
        # Extract data using css selectors

        eater_image = response.css('img::attr(src)').extract()
        
        
        # Extract data using xpath


        eater_title=response.xpath("//h2[@class='c-entry-box--compact__title']/a/text()").extract()
        eater_author=response.xpath("//span[@class='c-byline__item']/a/text()").extract()
        eater_type=response.xpath("//meta[@property='og:type']/@content").extract()
        eater_publishedtime = response.xpath("//meta[@property='article:published_time']/@content").extract()
        eater_modifiedtime = response.xpath("//meta[@property='article:modified_time']/@content").extract()
        #eater_labels = response.xpath("//li[@class='c-entry-group-labels__item']/span/text()").extract()
        eater_subtitle = response.xpath("//meta[@property='og:description']/@content").extract()
        #eater_articleLinks = response.xpath("//div[@class='c-entry-content']/@href").extract()

        row_data = zip(eater_title, eater_type, eater_subtitle, eater_labels, eater_author, eater_publishedtime, eater_modifiedtime, eater_image)

        # Making extracted data row wise
        for item in row_data:
            # create a dictionary to store the scraped info
            scraped_info = {
                # key:value
                'page': response.url,
                'eater_title': item[0],
                'eater_type': item[1],
                'eater_subtitle': item[2],
                'eater_labels': item[3],
                'eater_author': item[4],
                'eater_publishedtime': item[5],
                'eater_modifiedtime': item[6],
                'eater_image': item[7]
            }

            # yield or give the scraped info to scrapy
            yield scraped_info

            NEXT_PAGE_SELECTOR = 'c-pagination__next c-pagination__link p-button + a::attr(href)'
            next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse)
