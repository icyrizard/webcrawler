# Scrapy settings for crawly project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'wp-crawly'

SPIDER_MODULES = ['crawly.spiders']
NEWSPIDER_MODULE = 'crawly.spiders'
ITEM_PIPELINES = [
    'crawly.pipelines.CrawlyPipeline'
]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'crawly (+http://www.yourdomain.com)'
