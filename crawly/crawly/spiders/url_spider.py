# This spider crawls webpages to get as much urls as possible
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from crawly.items import URLItem

class StartpaginaCrawlySpider(CrawlSpider):
    """This crawler is build to strip 'startpagina' websites to get
    new urls"""
    pipelines = ['URLPipeline']
    name = "startpagina-crawly"

    start_urls = ["http://webdesign.startpagina.nl/"]
    rules = (Rule (SgmlLinkExtractor(
        allow=r"^http://([a-zA-Z0-9-\.])+\.nl(/)?$",
        deny=r".*mailto:.*",
        tags="a",
        unique=True,
        deny_domains=['hyves.nl', 'facebook.nl', 'google.nl', 'istats.nl']),
        callback="parse_items", follow=True),)

    #def _parse_anchors(self, hxs, item):
    #    anchors = hxs.select("//a")
    #    #for a in anchors:
    #    #    print a.select("@href").extract()
    #    return item

    def parse_items(self, response):
        # html object
        print response._get_url()
        hxs = HtmlXPathSelector(response)
        item = URLItem()

        item['source'] = self.start_urls[0]
        item['url'] = response._get_url()
        item['status'] = response.status
        item['country_code'] = "NL"

        #self._parse_anchors(hxs, item)
        return item

