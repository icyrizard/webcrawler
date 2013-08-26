## author: Richard Torenvliet

import re
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from crawly.items import CrawlyItem

class CrawlySpider(BaseSpider):
    """Wordpress spider, determines if the list of urls is wordpress"""
    name = "wp-crawly"
    wp_content = re.compile("wp-content")
    wp_theme = re.compile(r"wp-content/themes/(?P<theme>\w+)")
    #allowed_domains = ["dmoz.org"]
    start_urls = [
            "http://www.academicfactory.nl",
    ]

    def parse(self, response):
        """Parse method for wordpress spider"""
        hxs = HtmlXPathSelector(response)
        ##
        includelinks = hxs.select("//link/@href")

        ## init empty item #TODO: set default values in object?
        item = CrawlyItem()

        # set website name to url
        item['name'] = response._get_url()
        for b in includelinks:
            ## create item
            ## get href string
            href_link = b.extract()

            ## is wordpress ?
            if self.wp_content.search(href_link):

                # wordpress if obviously set to true
                item["wordpress"] = True

                ## set default to unknown
                item['theme_name'] = "unkown"
                theme_name = self.wp_theme.search(href_link)
                # just in case the regex fails to find something
                if theme_name:
                    item["theme_name"] = theme_name.group('theme')
                break
        return item
