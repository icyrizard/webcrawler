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
    'crawly.pipelines.CrawlyPipeline',
    'crawly.pipelines.URLPipeline'
]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'crawly (+http://www.yourdomain.com)'


## database settings needed to create the connection through SQLAlchemy
## http://docs.sqlalchemy.org/en/rel_0_8/core/engines.html#sqlalchemy.create_engine
DATABASE_LIST = {
    "development" : {
        "DIALECT": "postgresql", # options are: mysql, postgresql, oracle, sqlite
        "DRIVER":"", # if empty, SQLAlchemy uses default driver for dialect
        "NAME" : "webcrawler",
        "USER" : "richard",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "",
    },
    "homepc" : {
        "DIALECT": "mysql", # options are: mysql, postgresql, oracle, sqlite
        "DRIVER":"", # if empty, SQLAlchemy uses default driver for dialect
        "NAME" : "webcrawler",
        "USER" : "root",
        "PASSWORD": "3jkfjk",
        "HOST": "localhost",
        "PORT": "3306",
    }
}

# use the name of the database in DATABASE_LIST
DATABASE = "development"
