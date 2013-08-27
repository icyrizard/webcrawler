# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class CrawlyPipeline(object):
    """"Store information about websites in wordpress table"""
    def __init__(self):
        pass

    def process_item(self, item, spider):
        if 'crawly' not in getattr(spider, "pipelines"):
            return item
        return item

class URLPipeline(object):
    """store information about source urls to be processed by other spiders"""
    def __init__(self):
        pass

    def process_item(self, item, spider):
        if 'URL' not in getattr(spider, "pipelines"):
            return item
        print item

        return item
