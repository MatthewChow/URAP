from scrapy.spider import Spider
from scrapy.selector import Selector

from LeaflyStrains.items import StrainItem

class StrainSpider(Spider):
    # command to run: scrapy crawl strains -o hybrid_strains.json -t json -a category=hybrid/indica/sativa
    name = "strains"
    allowed_domains = ["leafly.com"]
    
    def __init__(self, category=''):
        self.start_urls = ["http://www.leafly.com/%s" %category]

    def parse(self, response):
        sel = Selector(response)
        item = StrainItem()

        item['strain_websites'] = sel.xpath('//div[@id="details"]/div[1]/div/a/@href').extract()
                
        temp = []        
        for entry in item['strain_websites']:
            clean = entry.encode('ascii','ignore').replace('\r', '').replace('\n', '').replace('\t', '')
            full = "http://www.leafly.com" + clean
            temp.append(full)

        item['strain_websites'] = temp

        return item
