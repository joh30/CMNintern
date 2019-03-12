#ALL OF THIS CODE DOES NOT BELONG TO ME!
#REFERENCE 'https://www.datacamp.com/community/tutorials/making-web-crawlers-scrapy-python#shell'

import scrapy
import csv

class AliexpressTabletsSpider(scrapy.Spider):
    name = 'aliexpress_tablets'
    allowed_domains = ['aliexpress.com']
    start_urls = ['https://www.aliexpress.com/category',
                  'https://www.aliexpress.com/category/200216607/tablets/2.html?site=glo&g=y&tag=']

    def parse(self, response):
        print("procesing:" + response.url)
        # Extract data using css selectors
        product_name = response.css('.product::text').extract()
        price_range = response.css('.value::text').extract()
        # Extract data using xpath
        orders = response.xpath("//em[@title='Total Orders']/text()").extract()
        company_name = response.xpath("//a[@class='store $p4pLog']/text()").extract()

        row_data = zip(product_name, price_range, orders, company_name)

        # Making extracted data row wise
        for item in row_data:
            # create a dictionary to store the scraped info
            scraped_info = {
                # key:value
                'page': response.url,
                'product_name': item[0],
            # item[0] means product in the list and so on, index tells what value to assign
                'price_range': item[1],
                'orders': item[2],
                'company_name': item[3],
            }

            # yield or give the scraped info to scrapy
            yield scraped_info
#____________________________________________________________________________________________________________________________________
#PYCHARM TERMINAL
#NOTE: OUTPUT (>>), INPUT (<<), WILL LEAVE AT LEAST 4 ENTER SPACES TO HELP DIFFERENTIATE THE INPUT AND OUTPUTS

<<
(venv) C:\Users\jyo30\PycharmProjects\untitled>scrapy runspider scraper3.py -o out_file.csv -t csv




>>
2019-03-12 15:10:52 [scrapy.utils.log] INFO: Scrapy 1.6.0 started (bot: scrapybot)
2019-03-12 15:10:52 [scrapy.utils.log] INFO: Versions: lxml 4.3.1.0, libxml2 2.9.5, cssselect 1.0.3, parsel 1.5.1, w3lib 1.20.0, Twisted 18.9.0, Python 3.7.1 (default, Dec 10 2018, 22:54:23
) [MSC v.1915 64 bit (AMD64)], pyOpenSSL 19.0.0 (OpenSSL 1.1.1a  20 Nov 2018), cryptography 2.5, Platform Windows-10-10.0.17134-SP0
2019-03-12 15:10:52 [scrapy.crawler] INFO: Overridden settings: {'FEED_FORMAT': 'csv', 'FEED_URI': 'out_file.csv', 'SPIDER_LOADER_WARN_ONLY': True}
2019-03-12 15:10:52 [scrapy.extensions.telnet] INFO: Telnet Password: 5d32a99ed1a6d066
2019-03-12 15:10:53 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.feedexport.FeedExporter',
 'scrapy.extensions.logstats.LogStats']
