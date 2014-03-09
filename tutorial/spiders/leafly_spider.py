from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from items import *

class LeaflySpider(CrawlSpider):
    name = "leafly"
    allowed_domains = ["leafly.com"]
    start_urls = [
        "http://www.leafly.com/dispensary-info/berkeley-patients-group"
    ]
    rules = [Rule(SgmlLinkExtractor(allow=['/menu']), 'parseMenu')]

    def parse(self, response):
        sel = Selector(response)
        item = LeaflyOverviewItem()
        item['name'] = sel.xpath('//h1[@itemprop="name"]/text()').extract()
        item['street'] = sel.xpath('//span[@itemprop="street-address"]/text()').extract()
        item['city'] = sel.xpath('//span[@itemprop="locality"]/text()').extract()
        item['state'] = sel.xpath('//span[@itemprop="region"]/text()').extract()
        item['zipcode'] = sel.xpath('//div[@class="map-address"]/text()').re(r'[0-9]+')
        item['followers'] = sel.xpath('//div[@class="info-line"]/text()').re(r'[0-9]+')
        item['numReviews'] = sel.xpath('//span[@itemprop="votes"]/text()').extract()
        item['avgReview'] = sel.xpath('//span[@itemprop="average"]/text()').extract()
        return item

    def parseMenu(self, response):
        sel = Selector(response)
        #sel.xpath('//div[@data-typeid=0]//div[@class="menu-item has-details"]//a/@title').extract()
        #gets the names of all the flowers
        #sel.xpath('//a[@title="All Star Banana Kush"]/../../../div[@class="rating"]/div/img/@title').extract()
        #gets the rating of a particular flower
        #sel.xpath('//a[@title="All Star Banana Kush"]/../../../..//dt').extract()
        #gets the prices


