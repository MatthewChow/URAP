from scrapy.spider import Spider
from scrapy.selector import Selector

from tutorial.items import LeaflyItem

class LeaflySpider(Spider):
    name = "leafly"
    allowed_domains = ["leafly.com"]
    start_urls = [
        "http://www.leafly.com/hybrid/blue-dream"
    ]

    def parse(self, response):
        sel = Selector(response)
	item = LeaflyItem()

	item['strain_name'] = sel.xpath('//section[@id="header"]/h1/text()').extract()
	item['strain_type'] = sel.xpath('//div[@class="panel"]/div[1]/div[@class="info"]/span[@class="type"]/text()').extract()
	item['strain_highlights'] = sel.xpath('//div[@class="text"]/p/text()').extract()
    	item['avg_rating'] = sel.xpath('//span[@itemprop="average"]/text()').extract()
	item['num_of_review'] = sel.xpath('//div[@class="reviews"]/div/text()').extract()

	flavor = sel.xpath('//div[@class="flavors-list"]/ul')
	item['flavor_one'] = flavor.xpath('li[1]/a[2]/span/text()').extract()
	item['flavor_two'] = flavor.xpath('li[2]/a[2]/span/text()').extract()
	item['flavor_three'] = flavor.xpath('li[3]/a[2]/span/text()').extract()

	effect = sel.xpath('//div[@class="chart effects active"]/dl')	
	item['effect_one'] = effect.xpath('dt[1]/a/text()').extract()
	item['effect_one_score'] = effect.xpath('dd[1]/div/@data-width').extract()
	item['effect_two'] = effect.xpath('dt[2]/a/text()').extract()
	item['effect_two_score'] = effect.xpath('dd[2]/div/@data-width').extract()
	item['effect_three'] = effect.xpath('dt[3]/a/text()').extract()
	item['effect_three_score'] = effect.xpath('dd[3]/div/@data-width').extract()
	item['effect_four'] = effect.xpath('dt[4]/a/text()').extract()
	item['effect_four_score'] = effect.xpath('dd[4]/div/@data-width').extract()
	item['effect_five'] = effect.xpath('dt[5]/a/text()').extract()
	item['effect_five_score'] = effect.xpath('dd[5]/div/@data-width').extract()

	medical = sel.xpath('//div[@class="chart medical"]/dl')
	item['medical_one'] = medical.xpath('dt[1]/a/text()').extract()
	item['medical_one_score'] = medical.xpath('dd[1]/div/@data-width').extract()
	item['medical_two'] = medical.xpath('dt[2]/a/text()').extract()
	item['medical_two_score'] = medical.xpath('dd[2]/div/@data-width').extract()
	item['medical_three'] = medical.xpath('dt[3]/a/text()').extract()
	item['medical_three_score'] = medical.xpath('dd[3]/div/@data-width').extract()
	item['medical_four'] = medical.xpath('dt[4]/a/text()').extract()
	item['medical_four_score'] = medical.xpath('dd[4]/div/@data-width').extract()
	item['medical_five'] = medical.xpath('dt[5]/a/text()').extract()
	item['medical_five_score'] = medical.xpath('dd[5]/div/@data-width').extract()

	negative = sel.xpath('//div[@class="chart negatives"]/dl')
	item['negative_one'] = negative.xpath('dt[1]/text()').extract()
	item['negative_one_score'] = negative.xpath('dd[1]/div/@data-width').extract()
	item['negative_two'] = negative.xpath('dt[2]/text()').extract()
	item['negative_two_score'] = negative.xpath('dd[2]/div/@data-width').extract()
	item['negative_three'] = negative.xpath('dt[3]/text()').extract()
	item['negative_three_score'] = negative.xpath('dd[3]/div/@data-width').extract()
	item['negative_four'] = negative.xpath('dt[4]/text()').extract()
	item['negative_four_score'] = negative.xpath('dd[4]/div/@data-width').extract()
	item['negative_five'] = negative.xpath('dt[5]/text()').extract()
	item['negative_five_score'] = negative.xpath('dd[5]/div/@data-width').extract()

	popular = sel.xpath('//div[@id="most-popular-at"]/ol')	
	item['most_popular_one'] = popular.xpath('li[1]/a/text()').extract()
	item['most_popular_two'] = popular.xpath('li[2]/a/text()').extract()
	item['most_popular_three'] = popular.xpath('li[3]/a/text()').extract()
	item['most_popular_four'] = popular.xpath('li[4]/a/text()').extract()
	item['most_popular_five'] = popular.xpath('li[5]/a/text()').extract()
	item['most_popular_six'] = popular.xpath('li[6]/a/text()').extract()
	item['most_popular_seven'] = popular.xpath('li[7]/a/text()').extract()
	item['most_popular_eight'] = popular.xpath('li[8]/a/text()').extract()
	item['most_popular_nine'] = popular.xpath('li[9]/a/text()').extract()
	item['most_popular_ten'] = popular.xpath('li[10]/a/text()').extract()
	
	return item