2019-03-12 15:10:53 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2019-03-12 15:10:53 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2019-03-12 15:10:53 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2019-03-12 15:10:53 [scrapy.core.engine] INFO: Spider opened
2019-03-12 15:10:54 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2019-03-12 15:10:54 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2019-03-12 15:10:54 [scrapy.core.engine] DEBUG: Crawled (404) <GET https://www.aliexpress.com/category> (referer: None)
2019-03-12 15:10:54 [scrapy.downloadermiddlewares.redirect] DEBUG: Redirecting (301) to <GET https://www.aliexpress.com/category/200216607/tablet/2.html> from <GET https://www.aliexpress.co
m/category/200216607/tablets/2.html?site=glo&g=y&tag=>
2019-03-12 15:10:54 [scrapy.spidermiddlewares.httperror] INFO: Ignoring response <404 https://www.aliexpress.com/category>: HTTP status code is not handled or not allowed
2019-03-12 15:10:55 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.aliexpress.com/category/200216607/tablet/2.html> (referer: None)
procesing:https://www.aliexpress.com/category/200216607/tablet/2.html
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'BDF 10 inch 3G Phone Call SIM card Android 6.0 Quad Core CE WiFi FM 16GB Tablet Pc', 'price_range':
'US $62.00 - 68.20', 'orders': ' Orders  (628)', 'company_name': 'BDF Official Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'Lonwalk T10 10 inch 10 Core Tablet PC Android 7.0 4GB RAM 128GB ROM Screen', 'price_range': 'US $95.
15 - 124.02', 'orders': ' Orders  (110)', 'company_name': 'ShenZhen Yell-Cool Technology Co.,Ltd.'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'BDF 2018 Russian Moscow Warehouse 10 Inch Mobile Sim Card Tablet Pc 16GB Quad Core', 'price_range':
'US $71.89 - 79.00', 'orders': ' Orders  (100)', 'company_name': 'BDF Official Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': '2019 New 10 inch 3G 4G LTE Tablet PC Octa Core 4GB RAM 64GB ROM 1280*800 IPS  10.1 GPS Tablets Andro
id 8.0 DHL free +Gifts', 'price_range': 'US $74.99 - 92.99', 'orders': ' Orders  (71)', 'company_name': 'honyuda Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'DHL Free Shipping 10 inch Tablet PC Ocat Core 4GB RAM 64GB ROM Android 7.0 GPS 5.0MP 1280*800 IPS 3G
 4G LTE Tablet PC 10.1" k107', 'price_range': 'US $70.29 - 79.17', 'orders': ' Orders  (14)', 'company_name': 'honyuda Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': '10 inch Octa Core 3G Tablet Android 5.1 RAM 4GB ROM 32GB 5.0MP Dual SIM Card Bluetooth GPS Tablets 9
.6 inch/ 10.1 inch tablet pc', 'price_range': 'US $190.00 - 210.00', 'orders': ' Orders  (3)', 'company_name': 'Shenzhen HongyangTechnology Co., Ltd.'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'DHL Free 2017 Newest 10 Inch Tablet PC 4G LTE Octa Core 4GB RAM 64GB ROM Dual SIM 8MP Android 6.0 GP
S 1920*1200 IPS Tablet PC10"', 'price_range': 'US $226.00 - 258.00', 'orders': ' Orders  (0)', 'company_name': 'Shenzhen HongyangTechnology Co., Ltd.'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'Xiaomi Mi Pad 4 Plus PC 10.1" Snapdragon 660 Octa Core Face 1920x1200 Tablets Android', 'price_range
': 'US $305.99 - 352.99', 'orders': ' Orders  (479)', 'company_name': 'Mi France Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': '2019 New 10 Inch Tablet MediaTek Octa Core 4G LTE 1280x800 IPS HD 5.0MP 4GB RAM 64GB ROM Android 8.0
 GPS Tablets 10.1 Gifts', 'price_range': 'US $77.81 - 100.96', 'orders': ' Orders  (0)', 'company_name': 'Tablets Global Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'CHUWI Hi10 Air Intel Quad Core Windows 10 Tablet 10.1 Inch 4GB RAM 64GB ROM 1 Tablet', 'price_range'
