# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class LeaflyOverviewItem(Item):
    name = Field()
    street = Field()
    city = Field()
    state = Field()
    zipcode = Field()
    followers = Field()
    numReviews = Field()
    avgReview = Field()
        
class LeaflyMenuItem(Item):
    name = Field()
    
