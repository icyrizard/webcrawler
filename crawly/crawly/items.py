# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class CrawlyItem(Item):
    url_domain = Field()
    theme_name = Field()
    template = Field()

class URLItem(Item):
    source = Field()
    url = Field()
    country_code = Field()
    status = Field()
    domain_ext = Field()