: 'US $189.70 - 237.13', 'orders': ' Orders  (645)', 'company_name': 'CHUWI Official Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'BEESITTO 2019 10 Inch Tablet PC 3G 4G LTE Octa Core 4GB RAM 64GB ROM Android 8.0', 'price_range': 'U
S $70.99 - 85.99', 'orders': ' Orders  (463)', 'company_name': 'Tablet Factory Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'Xiaomi Mi Pad 4 MiPad 4 OTG 660 Octa Core Tablets PC 1920x1200 kids Tablet Android', 'price_range':
'US $175.99 - 218.99', 'orders': ' Orders  (618)', 'company_name': 'Mi France Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': "CARBAYTA 2019 S119 10.1' Android 8.0 Octa Core 32GB 64GB ROM Dual Camera Tablet PC", 'price_range':
'US $84.24 - 139.62', 'orders': ' Orders  (28)', 'company_name': 'Tablet consulting center Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'BDF 2018 Best-Selling 10 inch 3G Phone Call Quad Core Tablet pc Android 4G 32G tablet', 'price_range
': 'US $73.13 - 103.88', 'orders': ' Orders  (534)', 'company_name': 'Shenzhen Skyline Technology Co.,Ltd '}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'Lonwalk 2018 2.5D 10 Inch Android 7.0 Tablet PC 1280x800 Octa Core 4GB RAM 128GB ROM', 'price_range'
: 'US $88.73 - 108.11', 'orders': ' Orders  (305)', 'company_name': 'Lontab Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'BOBARRY 1920*1200 IPS 10.1 Inch Android 7.0 Tablet PC Tab 128GB 10 Core tablet pcs', 'price_range':
'US $100.73 - 129.53', 'orders': ' Orders  (11)', 'company_name': 'BOBA Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'ALLDOCUBE 10.1" Tablets PC iwork10 Pro Full View IPS 1920*1200 4GB RAM 64GB ROM', 'price_range': 'US
 $178.02 - 217.26', 'orders': ' Orders  (186)', 'company_name': 'ALLDOCUBE Official Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'ZONNYOU 10.1 inches Tablet PC Android 7.0 3G Phone Call Octa -Core 4GB Ram 32GB Rom', 'price_range':
 'US $74.51 - 78.47', 'orders': ' Orders  (526)', 'company_name': 'ShenZhen GO GO co Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': "VOYO I8 Max LTE Phablet Android 7.1 10.1'' MTK6797 Deca Core 4GB 64GB 13MP Tablet PC", 'price_range'
: 'US $180.62 - 212.49', 'orders': ' Orders  (59)', 'company_name': 'Toptech 3C Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'FULCOL 2.5D Tempered Glass 10 inch Android 8.0 3G 4G LTE Tablet PC 4GB RAM 64GB ROM', 'price_range':
 'US $73.03 - 87.99', 'orders': ' Orders  (240)', 'company_name': 'Android phone Tablets Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'CARBAYTA MT6753 Android 8.0 Smart tablet pcs tablet pc 10.1 inch Octa 8 core 64GB', 'price_range': '
US $129.50 - 161.88', 'orders': ' Orders  (100)', 'company_name': 'TD Tablet Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'BEESITTO 2019 10 inch Octa Core 3G 4G FDD LTE Screen Android 7.0 Tablet', 'price_range': 'US $76.79
- 100.79', 'orders': ' Orders  (59)', 'company_name': 'Best Deal Group'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'CHUWI Hi9 Pro Android 8.0 4G LTE Tablet PC MT6797 X20 Deca Core 3GB RAM 32GB ROM', 'price_range': 'U
S $146.78', 'orders': ' Orders  (483)', 'company_name': 'CHUWI Official Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'ALLDOCUBE X1 4G Phone Call Tablet PC 8.4 Inch Deca core Android 7.1 4GB RAM 64GB ROM', 'price_range'
: 'US $183.33', 'orders': ' Orders  (60)', 'company_name': 'ALLDOCUBE Official Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'FULCOL 10 Inch Tablet pc Android 6.0 Octa Core 4GB RAM 64GB ROM dual sim kids Tablets', 'price_range
': 'US $64.16 - 77.96', 'orders': ' Orders  (945)', 'company_name': 'Android phone Tablets Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'CHUWI Hi9 Air 10.1 inch Android 8.0 Tablet PC MT6797 X20 Deca Core 4GB RAM 64GB ROM', 'price_range':
 'US $184.79 - 292.59', 'orders': ' Orders  (161)', 'company_name': 'CHUWI QH Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'BDF 7 Inch Android 6.0 small computer 3G Phone Call Tablets Pc WiFi Quad core', 'price_range': 'US $
