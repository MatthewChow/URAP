from scrapy.spider import Spider
from scrapy.selector import Selector

class LeaflySpider(Spider):
    name = "leafly"
    allowed_domains = ["leafly.com"]
    start_urls = [
        "http://www.leafly.com/hybrid/blue-dream"
    ]

    def parse(self, response):
        sel = Selector(response)
        """
	sites = sel.xpath('//ul/li')
        for site in sites:
            title = site.xpath('a/text()').extract()
            link = site.xpath('a/@href').extract()
            desc = site.xpath('text()').extract()
            print title, link, desc
	"""
	# strain_name = sel.xpath('//


