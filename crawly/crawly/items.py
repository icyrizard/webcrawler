# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class CrawlyItem(Item):
    # define the fields for your item here like:
    # name = Field()
    name = Field()
    theme_name = Field()
    link = Field()
    wordpress = Field()

class URLItem(Item):
    source = Field()
    url = Field()
    country_code = Field()



