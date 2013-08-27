## author: Richard Torenvliet
import re
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from crawly.items import CrawlyItem

class WPCrawlySpider(BaseSpider):
    """Wordpress spider, determines if the list of urls is wordpress"""
    name = "wp-crawly"

    # patterns, for global use
    wp_content = re.compile(r"wp-content")
    wp_theme = re.compile(r"wp-content/themes/(?P<theme>[a-zA-Z0-9_\-\s\.]+)")
    #allowed_domains = ["dmoz.org"]

    #TODO: From database?
    start_urls = [
        "http://www.academicfactory.nl",
    ]

    def _parse_links(self, hxs, item):
        ## links to wordpress urls
        includelinks = hxs.select("//link/@href")

        # tmp variable
        theme_name = item["theme_name"]

        for b in includelinks:
            ## get href string
            href_link = b.extract()

            ## set theme name if not yet found
            if not theme_name:
                theme_name = self.wp_theme.search(href_link)
                if theme_name:
                    item["theme_name"] = theme_name.group('theme')

            ## is wordpress ?
            if self.wp_content.search(href_link):
                # set to true if wordpress
                item["wordpress"] = True
        return item

    def _parse_script_includes(self, hxs, item):
        ## include scripts
        includelinks = hxs.select("//script/@src")
        # tmp variable
        theme_name = item["theme_name"]

        for b in includelinks:
            ## get href string
            href_link = b.extract()
            ## set theme name if not yet found
            if not theme_name:
                theme_name = self.wp_theme.search(href_link)
                if theme_name:
                    item["theme_name"] = theme_name.group('theme')

            ## is wordpress ?
            if self.wp_content.search(href_link):
                # set to true if wordpress
                item["wordpress"] = True
        return item

    def parse(self, response):
        """Parse method for wordpress spider"""
        # html object
        hxs = HtmlXPathSelector(response)
        # the item to collect information
        item = CrawlyItem()

        ## set default information
        # set website name to url #TODO, change this?
        item['name'] = response._get_url()
        item['theme_name'] = None
        item['wordpress'] = False

        # start checking links
        item = self._parse_links(hxs, item)

        # didnt work, check all script includes
        if not item['wordpress']:
            item = self._parse_script_includes(hxs, item)
        return item

