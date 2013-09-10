import re
from models import db, Domain, Template
from sqlalchemy.exc import IntegrityError
from datetime import datetime

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class CrawlyPipeline(object):
    """"Store information about websites in wordpress table"""
    def __init__(self):
        pass

    def process_item(self, item, spider):
        if 'WPPipeline' not in getattr(spider, "pipelines"):
            return item

        if item['template']:
            dmain = db.session.query(Domain).filter_by(url_domain=item['url_domain']).first()
            if dmain:
                ## create new template record
                site_template = Template(domain=dmain, template=item['template'],
                        theme=item['theme_name'], date_searched=datetime.now())
                db.session.add(site_template)
                try:
                    db.session.commit()
                except IntegrityError:
                    db.session.rollback()
        return item

class URLPipeline(object):
    """store information about source urls to be processed by other spiders"""

    subdomain_regex = re.compile(r"^http://((([^w])([a-zA-Z0-9-])+)|(w[^w][a-zA-Z0-9-]*)|(ww[^w]([a-zA-Z0-9-])*))\.([a-zA-Z0-9-])+\.(nl)(/)?$")
    def __init__(self):
        pass

    def is_subdomain(self, url):
       return re.match(self.subdomain_regex, url)

    def process_item(self, item, spider):
        if 'URLPipeline' not in getattr(spider, "pipelines"):
            return item

        if self.is_subdomain(item['url']):
            print 'subdomain: ', item['url']
            return item
        try:
            dmain = Domain(url_domain=item['url'],
                        start_url=item['source'],
                        status_code=item['status'],
                        domain_ext=item['domain_ext'])
            db.session.add(dmain)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
        return item