46.20 - 62.98', 'orders': ' Orders  (137)', 'company_name': 'SHENZHEN BDF TOUCH TECHNOLOGY CO.,LTD.'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'Teclast T20 Fingerprint Tablet PC MT6797 X27 Deca Core 4GB 64GB 10.1 inch Android 7.0', 'price_range
': 'US $199.80', 'orders': ' Orders  (872)', 'company_name': 'Teclast Global Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'Lonwalk Android Tablet PC Tab Pad 10 Inch IPS 10 Core 4GB RAM 64GB ROM Dual SIM Card', 'price_range'
: 'US $95.99 - 110.40', 'orders': ' Orders  (59)', 'company_name': 'Tablets Android Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'BEESITTO Android 7.0 10 inch tablet Octa Core 4GB RAM 64GB ROM Kids Tablets 10 10.1', 'price_range':
 'US $77.50 - 96.95', 'orders': ' Orders  (2031)', 'company_name': 'Peakier tablets Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'CIGE MediaPad 10.1 inch Tablet PC Android 7.0 Octa Core 4GB RAM 64GB ROM Dual Camera', 'price_range'
: 'US $79.68 - 124.91', 'orders': ' Orders  (11)', 'company_name': 'CG Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'VOYO i8 Max 4G Phablet Android Tablet 7.1 10.1 inch MTK6797 4GB RAM 64GB ROM', 'price_range': 'US $1
70.99', 'orders': ' Orders  (30)', 'company_name': 'Globale Electronic Style Co.,Ltd'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': "ALLDOCUBE iWork 10 Pro 2 in 1 Tablet PC 10.1'' Windows 10 Android 5.1 Quad Core 64GB", 'price_range'
: 'US $0.82', 'orders': ' Orders  (3)', 'company_name': 'Safe Security Camera Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'Lonwalk 10 inch Tablet Android 7.0 OS Octa Core 2.5G 1280*800 IPS Galss Bluetooth 4.0', 'price_range
': 'US $163.99 - 199.99', 'orders': ' Orders  (63)', 'company_name': 'ShenZhen Yell-Cool Technology Co.,Ltd.'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'Lenovo P8 Tab3 8 Plus 8.0 Inch 4G Tablet PC Android 6.0 Snapdragon 625 Octa Core 16GB', 'price_range
': 'US $88.19 - 105.83', 'orders': ' Orders  (101)', 'company_name': 'Toptech 3C Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'FULCOL 10 inch tablet pc Octa Core 3G 4G FDD LTE 4GB RAM 32GB ROM Bluetooth Wifi', 'price_range': 'U
S $163.99 - 173.99', 'orders': ' Orders  (6)', 'company_name': 'Top Tablets Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'BDF Super Nice 7 Inch Screen Android 6.0 Phone Call Tablet Pc 1G RAM 16G ROM 1024*600', 'price_range
': 'US $68.99 - 89.99', 'orders': ' Orders  (48)', 'company_name': 'Mon Cheng Tablets Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'perkbox 10 Inch tablet Support Youtube Octa Core 4GB RAM 64GB ROM 3G Android 8.0', 'price_range': 'U
S $45.68 - 64.61', 'orders': ' Orders  (830)', 'company_name': 'China Tablet Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'FULCOL Google play 10 inch Tablet android 8.0 Octa Core kids Tablets 4GB RAM 64GB ROM', 'price_range
': 'US $81.69 - 103.19', 'orders': ' Orders  (131)', 'company_name': 'Shenzhen TopTab Technology Co.,Ltd'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'perkbox 2019 Google Play Store Android 8.0 OS 10 inch tablet 4GB RAM 64GB ROM', 'price_range': 'US $
68.30 - 84.86', 'orders': ' Orders  (34)', 'company_name': 'China Tablet Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'BEESITTO 2019 10 inch Octa Core 4GB RAM 64GB ROM Android 7.0 Tablets 10 10.1', 'price_range': 'US $7
1.39 - 92.39', 'orders': ' Orders  (70)', 'company_name': 'Tablet Factory Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'Lonwalk 10 inch 4G LTE Phone call Octa Core 4GB RAM 32GB ROM android 10.1 tablet PC', 'price_range':
 'US $73.13 - 88.31', 'orders': ' Orders  (284)', 'company_name': 'Lontab Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'Glavey 4G LTE Phone Call tablet 7 Inch MTK6735 Quad core Android 5.1 1GB 8GB 1024*600', 'price_range
