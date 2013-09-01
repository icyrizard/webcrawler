## author: Richard Torenvliet
import re
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from crawly.items import CrawlyItem
from crawly.models import db, Domain

def get_urls():
    for url in db.session.query(Domain).all():
        yield url.url_domain

class WPCrawlySpider(BaseSpider):
    """Wordpress spider, determines if the list of urls is wordpress"""
    name = "wp-crawly"
    pipelines = ['WPPipeline']

    # patterns, for global use
    wp_content = re.compile(r"wp-content|wp-includes")
    wp_theme = re.compile(r"wp-content/themes/(?P<theme>[a-zA-Z0-9_\-\s\.]+)")

    #allowed_domains = ["dmoz.org"]

    #TODO: From database?
    start_urls = get_urls()

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
                item["template"] = 'wordpress'
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
                item["template"] = 'wordpress'
        return item

    def parse(self, response):
        """Parse method for wordpress spider"""
        # html object
        hxs = HtmlXPathSelector(response)
        # the item to collect information
        item = CrawlyItem()

        ## set default information
        # set website name to url #TODO, change this?
        item['url_domain'] = response._get_url()
        item['theme_name'] = None
        item['template'] = False

        # start checking links
        self._parse_links(hxs, item)

        # if that did'nt work, check all script includes
        if not item['template']:
            self._parse_script_includes(hxs, item)
        return item

