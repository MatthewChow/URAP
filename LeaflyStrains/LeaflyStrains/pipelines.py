# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
from scrapy.contrib.exporter import CsvItemExporter

class CSVPipeline(object):

	def __init__(self):
		self.files = {}
		
	@classmethod
	def from_crawler(cls, crawler):
		pipeline = cls()
		crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
		crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
		return pipeline
		
	def spider_opened(self, spider):
		file = open('%s_items.csv' % spider.name, 'w+b')
		self.files[spider] = file
		self.exporter = CsvItemExporter(file)
		self.exporter.fields_to_export = ['scrape_date', 'scrape_time', 'strain_name', 'strain_type', 'website', 'strain_highlights', 'num_ratings', 'avg_rating', 'num_of_review', 'flavor_one', 'flavor_two', 'flavor_three', 'effect_one', 'effect_one_score', 'effect_two', 'effect_two_score', 'effect_three', 'effect_three_score', 'effect_four', 'effect_four_score', 'effect_five', 'effect_five_score', 'medical_one', 'medical_one_score', 'medical_two', 'medical_two_score', 'medical_three', 'medical_three_score', 'medical_four', 'medical_four_score', 'medical_five', 'medical_five_score', 'ailment_one', 'ailment_two', 'ailment_three', 'ailment_four', 'ailment_five', 'negative_one', 'negative_one_score', 'negative_two', 'negative_two_score', 'negative_three', 'negative_three_score', 'negative_four', 'negative_four_score', 'negative_five', 'negative_five_score', 'most_popular_one', 'most_popular_two', 'most_popular_three', 'most_popular_four', 'most_popular_five', 'most_popular_six', 'most_popular_seven', 'most_popular_eight', 'most_popular_nine', 'most_popular_ten']
		self.exporter.start_exporting()
		
	def spider_closed(self, spider):
		self.exporter.finish_exporting()
		file = self.files.pop(spider)
		file.close()
		
	def process_item(self, item, spider):
		self.exporter.export_item(item)
		return item

class LeaflyStrainsPipeline(object):
    def process_item(self, item, spider):
        return item