': 'US $76.79 - 100.80', 'orders': ' Orders  (15)', 'company_name': 'DIGITALTOOLS Technology Ltd. '}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'BOBARRY T900 Android 8.0 tablet pcs tablet pc 10.1 inch Octa core 128GB 1920X1200', 'price_range': '
US $46.78 - 51.28', 'orders': ' Orders  (79)', 'company_name': 'BOBA Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'OYYU T11 10.1 inch Phablets Android 7.0 3G Phone Call Tablet Pc Quad Core 1.3GHz 16GB', 'price_range
': 'US $116.07 - 133.67', 'orders': ' Orders  (6)', 'company_name': 'Shenzhen Luckystars Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'BOBARRY T100 10 inch 10 Core Tablet PC Android 7.0 4GB RAM 128GB ROM Screen', 'price_range': 'US $69
.01 - 75.77', 'orders': ' Orders  (12)', 'company_name': 'Weilian Store'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'ALLDOCUBE M5X 10.1 Inch 4G Tablet PC 4GB RAM 64GB ROM Android 8.0 Deca Core', 'price_range': 'US $94
.83 - 131.33', 'orders': ' Orders  (35)', 'company_name': 'MC Computer accessories Technology Co., Ltd.'}
2019-03-12 15:10:55 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aliexpress.com/category/200216607/tablet/2.html>
{'page': 'https://www.aliexpress.com/category/200216607/tablet/2.html', 'product_name': 'VOYO i3 wifi 2 in 1 10.1 Inch 1920*1200 Tablet PC Win10 Intel X5 Quad Core 8G RAM', 'price_range': '
US $168.99 - 194.99', 'orders': ' Orders  (22)', 'company_name': 'Voyo Factory Store'}
2019-03-12 15:10:55 [scrapy.core.engine] INFO: Closing spider (finished)
2019-03-12 15:10:55 [scrapy.extensions.feedexport] INFO: Stored csv feed (48 items) in: out_file.csv
2019-03-12 15:10:55 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 1317,
 'downloader/request_count': 3,
 'downloader/request_method_count/GET': 3,
 'downloader/response_bytes': 39914,
 'downloader/response_count': 3,
 'downloader/response_status_count/200': 1,
 'downloader/response_status_count/301': 1,
 'downloader/response_status_count/404': 1,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2019, 3, 12, 19, 10, 55, 532850),
 'httperror/response_ignored_count': 1,
 'httperror/response_ignored_status_count/404': 1,
 'item_scraped_count': 48,
 'log_count/DEBUG': 51,
 'log_count/INFO': 11,
 'response_received_count': 2,
 'scheduler/dequeued': 3,
 'scheduler/dequeued/memory': 3,
 'scheduler/enqueued': 3,
 'scheduler/enqueued/memory': 3,
 'start_time': datetime.datetime(2019, 3, 12, 19, 10, 54, 10376)}
2019-03-12 15:10:55 [scrapy.core.engine] INFO: Spider closed (finished)




<<
(venv) C:\Users\jyo30\PycharmProjects\untitled>scrapy runspider scraper3.py -o out_file.csv -t csv
#EXPORTS ALL OF THE DATA AND SEPERATES EACH INDEX BASED ON WHICH ROW... 
#LOCATE THE CSV FILE FROM PROJECT DIRECTORY, THEN OPEN CSV ON MICROSOFT EXCEL c:







